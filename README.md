# CIFAR Vision Objects — AI Engineering Project

Everything lives in **`cifar_vision_project.ipynb`**. Open it in JupyterLab or VS Code and run the cells from top to bottom.

## Folder layout

```
cifar_vision_project/
├── cifar_vision_project.ipynb   # THE notebook — runs the whole pipeline
├── README.md                    # this file
├── requirements.txt             # pinned Python packages
├── EVALUATION_MAPPING.md        # rubric criterion → file evidence
├── REPORT_TEMPLATE.md           # skeleton for the final written report
├── ETHICS_AND_FAIRNESS.md       # rubric §5.3, §5.4 deliverable
│
├── data/
│   ├── own/                     # your photographs, one folder per class
│   │   ├── 0_airplane/  1_automobile/  2_bird/  3_cat/  4_deer/
│   │   └── 5_dog/  6_frog/  7_horse/  8_ship/  9_truck/
│   └── (CIFAR-10 is downloaded automatically into ~/.keras/ on first run)
│
├── docs/                        # course PDFs (reference)
├── models/                      # trained .keras files (auto-created)
└── reports/
    ├── figures/                 # PNGs for the report (auto-created)
    └── tables/                  # CSVs for the report (auto-created)
```

## First run (3 commands)

```powershell
# 1. (Windows / PowerShell) create + activate a virtual environment
python -m venv .venv
.venv\Scripts\activate
# (alternative if you have the Python launcher installed: py -3.10 -m venv .venv)

# 2. install Python dependencies (also installs Jupyter so step 3 works)
pip install -r requirements.txt
pip install jupyterlab

# 3. open the notebook
jupyter lab cifar_vision_project.ipynb
```

If PowerShell refuses to activate the venv ("...cannot be loaded because running scripts is disabled..."), run this once:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

On Linux / macOS replace step 1 with `python3.10 -m venv .venv && source .venv/bin/activate`.

Inside the notebook click **Run ▸ Run All Cells** the first time. Total runtime: ~10 min on an A100 GPU, ~1–2 hours on CPU.

## What the notebook produces (rubric evidence)

* `models/exp1_baseline.keras`, `exp3_with_own.keras`, `exp5_transfer.keras`
* `reports/figures/eda_*.png`, `curves_*.png`, `confusion_matrix_*.png`, `misclassified_*.png`, `gradcam_*.png`
* `reports/tables/summary_all.csv`, `metrics_*.csv`, `hp_results.csv`, `config_*.json`, `history_*.csv`

See `EVALUATION_MAPPING.md` for the full rubric → file mapping and the submission checklist at the bottom of that file.
