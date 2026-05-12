# Ethics, Fairness & Limitations

Rubric items 5.3, 5.4, 5.5 together are worth ~3 points. They are cheap
points **if you write anything thoughtful** and easy to lose if you leave
the section empty. The template below is a starting point — edit it to
match your actual findings, do not paste it unchanged.

---

## Biases in the data (rubric 5.3)

### Biases we know are in CIFAR-10
- **Iconic-view bias.** CIFAR-10 images mostly show objects from a
  canonical angle: cars side-on, planes in the sky, cats facing the
  camera. A model trained only on CIFAR-10 will struggle with objects
  seen from unusual angles (top-down plane, back of a cat).
- **Class co-occurrence bias.** Birds often appear with sky, ships with
  water, frogs with green backgrounds. The model can learn to rely on
  the background instead of the object. Our Grad-CAM results
  [confirm / do not confirm] this.
- **Western-centric object choice.** The 10 CIFAR classes reflect
  objects common in North American daily life (automobile, dog, truck).
  A system trained on CIFAR-10 alone would be a poor fit for contexts
  where different objects matter (e.g., water buffalo instead of deer).

### Biases in our own images
- We collected photos in **[Vienna / your city]**, so our photos show
  **[European-style cars, central-European bird species]** which may
  differ from the CIFAR distribution.
- Our photos were taken on **[list phone models]**, which have different
  lenses, color calibration, and autofocus behaviour.
- Class coverage in our own set is uneven — we have more **[e.g. cat]**
  photos than **[e.g. deer]** because access was easier.

### Mitigations we applied
- Data augmentation (flip, rotation, zoom) makes the model more robust
  to non-canonical views.
- Evaluating on two test sets (CIFAR-test vs own-test) makes the
  performance gap visible in the report — we do not hide it.
- We include per-class metrics in `metrics_*.csv` so readers can see
  where the model is weakest.

---

## Ethical considerations (rubric 5.4)

### Potential misuse scenarios
1. **Surveillance.** A generic object classifier is a small building
   block of a surveillance pipeline. Ours is trained only on 10 generic
   classes, but the architecture could be retrained on people, faces,
   or license plates. We do not release the training code for
   person/face detection and explicitly scope this project to objects.
2. **Over-trusted decisions.** If someone deployed this model for
   safety-critical decisions (e.g., autonomous driving), a ~80% accuracy
   model would cause serious harm. Our model is a coursework artifact
   and should not be used in production without much more rigorous
   evaluation and orders of magnitude more training data.
3. **Data scraping concerns.** CIFAR-10 was collected from photos on
   the internet (scraped via Google Image Search in 2009). We inherit
   any consent questions those photos carry. For our own photos we
   took every picture ourselves and did not capture identifiable
   people, license plates, or private property.

### Dual-use reflection
Image classification has many beneficial uses (wildlife conservation,
accessibility tools, automated medical imaging) and many harmful uses
(mass surveillance, autonomous weapons). The **model itself** is
dual-use — what changes the ethical picture is how it is deployed, by
whom, and with what data. As responsible engineers we should refuse to
build classifiers for populations or contexts where the harms
outweigh the benefits.

### Privacy of our own images
- We stripped EXIF metadata (including GPS coordinates) from every
  uploaded photograph before putting it in `data/own/`. Command:
  `exiftool -all= data/own/*/*.jpg`.
- No photographs contain identifiable human faces.
- Photographs of private property were taken from public streets.

---

## Limitations (rubric 5.5)

### Technical limitations
- **32×32 resolution** is extremely low. The model cannot distinguish
  fine details — a Persian cat looks indistinguishable from a ragdoll
  at this size, and often from a small dog. This is fine for our task
  (10 broad classes) but would not transfer to fine-grained classification.
- **10 fixed classes.** The model assigns every input to one of the 10
  classes with no "unknown" option. If you show it a picture of a
  bicycle, it will confidently predict something wrong.
- **Small own-image test set.** With [N=~50] own images, each individual
  prediction moves the accuracy by ±2 %. Differences smaller than that
  are not statistically meaningful.
- **Single evaluation metric.** We report macro-F1, but the right
  metric depends on deployment. For a deployment that penalizes false
  positives (e.g., refusing to classify a non-animal as an animal),
  a different metric would matter more.

### Explainability limitations
- Grad-CAM shows which **spatial region** the model looked at, but not
  which **features** (edges? colors? textures?) within that region.
- Grad-CAM can disagree with the model's actual decision process for
  deep networks. Other methods (LIME, SHAP, Integrated Gradients) give
  different explanations.

### Fairness limitations
- We did not evaluate performance by **image source** (e.g., Canon
  camera vs iPhone photos), so the model's fairness across capture
  devices is unknown.
- We did not evaluate performance on images from other cultures,
  weather conditions, or visual styles. Generalization outside our
  collection conditions is unquantified.

### What we would do differently with more time
- Collect a larger own-image test set (300+ images) stratified across
  angles, lighting, and devices.
- Use stratified cross-validation on the training set for more stable
  hyperparameter selection.
- Run a second explainability method (e.g., LIME) and cross-check with Grad-CAM.
- Compare against a simple non-CNN baseline (e.g., logistic regression on
  raw pixels) to quantify how much benefit the CNN actually provides.
