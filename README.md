# Learning the Right Boundaries

This repository contains the code and supporting review artifacts for a
FinCausal 2026 question-answering project on answer-boundary behavior under
Direct Preference Optimization (DPO).

The experiment compares:

- **B1:** supervised fine-tuning of `Qwen/Qwen3-4B-Instruct-2507`.
- **C1:** DPO with matched answers from unrelated training questions.
- **M1:** DPO with screened model-generated boundary errors (223 incomplete,
  13 overextended).
- **M2:** a balanced hybrid DPO dataset (118 incomplete, 118 overextended)
  that retains 131 M1 negatives and replaces 105 incomplete negatives with
  constructed overextensions.

M1 and M2 differ in both error-type balance and negative construction.
Therefore, the experiment evaluates the two complete rejected-answer designs;
it does not isolate the causal effect of balance alone.

## Final test results

The test set contains 391 examples after removing cross-split overlaps.
Percentages are reported on a 0–100 scale.

| Model | Exact Match | Token F1 | SAS | Hybrid semantic acceptance | Too long | Too short |
|---|---:|---:|---:|---:|---:|---:|
| B1 | 82.86 | 93.26 | 92.12 | 91.82 | 34 | 25 |
| C1 | 82.86 | 93.37 | 92.39 | 91.05 | 30 | 31 |
| M1 | 79.28 | 92.19 | 91.48 | 90.79 | 63 | 9 |
| M2 | 83.89 | 94.44 | 92.99 | 93.35 | 35 | 22 |

The predeclared primary comparison, M2 versus B1, was not statistically
significant (Exact Match difference +1.02 percentage points; 95% bootstrap CI
[-1.53, 3.58]; McNemar p = 0.5413). M2 outperformed M1 with nominal,
unadjusted p = 0.0029. C1 provided no measurable improvement over B1 in exact
boundary selection.

## Repository contents

```text
notebooks/
  NLP_Final_Project_FinCausal_v11.ipynb
data/
  train_en_2000.csv
  splits/
human_reviews/
  m1_model_first_v6_screened_acceptance.csv
  c1_cross_example_candidate_audit_v7.csv
  m2_final_test_manual_review_packet_v1.csv
results/
  final_test_metrics.csv
  final_test_paired_comparisons.csv
scripts/
  validate_repository.py
```

The notebook contains the full data audit, split construction, supervised
fine-tuning, preference-data construction, DPO training, evaluation, and error
analysis. Model checkpoints are intentionally excluded because of their size.
Cached notebook outputs preserve the reported run.

## Validate the submitted files

From the repository root, run:

```bash
python scripts/validate_repository.py
```

This checks the dataset and split sizes, frozen M1 and C1 review hashes, the
completed 31-row M2 review, the seven-of-ten regression finding, notebook
structure, and common secret patterns.

## Reproduce in Google Colab

The notebook was designed for Google Colab with a T4 GPU and persistent Google
Drive storage.

1. Copy the repository's `data` and `human_reviews` folders into
   `/content/drive/MyDrive/FinCausal_Project/`.
2. Open `notebooks/NLP_Final_Project_FinCausal_v11.ipynb` in Colab.
3. Select a T4 GPU runtime.
4. Run the package-installation cell once. Restart the runtime if Colab asks,
   then resume at Section 1.2.
5. Add `OPENAI_API_KEY` to Colab Secrets only if the blinded semantic judging
   cells must be rerun. No key is stored in this repository.
6. Run the notebook in section order. The included frozen splits allow Section
   2.1 to run immediately without rebuilding them.

Recreating all model adapters and final predictions requires substantial GPU
time. The completed notebook outputs and the CSV result tables are included so
the reported findings can be inspected without rerunning training.

## Data

The included data are from the **FinCausal 2026 Dataset**, DOI
`10.21950/H7RKHH`. The dataset documentation states a
[CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) license.
See `data/DATA_LICENSE.md` and `data/FinCausal_2026_dataset_readme.txt`.

## Reproducibility notes

- Random seed: 42.
- The development set informed model and data-design decisions; the final test
  set remained frozen until M2 was selected.
- Confidence intervals resample individual questions and do not adjust for
  within-passage dependence.
- All models were trained with one seed.
- Non-primary p-values are nominal and unadjusted.
- The 105 constructed M2 overextensions received a structural audit rather
  than the sampled semantic validation used for M1.

