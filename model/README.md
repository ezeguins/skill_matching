---
tags:
- sentence-transformers
- sentence-similarity
- feature-extraction
- generated_from_trainer
- dataset_size:268494
- loss:CosineSimilarityLoss
base_model: sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2
widget:
- source_sentence: alta especializacion y manejo de sistemas de computo
  sentences:
  - high specialization and computer systems management
  - Monitoring des appels
  - knowledge in chronic diseases
- source_sentence: Arbeidssatisfactie
  sentences:
  - performance management
  - 'Programming: t  tJava, JavaScript, SQL'
  - Gardening services
- source_sentence: Content & Stroytelling
  sentences:
  - content & narrative
  - Dibujo, lectura y uso de diagramas
  - All Microsoft Programs (Word, Excel, etc.)
- source_sentence: If you need electrical work done give us a call for a great price
    (845) 232-5939
  sentences:
  - 'Native language: Greek'
  - cultura celular
  - Microsoft Office
- source_sentence: Certified CISCO CCNA-DataCenter
  sentences:
  - video sales letter editor
  - Fast Learner, Good talker, Can be Persuasive,
  - základní znalost v programu Microsoft Access
pipeline_tag: sentence-similarity
library_name: sentence-transformers
metrics:
- pearson_cosine
- spearman_cosine
model-index:
- name: SentenceTransformer based on sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2
  results:
  - task:
      type: semantic-similarity
      name: Semantic Similarity
    dataset:
      name: sts dev
      type: sts-dev
    metrics:
    - type: pearson_cosine
      value: 0.9146462708277019
      name: Pearson Cosine
    - type: spearman_cosine
      value: 0.8651786914924077
      name: Spearman Cosine
  - task:
      type: semantic-similarity
      name: Semantic Similarity
    dataset:
      name: sts test
      type: sts-test
    metrics:
    - type: pearson_cosine
      value: 0.9148048974332805
      name: Pearson Cosine
    - type: spearman_cosine
      value: 0.8655004266760449
      name: Spearman Cosine
---

# SentenceTransformer based on sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2

This is a [sentence-transformers](https://www.SBERT.net) model finetuned from [sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2](https://huggingface.co/sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2). It maps sentences & paragraphs to a 384-dimensional dense vector space and can be used for semantic textual similarity, semantic search, paraphrase mining, text classification, clustering, and more.

## Model Details

### Model Description
- **Model Type:** Sentence Transformer
- **Base model:** [sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2](https://huggingface.co/sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2) <!-- at revision 86741b4e3f5cb7765a600d3a3d55a0f6a6cb443d -->
- **Maximum Sequence Length:** 30 tokens
- **Output Dimensionality:** 384 dimensions
- **Similarity Function:** Cosine Similarity
<!-- - **Training Dataset:** Unknown -->
<!-- - **Language:** Unknown -->
<!-- - **License:** Unknown -->

### Model Sources

- **Documentation:** [Sentence Transformers Documentation](https://sbert.net)
- **Repository:** [Sentence Transformers on GitHub](https://github.com/UKPLab/sentence-transformers)
- **Hugging Face:** [Sentence Transformers on Hugging Face](https://huggingface.co/models?library=sentence-transformers)

### Full Model Architecture

```
SentenceTransformer(
  (0): Transformer({'max_seq_length': 30, 'do_lower_case': False}) with Transformer model: BertModel 
  (1): Pooling({'word_embedding_dimension': 384, 'pooling_mode_cls_token': False, 'pooling_mode_mean_tokens': True, 'pooling_mode_max_tokens': False, 'pooling_mode_mean_sqrt_len_tokens': False, 'pooling_mode_weightedmean_tokens': False, 'pooling_mode_lasttoken': False, 'include_prompt': True})
)
```

## Usage

### Direct Usage (Sentence Transformers)

First install the Sentence Transformers library:

```bash
pip install -U sentence-transformers
```

Then you can load this model and run inference.
```python
from sentence_transformers import SentenceTransformer

# Download from the 🤗 Hub
model = SentenceTransformer("sentence_transformers_model_id")
# Run inference
sentences = [
    'Certified CISCO CCNA-DataCenter',
    'Fast Learner, Good talker, Can be Persuasive,',
    'základní znalost v programu Microsoft Access',
]
embeddings = model.encode(sentences)
print(embeddings.shape)
# [3, 384]

# Get the similarity scores for the embeddings
similarities = model.similarity(embeddings, embeddings)
print(similarities.shape)
# [3, 3]
```

<!--
### Direct Usage (Transformers)

<details><summary>Click to see the direct usage in Transformers</summary>

</details>
-->

<!--
### Downstream Usage (Sentence Transformers)

You can finetune this model on your own dataset.

<details><summary>Click to expand</summary>

</details>
-->

<!--
### Out-of-Scope Use

*List how the model may foreseeably be misused and address what users ought not to do with the model.*
-->

## Evaluation

### Metrics

#### Semantic Similarity

* Datasets: `sts-dev` and `sts-test`
* Evaluated with [<code>EmbeddingSimilarityEvaluator</code>](https://sbert.net/docs/package_reference/sentence_transformer/evaluation.html#sentence_transformers.evaluation.EmbeddingSimilarityEvaluator)

| Metric              | sts-dev    | sts-test   |
|:--------------------|:-----------|:-----------|
| pearson_cosine      | 0.9146     | 0.9148     |
| **spearman_cosine** | **0.8652** | **0.8655** |

<!--
## Bias, Risks and Limitations

*What are the known or foreseeable issues stemming from this model? You could also flag here known failure cases or weaknesses of the model.*
-->

<!--
### Recommendations

*What are recommendations with respect to the foreseeable issues? For example, filtering explicit content.*
-->

## Training Details

### Training Dataset

#### Unnamed Dataset

* Size: 268,494 training samples
* Columns: <code>sentence1</code>, <code>sentence2</code>, and <code>score</code>
* Approximate statistics based on the first 1000 samples:
  |         | sentence1                                                                        | sentence2                                                                        | score                                                           |
  |:--------|:---------------------------------------------------------------------------------|:---------------------------------------------------------------------------------|:----------------------------------------------------------------|
  | type    | string                                                                           | string                                                                           | float                                                           |
  | details | <ul><li>min: 4 tokens</li><li>mean: 10.0 tokens</li><li>max: 30 tokens</li></ul> | <ul><li>min: 3 tokens</li><li>mean: 9.16 tokens</li><li>max: 30 tokens</li></ul> | <ul><li>min: 0.0</li><li>mean: 0.56</li><li>max: 0.98</li></ul> |
* Samples:
  | sentence1                                              | sentence2                                                   | score             |
  |:-------------------------------------------------------|:------------------------------------------------------------|:------------------|
  | <code>CPT Rig Supervision</code>                       | <code>current procedural terminology rig supervision</code> | <code>0.98</code> |
  | <code>Front office admin and reception</code>          | <code>Oracle Vault and Wallet</code>                        | <code>0.09</code> |
  | <code>Site supervision for system commissioning</code> | <code>social-media translating</code>                       | <code>0.29</code> |
* Loss: [<code>CosineSimilarityLoss</code>](https://sbert.net/docs/package_reference/sentence_transformer/losses.html#cosinesimilarityloss) with these parameters:
  ```json
  {
      "loss_fct": "torch.nn.modules.loss.MSELoss"
  }
  ```

### Evaluation Dataset

#### Unnamed Dataset

* Size: 33,561 evaluation samples
* Columns: <code>sentence1</code>, <code>sentence2</code>, and <code>score</code>
* Approximate statistics based on the first 1000 samples:
  |         | sentence1                                                                        | sentence2                                                                        | score                                                           |
  |:--------|:---------------------------------------------------------------------------------|:---------------------------------------------------------------------------------|:----------------------------------------------------------------|
  | type    | string                                                                           | string                                                                           | float                                                           |
  | details | <ul><li>min: 4 tokens</li><li>mean: 10.3 tokens</li><li>max: 30 tokens</li></ul> | <ul><li>min: 3 tokens</li><li>mean: 9.21 tokens</li><li>max: 30 tokens</li></ul> | <ul><li>min: 0.0</li><li>mean: 0.53</li><li>max: 0.98</li></ul> |
* Samples:
  | sentence1                                               | sentence2                                          | score            |
  |:--------------------------------------------------------|:---------------------------------------------------|:-----------------|
  | <code>Exercendo a Liderança e Liderança Dinâmica</code> | <code>Konsultan Kemasan/Box</code>                 | <code>0.1</code> |
  | <code>Customer Incident Resolutions</code>              | <code>IT CORDINATION & INTEGRATION  SYSTEMS</code> | <code>0.6</code> |
  | <code>Debitorenmanagement für KMU</code>                | <code>Radio planning network</code>                | <code>0.1</code> |
* Loss: [<code>CosineSimilarityLoss</code>](https://sbert.net/docs/package_reference/sentence_transformer/losses.html#cosinesimilarityloss) with these parameters:
  ```json
  {
      "loss_fct": "torch.nn.modules.loss.MSELoss"
  }
  ```

### Training Hyperparameters
#### Non-Default Hyperparameters

- `eval_strategy`: epoch
- `per_device_train_batch_size`: 32
- `per_device_eval_batch_size`: 32
- `learning_rate`: 1e-05
- `num_train_epochs`: 4
- `warmup_ratio`: 0.1
- `fp16`: True

#### All Hyperparameters
<details><summary>Click to expand</summary>

- `overwrite_output_dir`: False
- `do_predict`: False
- `eval_strategy`: epoch
- `prediction_loss_only`: True
- `per_device_train_batch_size`: 32
- `per_device_eval_batch_size`: 32
- `per_gpu_train_batch_size`: None
- `per_gpu_eval_batch_size`: None
- `gradient_accumulation_steps`: 1
- `eval_accumulation_steps`: None
- `torch_empty_cache_steps`: None
- `learning_rate`: 1e-05
- `weight_decay`: 0.0
- `adam_beta1`: 0.9
- `adam_beta2`: 0.999
- `adam_epsilon`: 1e-08
- `max_grad_norm`: 1.0
- `num_train_epochs`: 4
- `max_steps`: -1
- `lr_scheduler_type`: linear
- `lr_scheduler_kwargs`: {}
- `warmup_ratio`: 0.1
- `warmup_steps`: 0
- `log_level`: passive
- `log_level_replica`: warning
- `log_on_each_node`: True
- `logging_nan_inf_filter`: True
- `save_safetensors`: True
- `save_on_each_node`: False
- `save_only_model`: False
- `restore_callback_states_from_checkpoint`: False
- `no_cuda`: False
- `use_cpu`: False
- `use_mps_device`: False
- `seed`: 42
- `data_seed`: None
- `jit_mode_eval`: False
- `use_ipex`: False
- `bf16`: False
- `fp16`: True
- `fp16_opt_level`: O1
- `half_precision_backend`: auto
- `bf16_full_eval`: False
- `fp16_full_eval`: False
- `tf32`: None
- `local_rank`: 0
- `ddp_backend`: None
- `tpu_num_cores`: None
- `tpu_metrics_debug`: False
- `debug`: []
- `dataloader_drop_last`: False
- `dataloader_num_workers`: 0
- `dataloader_prefetch_factor`: None
- `past_index`: -1
- `disable_tqdm`: False
- `remove_unused_columns`: True
- `label_names`: None
- `load_best_model_at_end`: False
- `ignore_data_skip`: False
- `fsdp`: []
- `fsdp_min_num_params`: 0
- `fsdp_config`: {'min_num_params': 0, 'xla': False, 'xla_fsdp_v2': False, 'xla_fsdp_grad_ckpt': False}
- `tp_size`: 0
- `fsdp_transformer_layer_cls_to_wrap`: None
- `accelerator_config`: {'split_batches': False, 'dispatch_batches': None, 'even_batches': True, 'use_seedable_sampler': True, 'non_blocking': False, 'gradient_accumulation_kwargs': None}
- `deepspeed`: None
- `label_smoothing_factor`: 0.0
- `optim`: adamw_torch
- `optim_args`: None
- `adafactor`: False
- `group_by_length`: False
- `length_column_name`: length
- `ddp_find_unused_parameters`: None
- `ddp_bucket_cap_mb`: None
- `ddp_broadcast_buffers`: False
- `dataloader_pin_memory`: True
- `dataloader_persistent_workers`: False
- `skip_memory_metrics`: True
- `use_legacy_prediction_loop`: False
- `push_to_hub`: False
- `resume_from_checkpoint`: None
- `hub_model_id`: None
- `hub_strategy`: every_save
- `hub_private_repo`: None
- `hub_always_push`: False
- `gradient_checkpointing`: False
- `gradient_checkpointing_kwargs`: None
- `include_inputs_for_metrics`: False
- `include_for_metrics`: []
- `eval_do_concat_batches`: True
- `fp16_backend`: auto
- `push_to_hub_model_id`: None
- `push_to_hub_organization`: None
- `mp_parameters`: 
- `auto_find_batch_size`: False
- `full_determinism`: False
- `torchdynamo`: None
- `ray_scope`: last
- `ddp_timeout`: 1800
- `torch_compile`: False
- `torch_compile_backend`: None
- `torch_compile_mode`: None
- `include_tokens_per_second`: False
- `include_num_input_tokens_seen`: False
- `neftune_noise_alpha`: None
- `optim_target_modules`: None
- `batch_eval_metrics`: False
- `eval_on_start`: False
- `use_liger_kernel`: False
- `eval_use_gather_object`: False
- `average_tokens_across_devices`: False
- `prompts`: None
- `batch_sampler`: batch_sampler
- `multi_dataset_batch_sampler`: proportional

</details>

### Training Logs
| Epoch  | Step  | Training Loss | Validation Loss | sts-dev_spearman_cosine | sts-test_spearman_cosine |
|:------:|:-----:|:-------------:|:---------------:|:-----------------------:|:------------------------:|
| 0.1192 | 500   | 0.0506        | -               | -                       | -                        |
| 0.2383 | 1000  | 0.0399        | -               | -                       | -                        |
| 0.3575 | 1500  | 0.0357        | -               | -                       | -                        |
| 0.4766 | 2000  | 0.0335        | -               | -                       | -                        |
| 0.5958 | 2500  | 0.0326        | -               | -                       | -                        |
| 0.7150 | 3000  | 0.0314        | -               | -                       | -                        |
| 0.8341 | 3500  | 0.0304        | -               | -                       | -                        |
| 0.9533 | 4000  | 0.0297        | -               | -                       | -                        |
| 1.0    | 4196  | -             | 0.0272          | 0.8592                  | -                        |
| 1.0724 | 4500  | 0.0274        | -               | -                       | -                        |
| 1.1916 | 5000  | 0.0263        | -               | -                       | -                        |
| 1.3108 | 5500  | 0.0261        | -               | -                       | -                        |
| 1.4299 | 6000  | 0.0258        | -               | -                       | -                        |
| 1.5491 | 6500  | 0.0255        | -               | -                       | -                        |
| 1.6683 | 7000  | 0.025         | -               | -                       | -                        |
| 1.7874 | 7500  | 0.0249        | -               | -                       | -                        |
| 1.9066 | 8000  | 0.025         | -               | -                       | -                        |
| 2.0    | 8392  | -             | 0.0252          | 0.8635                  | -                        |
| 2.0257 | 8500  | 0.0249        | -               | -                       | -                        |
| 2.1449 | 9000  | 0.0221        | -               | -                       | -                        |
| 2.2641 | 9500  | 0.0223        | -               | -                       | -                        |
| 2.3832 | 10000 | 0.0227        | -               | -                       | -                        |
| 2.5024 | 10500 | 0.022         | -               | -                       | -                        |
| 2.6215 | 11000 | 0.0222        | -               | -                       | -                        |
| 2.7407 | 11500 | 0.0219        | -               | -                       | -                        |
| 2.8599 | 12000 | 0.022         | -               | -                       | -                        |
| 2.9790 | 12500 | 0.022         | -               | -                       | -                        |
| 3.0    | 12588 | -             | 0.0248          | 0.8648                  | -                        |
| 3.0982 | 13000 | 0.0205        | -               | -                       | -                        |
| 3.2173 | 13500 | 0.0201        | -               | -                       | -                        |
| 3.3365 | 14000 | 0.0205        | -               | -                       | -                        |
| 3.4557 | 14500 | 0.0202        | -               | -                       | -                        |
| 3.5748 | 15000 | 0.0203        | -               | -                       | -                        |
| 3.6940 | 15500 | 0.0203        | -               | -                       | -                        |
| 3.8132 | 16000 | 0.0203        | -               | -                       | -                        |
| 3.9323 | 16500 | 0.02          | -               | -                       | -                        |
| 4.0    | 16784 | -             | 0.0245          | 0.8652                  | -                        |
| -1     | -1    | -             | -               | -                       | 0.8655                   |


### Framework Versions
- Python: 3.11.11
- Sentence Transformers: 4.1.0
- Transformers: 4.51.1
- PyTorch: 2.5.1+cu124
- Accelerate: 1.3.0
- Datasets: 3.5.0
- Tokenizers: 0.21.0

## Citation

### BibTeX

#### Sentence Transformers
```bibtex
@inproceedings{reimers-2019-sentence-bert,
    title = "Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks",
    author = "Reimers, Nils and Gurevych, Iryna",
    booktitle = "Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing",
    month = "11",
    year = "2019",
    publisher = "Association for Computational Linguistics",
    url = "https://arxiv.org/abs/1908.10084",
}
```

<!--
## Glossary

*Clearly define terms in order to be accessible across audiences.*
-->

<!--
## Model Card Authors

*Lists the people who create the model card, providing recognition and accountability for the detailed work that goes into its construction.*
-->

<!--
## Model Card Contact

*Provides a way for people who have updates to the Model Card, suggestions, or questions, to contact the Model Card authors.*
-->