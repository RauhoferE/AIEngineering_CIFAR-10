# Put your own photos in this folder

Each class has its own subfolder. The folder name starts with the **class
index** (0–9) followed by an underscore and the **class name**.

Supported formats: `.jpg`, `.jpeg`, `.png`, `.bmp` (everything else is skipped).

## How many photos?
- **Minimum:** 50 total (5 per class). Below this the test metric is unstable.
- **Recommended:** 100 total (10 per class).
- **Ideal:** 200+ (20+ per class).

## File naming
It does not matter — the data loader reads every image file in each
folder. A simple numbering scheme makes your life easy:

    data/own/3_cat/3_001.jpg
    data/own/3_cat/3_002.jpg
    data/own/3_cat/3_003.jpg
    ...

## What makes a good own photo
- The object is the **clearly dominant** thing in the frame.
- Various **angles and lighting** across your set (not all the same shot).
- No people's faces, no license plates, no private-property interiors.

## What to do if a class is impossible
You cannot photograph a real deer easily. Options:
1. Use a figurine / toy model (mention this as a limitation in the report).
2. Photograph a printed photo on a magazine (also note as limitation).
3. Leave that class under-represented (most honest — note in ETHICS_AND_FAIRNESS.md).

Any of these is acceptable as long as you document it in your report.

## Metadata / privacy
Strip EXIF data (which can include GPS coordinates) before committing:

    # Linux / macOS (install: sudo apt install libimage-exiftool-perl)
    exiftool -all= data/own/*/*.jpg

    # Windows alternative: right-click file -> Properties -> Details ->
    # "Remove Properties and Personal Information".
