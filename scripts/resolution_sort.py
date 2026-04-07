#!/usr/bin/env python3

import os
import shutil
from PIL import Image
from pathlib import Path

SOURCE_DIR = "."
TARGET_DIR = "walled_tiers"
IGNORE = {".git", ".github", TARGET_DIR}

# Define your tiers (Width thresholds)
TIERS = {"8k": 7680, "4k": 3840, "1440p": 2560, "1080p": 1920, "low_res": 0}


def get_tier(file_path):
    try:
        with Image.open(file_path) as img:
            w = img.width
            # Find the highest tier the image qualifies for
            for name, threshold in TIERS.items():
                if w >= threshold:
                    return name
    except:
        return None


def main():
    target_path = Path(TARGET_DIR)

    for img_file in Path(SOURCE_DIR).rglob("*"):
        if img_file.suffix.lower() in {".jpg", ".jpeg", ".png", ".webp"}:
            if any(part in IGNORE for part in img_file.parts):
                continue

            tier = get_tier(img_file)
            if tier:
                # Path: walled_tiers/4k/original_category/image.jpg
                # This preserves the artist/category info
                category = img_file.parent.name
                dest = target_path / tier / category
                dest.mkdir(parents=True, exist_ok=True)
                shutil.copy2(img_file, dest / img_file.name)

    print("Tiered sorting complete.")


if __name__ == "__main__":
    main()
