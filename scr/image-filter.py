import os
from pathlib import Path

import cv2

base_path = "data/scrapped/"


def review_images(folder_path):
    # Supported image extensions
    valid_extensions = (".jpg", ".jpeg", ".png", ".bmp", ".webp")

    # Get list of images and sort them so they show in order
    files = [f for f in os.listdir(folder_path) if f.lower().endswith(valid_extensions)]

    if not files:
        print("No images found in that folder.")
        return

    print(f"Found {len(files)} images. \n[k] = KEEP | [d] = DELETE | [q] = QUIT")

    window_name = "Image Review"
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)

    # 2. Set your fixed size (Width, Height)
    cv2.resizeWindow(window_name, 800, 600)

    for filename in files:
        file_path = os.path.join(folder_path, filename)

        # Load image
        img = cv2.imread(file_path)
        if img is None:
            print(f"Could not read {filename}, skipping...")
            continue

        # Resize image if it's too big for your screen (optional)
        # img = cv2.resize(img, (800, 600))
        img = cv2.resize(img, (800, 600))
        # Display image
        cv2.imshow("Image Review - [k] Keep, [d] Delete, [q] Quit", img)

        # Wait for keypress
        key = cv2.waitKey(0) & 0xFF

        if key == ord("d"):
            cv2.destroyAllWindows()  # Close window briefly to show progress
            os.remove(file_path)
            print(f"🗑️ Deleted: {filename}")
        elif key == ord("k"):
            print(f"✅ Kept: {filename}")
        elif key == ord("q"):
            print("Exiting...")
            break

    cv2.destroyAllWindows()
    print("Review complete.")


if __name__ == "__main__":
    # Point this to the folder icrawler created (e.g., 'my_data')
    # target_folder = "my_data"
    p = Path(base_path)
    folders = [f.name for f in p.iterdir() if f.is_dir()]
    for folder in folders:
        review_images(os.path.join(base_path, folder))
    # review_images(target_folder)
