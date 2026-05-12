# Final Report — CIFAR Vision Objects

> Copy this file into a new `.docx` or Google Doc and fill in the `[...]`
> placeholders. Every section maps to at least one rubric criterion — see
> `EVALUATION_MAPPING.md`.

**Team:** [Names]
**Group:** CIFAR Vision Objects
**Date:** [YYYY-MM-DD]

---

## 1. Introduction (rubric items 1.1, 1.2, 1.5, 7.1)

### Business problem
We want to automatically classify photographs of everyday objects into one
of 10 categories: airplane, automobile, bird, cat, deer, dog, frog, horse,
ship, truck.

Why it matters: image classification is a foundational computer-vision task
used in wildlife monitoring, autonomous driving, content moderation, and
accessibility tools (describing images to visually impaired users).

### Machine learning task
This is **multi-class image classification** with 10 mutually exclusive
classes. Input: a 32×32 RGB image. Output: one class label (integer 0–9).

### Success criteria
- **Primary metric** (optimizing): macro-F1 on CIFAR-10 test set ≥ 0.75.
- **Secondary**: accuracy on CIFAR-10 test set ≥ 0.78.
- **Robustness metric**: accuracy on own images ≥ 0.40 (domain shift to
  high-resolution real-world photos is severe; any number above random
  chance of 0.10 is informative).

### Assumptions
- [1] 32×32 resolution is sufficient for our 10 broad object categories.
- [2] CIFAR-10 class distribution is representative of the objects we care about.
- [3] Our hand-collected test images are labeled correctly.

---

## 2. Dataset (rubric items 2.1, 2.2, 2.3, 2.6)

### External dataset: CIFAR-10
- **Source:** https://www.cs.toronto.edu/~kriz/cifar.html (Krizhevsky 2009).
- **Size:** 60,000 images (50,000 training + 10,000 test), 32×32 RGB.
- **Classes:** 10, balanced (6,000 images per class).
- **Why it fits:** matches the task name exactly; standard benchmark; loads
  through `tf.keras.datasets.cifar10.load_data()` with no setup friction.

### Own images
We photographed **[N]** objects across **[M]** classes with our phones.

| Class | Count | Notes |
|---|---|---|
| airplane   | [n] | [e.g. Vienna airport] |
| automobile | [n] | [street photos + parked cars] |
| bird       | [n] | [park pigeons + pet canary] |
| cat        | [n] | [own pet + friend's] |
| deer       | [n] | [zoo / figurine — justify] |
| dog        | [n] | [dog park] |
| frog       | [n] | [aquarium / figurine] |
| horse      | [n] | [stable / riding school] |
| ship       | [n] | [Danube] |
| truck      | [n] | [construction sites] |

Insert screenshot of sample grid from `notebooks/01_data_exploration.ipynb`.

### Differences between CIFAR-10 and our photos
| Property | CIFAR-10 | Our photos (before 32×32 resize) |
|---|---|---|
| Resolution | 32×32 native | 3000+ pixels on long side |
| Background | usually clean, centered | cluttered, uncontrolled |
| Lighting | normalized | varies (shadow, flash, overcast) |
| Angle | canonical | varies (top-down, side, tilted) |

This difference is a **domain shift** — models trained on CIFAR may
struggle on our photos. Experiment 3 measures that explicitly.

### Data quality issues (rubric 2.3)
- We could not photograph a real deer, so those images are [zoo / figurine].
  We mark this as a limitation.
- Some of our photos contain multiple candidate classes (e.g. a cat on a
  truck). We chose the most prominent object for the label.
- Class balance in our own set is [balanced / imbalanced, explain].

---

## 3. Preprocessing (rubric items 2.4, 2.7)

Applied to every image:

1. **Resize** to 32×32 RGB (matches CIFAR native resolution).
2. **Rescale** pixel values from 0..255 to 0..1 (inside the model via
   `Rescaling(1/255.)` layer — see `model.py`).
3. **Augmentation** during training only (the layers do nothing at evaluation):
   - `RandomFlip("horizontal")` — many classes look the same flipped.
   - `RandomRotation(0.08)` — ±30° rotation tolerates tilted phone shots.
   - `RandomZoom(0.10)` — tolerates different framing.
   - `RandomTranslation(0.10, 0.10)` — tolerates off-center framing.
4. **No vertical flip** — an upside-down airplane is a wrong training signal.

### Splits
| Split | Size | Source |
|---|---|---|
| Train | 45,000 CIFAR + [0 or 60% of own] | CIFAR-10 training set |
| Validation | 5,000 | CIFAR-10 training set (held out) |
| Test (CIFAR) | 10,000 | CIFAR-10 test set (never touched during training) |
| Test (Own) | [N] | Our photos (either all, or 40% if own images added to training) |

All splits are deterministic: `np.random.default_rng(SEED=42)` shuffle
before the val slice.

---

## 4. Model (rubric items 1.3, 3.1, 3.3)

We compare two substantively different approaches (rubric 3.2):

### Model A: Baseline CNN (trained from scratch)
3 convolutional blocks + a small classifier head; ~158,000 parameters.

```
Input(32,32,3) → Augment → Rescale(/255)
→ Conv(32) → BN → Conv(32) → BN → MaxPool → Dropout(0.25)
→ Conv(64) → BN → Conv(64) → BN → MaxPool → Dropout(0.25)
→ Conv(128) → BN → GlobalAveragePooling
→ Dense(128) → Dropout(0.5) → Dense(10, softmax)
```

**Justification:** Matches ML_Project.pdf slide 20 ("Image Recognition,
Computer Vision → CNN"). Small 3×3 convolutions + BatchNorm + Dropout is
the classic well-understood pattern for CIFAR-sized images.

### Model B: MobileNetV2 transfer learning
ImageNet-pretrained MobileNetV2 with a small new classifier head. Input
is resized from 32×32 to 96×96 (MobileNetV2's minimum input). Backbone
is frozen — only the 10-way head is trained.

**Justification:** ML_Project.pdf slide 21 recommends transfer learning
"if possible". Small new task + small dataset + backbone trained on a
similar domain (ImageNet has many of our classes) fits quadrant 4 of
slide 22 ("freeze the convolutional base").

### Training configuration
| Setting | Value |
|---|---|
| Optimizer | Adam |
| Loss | sparse_categorical_crossentropy |
| Initial learning rate | 1e-3 |
| Batch size | 64 |
| Max epochs | 50 |
| Early stopping | patience=8 on val_accuracy, restore_best_weights |
| LR schedule | ReduceLROnPlateau, factor 0.5, patience 4 |
| Precision | mixed_float16 on GPU (server guide slide 19) |

---

## 5. Training (rubric item 4.7)

Insert `reports/figures/curves_exp1_baseline.png` and
`reports/figures/curves_exp5_transfer.png` side by side.

Describe for each:
- How many epochs until EarlyStopping fired.
- Gap between training and validation accuracy (bigger gap = more overfitting).
- Whether LR was reduced by ReduceLROnPlateau.

---

## 6. Experiments (rubric items 3.7, 3.8)

All experiments use the same splits and same validation set (rubric 3.5).
Fill this table from `reports/tables/summary_*.csv`:

| # | Experiment | CIFAR test acc | CIFAR test F1 | Own test acc | Notes |
|---|---|---|---|---|---|
| 1 | Baseline CNN | [x.xx] | [x.xx] | [x.xx] | starting point |
| 2 | + Augmentation | [x.xx] | [x.xx] | [x.xx] | reduced train-val gap from [a] to [b] |
| 3 | + Own images in training | [x.xx] | [x.xx] | [x.xx] | own-test improved from [a] to [b] |
| 4 | + Hyperparameter tuning | [x.xx] | [x.xx] | [x.xx] | best: lr=[x], dropout=[y] |
| 5 | Transfer learning | [x.xx] | [x.xx] | [x.xx] | [higher on CIFAR / lower on own?] |

### Hyperparameter tuning (rubric 3.4)
Paste `reports/tables/hp_results.csv` as a table.

One paragraph interpreting the biggest effect (usually learning rate).

### Why we chose the final model
[Our final submitted model is `models/<run>.keras`. We chose it because
it has the best F1 on CIFAR test while still performing decently on own
images. The alternative (transfer learning) was / was not better because …]

---

## 7. Results & Error Analysis (rubric items 4.2, 4.3, 4.4, 4.5)

### Overall metrics (final model)
| Metric | CIFAR test | Own test |
|---|---|---|
| Accuracy | [x.xx] | [x.xx] |
| Macro precision | [x.xx] | [x.xx] |
| Macro recall | [x.xx] | [x.xx] |
| Macro F1 | [x.xx] | [x.xx] |

### Per-class F1 (from `metrics_cifar_<run>.csv`)
[paste table]

### Confusion matrices
Insert `reports/figures/confusion_matrix_cifar_<run>.png`
Insert `reports/figures/confusion_matrix_own_<run>.png`

Observations:
- Easiest classes: [list].
- Hardest classes: [list] (often cat↔dog and bird↔airplane confusions on CIFAR).
- Domain shift: same model drops [X]% accuracy from CIFAR-test to own-test.

### Misclassification analysis (rubric 4.4)
Insert `reports/figures/misclassified_<run>.png`.

For each of the worst mistakes, write one sentence explaining why:
- Image 1: [e.g. "Predicted 'deer' instead of 'horse' — the image is dark and the animal is side-on, making the antler pattern ambiguous."]
- Image 2: …
- …

---

## 8. Explainability (rubric items 5.1, 5.2)

We used **Grad-CAM** on the final model's last convolutional layer.

Insert 3 correct examples and 3 misclassified examples from
`reports/figures/gradcam_<run>_*.png`.

For each image, one sentence describing where the heatmap "looked":
- Correct 1: [e.g. "The model focused on the wings and body of the plane."]
- Correct 2: …
- Wrong 1: [e.g. "The model highlighted the blue sky instead of the bird itself, explaining the 'airplane' misprediction."]
- Wrong 2: …

This tells us the model has learned to rely on [object shapes / background context / specific textures], which is [good / a weakness we should fix].

---

## 9. Deployment (rubric item 6.2)

- Server: university AI server (A100 GPU).
- Access: SSH on port 24 with key-based authentication.
- Runtime: Python 3.10 virtualenv with pinned `requirements.txt`.
- Inference: command-line via `predict.py --image <path> --run-name <run>`.
- Example output: [insert screenshot of terminal].

Full procedure in `DEPLOYMENT.md`.

---

## 10. Ethics & Fairness (rubric items 5.3, 5.4, 5.5)

See `ETHICS_AND_FAIRNESS.md` (include a condensed version here — 1 page max).

---

## 11. Conclusion (rubric items 1.5, 7.3)

### What worked
- [e.g. "Data augmentation reduced overfitting by X%."]
- [e.g. "Transfer learning improved CIFAR test accuracy by Y%."]

### What did not work
- [e.g. "Learning rate 1e-4 was too small — model underfit after 50 epochs."]
- [e.g. "Transfer learning performed worse on own images because MobileNetV2 expects ImageNet-style photos."]

### Limitations (rubric 5.5)
- Images are 32×32 — enough for 10 broad classes, not for fine-grained classification (e.g., dog breeds).
- Only 10 classes — a real system would need hundreds or thousands.
- Our own dataset is small (N photos). Any own-test metric has ±[X]% noise.
- Single evaluation metric (macro-F1) cannot capture all failure modes.

### Future work (rubric 7.4)
- Try a stronger backbone (EfficientNet, ResNet-50) with full fine-tuning.
- Collect 10× more own images to make own-test statistically tight.
- Add test-time augmentation to improve robustness on own photos.
- Explore class-balanced loss weighting if own images are imbalanced.

---

## 12. References

- Géron, A. *Hands-on Machine Learning with Scikit-Learn, Keras, and TensorFlow*, 2022.
- Krizhevsky, A. *Learning Multiple Layers of Features from Tiny Images*, 2009 (CIFAR-10).
- Sandler et al. *MobileNetV2: Inverted Residuals and Linear Bottlenecks*, CVPR 2018.
- Selvaraju et al. *Grad-CAM: Visual Explanations from Deep Networks*, ICCV 2017.
- Course PDFs: `03_ML_Project.pdf`, `2026_AI_Engineering-Project.pdf`,
  `2026_AI_Engineering_Working-on-AI-Server.pdf`.
