# **maintenance tools**

Tools for organizing the wallpaper library.

## **Setup**

### **Nix**

Enter the development shell from the repository root:

```bash
nix develop
```

### **Non-Nix**

Install dependencies via Poetry:

```bash
poetry install
```

## **Usage**

The resolution\_sort.py script crawls a source directory and copies images into
the walled\_tiers/ hierarchy based on their dimensions.

**Using Poetry:**

```bash
poetry run python -m resolution_sort
```

## **Logic**

Tiers are determined by horizontal pixel count. Original category names (the
parent folder of the image) are preserved within each resolution tier.
