# AIEngineering_CIFAR-10

This repository contains the implemented CIFAR-10 image-classification
pipeline in `cifar_resnet50_project.ipynb` and the documentation assets used
to turn its outputs into the final AI Engineering submission.


## Prerequisites

- Python 3.10 or newer
- PowerShell on Windows, or an equivalent shell on Linux/macOS
- Enough disk space for TensorFlow, notebook outputs, and downloaded CIFAR-10
  data
- Optional but recommended: an NVIDIA GPU; CPU execution also works with
  longer runtimes

## Setup

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

If PowerShell blocks activation, run this once and retry:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

## First Run

1. Open `cifar_resnet50_project.ipynb` in VS Code or JupyterLab.
2. Run all notebook cells from top to bottom.
3. Verify that the notebook produces updated artifacts under `reports/` and,
   when training is enabled, saved model checkpoints under `models/`.

## Folder Layout

### Current repository folders

- `docs/` - course PDFs and the grading rubric
- `project-documentation/` - Speckit specification, plan, tasks, and evidence
  contract
- `reports/` - generated figures and tables already available for the report

### Runtime and submission folders

- `data/own/` - own photographs used for robustness testing; organize them by
  class before running the full notebook workflow
- `models/` - generated `.keras` checkpoints for `exp1_baseline`,
  `exp3_with_own`, and `exp5_transfer`

## Expected Outputs

The notebook and documentation workflow should leave you with:

- trained models for the three experiments
- evaluation tables in `reports/tables/`
- EDA, confusion-matrix, learning-curve, misclassification, and Grad-CAM
  figures in `reports/figures/`
- a completed report, ethics reflection, evidence map, and slide deck
