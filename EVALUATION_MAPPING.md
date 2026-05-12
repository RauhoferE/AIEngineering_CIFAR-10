# Evaluation Mapping — Rubric → Evidence

This file maps every criterion from `AIE_Projekt_Evaluierungstemplate.xlsx`
(45 sub-items, 45 total points) to the exact file or section where you can
find the evidence.

**Use this file before submission** as a checklist: can you point at a
concrete file for each row? If yes → you have evidence. If no → add it.

---

## Section 1 — Problem Definition & Conceptual Clarity (5 pts)

| # | Criterion | Evidence location |
|---|---|---|
| 1.1 | Business objective clearly defined, specific, non-trivial | `REPORT_TEMPLATE.md` §Introduction |
| 1.2 | Translated into clearly defined ML task | `REPORT_TEMPLATE.md` §Introduction (multi-class image classification, 10 classes) |
| 1.3 | Modeling approach conceptually appropriate and justified | `REPORT_TEMPLATE.md` §Model (CNN for images — justified with slide 20 of ML_Project.pdf) |
| 1.4 | Evaluation metrics appropriate and justified | `REPORT_TEMPLATE.md` §Evaluation (macro-F1 primary + accuracy + per-class) |
| 1.5 | Key assumptions, constraints, limitations acknowledged | `REPORT_TEMPLATE.md` §Conclusion + `ETHICS_AND_FAIRNESS.md` |

---

## Section 2 — Data Understanding & Preparation (7 pts)

| # | Criterion | Evidence location |
|---|---|---|
| 2.1 | Dataset selection justified and appropriate | `REPORT_TEMPLATE.md` §Dataset |
| 2.2 | Meaningful exploratory data analysis | `notebooks/01_data_exploration.ipynb` |
| 2.3 | Data quality issues and biases discussed | `REPORT_TEMPLATE.md` §Dataset + `ETHICS_AND_FAIRNESS.md` |
| 2.4 | Preprocessing steps described and reproducible | `model.py` (augmentation + rescaling layers) + `REPORT_TEMPLATE.md` §Preprocessing |
| 2.5 | Train/val/test split methodologically correct | `data_loader.py::load_cifar10` (45k/5k/10k split with fixed seed) |
| 2.6 | Dataset-specific challenges handled | `REPORT_TEMPLATE.md` §Dataset (small 32×32, domain shift to own photos) |
| 2.7 | Data preparation pipeline reproducible | `data_loader.py` + `config.SEED` + `requirements.txt` |

---

## Section 3 — Modeling & Experimental Design (8 pts)

| # | Criterion | Evidence location |
|---|---|---|
| 3.1 | Baseline model implemented and evaluated | `model.build_baseline_cnn` + `models/exp1_baseline.keras` + `reports/tables/summary_exp1_baseline.csv` |
| 3.2 | **Two substantively different approaches compared** | Baseline CNN vs MobileNetV2 transfer (`models/exp1_baseline.keras` vs `models/exp5_transfer.keras`) |
| 3.3 | Modeling choices justified by problem and data | `REPORT_TEMPLATE.md` §Model (why 3 conv blocks, why augmentation, why no vertical flip, etc.) |
| 3.4 | Hyperparameter tuning systematic and reproducible | `tune.py` + `reports/tables/hp_results.csv` + `reports/tables/hp_best.json` |
| 3.5 | Models compared under fair and consistent conditions | Same data splits, same callbacks, same augmentation (see `train.py` and `model.py`) |
| 3.6 | Experiments reproducible | Fixed `SEED`, pinned `requirements.txt`, JSON config saved per run |
| 3.7 | Experiments organized and systematically tracked | `reports/tables/config_*.json`, `history_*.csv`, `summary_*.csv` per run |
| 3.8 | Conclusions supported by experimental evidence | `REPORT_TEMPLATE.md` §Experiments (5-row comparison table with numbers) |

---

## Section 4 — Evaluation, Error Analysis & Robustness (8 pts)

| # | Criterion | Evidence location |
|---|---|---|
| 4.1 | Metrics appropriate for task | `evaluate.py::compute_metrics` (macro-F1, precision, recall, accuracy) |
| 4.2 | Performance reported completely and transparently | `reports/tables/summary_*.csv` + `metrics_*.csv` |
| 4.3 | Detailed breakdown beyond aggregate metrics | Per-class precision/recall/F1 in `metrics_<split>_<run>.csv` + confusion matrix PNGs |
| 4.4 | **Concrete mispredictions analyzed** | `reports/figures/misclassified_*.png` + `REPORT_TEMPLATE.md` §Results |
| 4.5 | Systematic weaknesses identified | `REPORT_TEMPLATE.md` §Results (which classes confuse the model) |
| 4.6 | **Robustness tested or discussed** | Own-images test (`summary_*.csv` row with split=own) shows domain shift |
| 4.7 | Overfitting assessed and discussed | `reports/figures/curves_*.png` (train-val gap) + `REPORT_TEMPLATE.md` |
| 4.8 | Conclusions aligned with evaluation results | `REPORT_TEMPLATE.md` §Conclusion |

---

## Section 5 — Explainability, Fairness & Ethical Reflection (5 pts)

| # | Criterion | Evidence location |
|---|---|---|
| 5.1 | **Explainability method applied** | Grad-CAM: `explain.py` + `reports/figures/gradcam_*.png` |
| 5.2 | Explainability results meaningfully interpreted | `REPORT_TEMPLATE.md` §Explainability (1 sentence per heatmap) |
| 5.3 | Fairness issues / biases considered | `ETHICS_AND_FAIRNESS.md` §Biases |
| 5.4 | Ethical implications and misuse scenarios | `ETHICS_AND_FAIRNESS.md` §Ethics |
| 5.5 | Limitations clearly communicated | `ETHICS_AND_FAIRNESS.md` §Limitations + `REPORT_TEMPLATE.md` §Conclusion |

---

## Section 6 — Technical Implementation & Reproducibility (5 pts)

| # | Criterion | Evidence location |
|---|---|---|
| 6.1 | Code well-structured, readable, modular | This repo: separate files for config, data, model, train, evaluate, explain, predict |
| 6.2 | Technical setup clearly documented | `SETUP.md` |
| 6.3 | Training settings fully documented | `config.py` + `reports/tables/config_*.json` per run |
| 6.4 | Logical and professional folder structure | See top-level tree in `README.md` |
| 6.5 | Professional engineering discipline | Pinned deps, seed fixed, memory growth enabled, mixed precision configured |

---

## Section 7 — Documentation & Scientific Reflection (4 pts)

| # | Criterion | Evidence location |
|---|---|---|
| 7.1 | ML pipeline coherently described end-to-end | `REPORT_TEMPLATE.md` (all sections) |
| 7.2 | Methodological decisions explicitly justified | `REPORT_TEMPLATE.md` §Model and §Preprocessing |
| 7.3 | Critical reflection on own work | `REPORT_TEMPLATE.md` §Conclusion §What did not work |
| 7.4 | Realistic future improvements proposed | `REPORT_TEMPLATE.md` §Future work |

---

## Section 8 — Presentation & Defense (3 pts)

| # | Criterion | Evidence location |
|---|---|---|
| 8.1 | Presentation clearly structured | Slides (one per report section) |
| 8.2 | Results presented clearly and interpreted | Slides include key figures from `reports/figures/` |
| 8.3 | Each team member can answer questions | Each member owns one section and knows the code behind it |

---

## Submission checklist (tick before handing in)

- [ ] All 10 class folders in `data/own/` have ≥ 5 photos each
- [ ] `models/` contains at least `exp1_baseline.keras`, `exp3_with_own.keras`, `exp5_transfer.keras`
- [ ] `reports/tables/summary_*.csv` exists for each experiment
- [ ] `reports/figures/confusion_matrix_cifar_*.png` exists for each experiment
- [ ] `reports/figures/confusion_matrix_own_*.png` exists for each experiment
- [ ] `reports/figures/curves_*.png` exists for each experiment (shows overfitting — item 4.7)
- [ ] `reports/figures/misclassified_*.png` exists (item 4.4)
- [ ] `reports/figures/gradcam_*.png` exists (item 5.1) — at least 3 correct + 3 wrong
- [ ] `reports/tables/hp_results.csv` exists (item 3.4)
- [ ] Report PDF covers every section of `REPORT_TEMPLATE.md`
- [ ] `ETHICS_AND_FAIRNESS.md` is filled in (not left as template)
- [ ] Code runs end-to-end on a fresh checkout: `bash run_all.sh`
- [ ] At least one team member has deployed on the AI server (screenshot of `predict.py` output)
