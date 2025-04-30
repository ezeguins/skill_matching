import streamlit as st
import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer
import faiss
import os
os.environ["STREAMLIT_SERVER_ENABLE_FILE_WATCHER"] = "false"
import torch
torch.classes.__path__ = []
import zipfile

from pathlib import Path

def unzip_to_current_dir(zip_path):
    """Uncompress a ZIP file into the current directory."""
    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            # Extract all files to the current directory
            zip_ref.extractall()  # No argument = extract to current directory
            
            # List extracted files
            extracted_files = zip_ref.namelist()
            
        print(f"Files extracted to current directory: {os.getcwd()}")
        return extracted_files
        
    except FileNotFoundError:
        print(f"Error: ZIP file not found at {zip_path}")
    except zipfile.BadZipFile:
        print("Error: File is not a valid ZIP archive")
    except Exception as e:
        print(f"Unexpected error: {str(e)}")

# Path to your ZIP file
zip_path = "filtered_skills_10M_embeddings.zip"
extracted_files = unzip_to_current_dir(zip_path)
if extracted_files:
    print("Extracted files:", extracted_files)

# --------------------
# Configuration
# --------------------
AGG_CSV = 'filtered_skills_10M_SkillsEmbeddings.csv'   # Aggregated embeddings per Identifier
PER_SKILL_CSV = 'filtered_skills_10M_embeddings.csv'  # Per-skill embeddings
MODEL_NAME = 'model'
MAX_TOKENS = 30
DEVICE = 'cpu'
TOP_K = 20

# --------------------
# Utility functions
# --------------------
def parse_float16_array(s: str) -> np.ndarray:
    try:
        inner = s.strip().lstrip('[').rstrip(']')
        inner = inner.replace(',', ' ')
        nparray = np.fromstring(inner, dtype=np.float16, sep=' ')
        return nparray
    except Exception as e:
        print(f"Error parsing string: {s} - {e}")
        return np.zeros(384, dtype=np.float16)
    


def max_pool_and_normalize(embs: np.ndarray) -> np.ndarray:
    pooled = np.max(embs, axis=0).astype(np.float32)
    norm = np.linalg.norm(pooled)
    if norm > 0:
        pooled /= norm
    return pooled.astype(np.float16)


def cosine_similarity(a: np.ndarray, b: np.ndarray) -> float:
    return float(np.dot(a.astype(np.float32), b.astype(np.float32)))

@st.cache_data
def load_data():
    # Load aggregated embeddings
    agg_df = pd.read_csv(AGG_CSV)
    # Load per-skill embeddings
    skill_df = pd.read_csv(PER_SKILL_CSV)
    # Parse aggregated
    agg_embs = agg_df['SkillsEmbedding'].apply(parse_float16_array).tolist()
    emb_matrix = np.stack(agg_embs, axis=0).astype(np.float32)
    # Normalize for cosine
    norms = np.linalg.norm(emb_matrix, axis=1, keepdims=True)
    emb_matrix = emb_matrix / np.clip(norms, 1e-9, None)
    # Build FAISS index
    dim = emb_matrix.shape[1]
    index = faiss.IndexFlatIP(dim)
    index.add(emb_matrix)
    return agg_df, skill_df, agg_df['Identifier'].tolist(), index

@st.cache_resource
def load_model():
    return SentenceTransformer(MODEL_NAME, device=DEVICE)

# --------------------
# Main App
# --------------------
st.title("Skill-Based Identifier Finder")

# Initialize
agg_df, skill_df, identifiers, faiss_index = load_data()
model = load_model()

st.markdown(f"Enter up to 5 skills to find the top {TOP_K} closest Identifiers.")
with st.form('skills_form'):
    skills = [st.text_input(f"Skill {i}", key=f"skill_{i}") for i in range(1,6)]
    submitted = st.form_submit_button("Search")

if submitted:
    skills = [s.strip() for s in skills if s.strip()]
    if not skills:
        st.warning("Please enter at least one skill.")
    else:
        # 1) Embed input skills
        input_embs = model.encode(
            skills,
            show_progress_bar=False,
            batch_size=len(skills),
            max_length=MAX_TOKENS,
            truncation=True,
            convert_to_numpy=True
        ).astype(np.float16)
        # 2) Pool + normalize
        query_vec = max_pool_and_normalize(input_embs).astype(np.float32).reshape(1,-1)
        # 3) Search top K
        if query_vec.shape[1] != faiss_index.d:
            st.error(f"Dimension mismatch: query has {query_vec.shape[1]} but index expects {faiss_index.d}")
        else:
            distances, indices = faiss_index.search(query_vec, TOP_K)
            top_ids = [identifiers[i] for i in indices[0]]
            scores = distances[0].tolist()

            # Display results
            st.subheader("Top Matches")
            res_df = pd.DataFrame({'Identifier': top_ids, 'Score': scores})
            st.table(res_df)

            # 4) Per-skill similarity for each Identifier
            st.subheader("Per-Skill Similarities")
            for ident in top_ids:
                st.markdown(f"**Identifier: {ident}**")
                sub = skill_df[skill_df['Identifier'] == ident].copy()
                sub['emb_array'] = sub['embeddings'].apply(parse_float16_array)
                records = []
                for _, row in sub.iterrows():
                    sims = [cosine_similarity(row['emb_array'], emb) for emb in input_embs]
                    best_sim = max(sims)
                    records.append({'SkillName': row['SkillName'], 'Similarity': best_sim})
                df_sim = pd.DataFrame(records).sort_values('Similarity', ascending=False)
                st.table(df_sim)
