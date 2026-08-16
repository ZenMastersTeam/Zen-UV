import os
import re
from pathlib import Path

# ==================== CONFIGURATION ====================

# Path to the text file containing the list of image files (one filename per line)
IMAGES_LIST_FILE = "images_list.txt"

# Path to the directory with your Markdown documentation
# '.' means the current working directory
DOCS_DIR = "../mkdocs"

CHECK_EMPTY_ALT_RECORDS = False

# =======================================================


def load_image_list(filepath):
    """Loads a list of image filenames from a plain text file."""
    path = Path(filepath)
    if not path.exists():
        print(f"❌ Error: Image list file '{filepath}' not found.")
        return []

    with open(path, "r", encoding="utf-8") as f:
        # Read lines, strip whitespace, and filter out empty lines
        return [line.strip() for line in f if line.strip()]


def analyze_documentation(docs_dir, target_images):
    docs_path = Path(docs_dir)
    if not docs_path.exists():
        print(f"❌ Error: Documentation directory '{docs_dir}' not found.")
        return

    # Regex for standard Markdown images: ![Alt text](path/to/image)
    md_img_pattern = re.compile(r'!\[([^\]]*)\]\(([^)]+)\)')

    # Regex for HTML <img> tags: <img src="path/to/image" alt="text">
    html_img_pattern = re.compile(r'<img\s+[^>]*src=["\']([^"\']+)["\'][^>]*>', re.IGNORECASE)
    html_alt_pattern = re.compile(r'alt=["\']([^"\']*)["\']', re.IGNORECASE)

    # Set of all image filenames referenced across all .md files
    used_image_filenames = set()

    # List of records for images missing alt text: (filename, md_file_path, line_number)
    empty_alt_records = []

    # Recursively traverse all .md files in the documentation directory
    for md_file in docs_path.rglob("*.md"):
        print(md_file)
        try:
            with open(md_file, "r", encoding="utf-8") as f:
                for line_num, line in enumerate(f, 1):
                    # 1. Check standard Markdown image syntax ![alt](url)
                    for alt_text, img_url in md_img_pattern.findall(line):
                        # Strip URL parameters (e.g., pic.png?v=1) and anchors
                        clean_url = img_url.split("?")[0].split("#")[0].strip()
                        filename = os.path.basename(clean_url)

                        if filename:
                            used_image_filenames.add(filename)

                            # Check if [] square brackets are empty
                            if not alt_text.strip():
                                empty_alt_records.append((filename, md_file, line_num))

                    # 2. Check HTML <img src="..."> tags
                    for img_url in html_img_pattern.findall(line):
                        clean_url = img_url.split("?")[0].split("#")[0].strip()
                        filename = os.path.basename(clean_url)

                        if filename:
                            used_image_filenames.add(filename)

                            # Check alt attribute in HTML tag
                            alt_match = html_alt_pattern.search(line)
                            if not alt_match or not alt_match.group(1).strip():
                                empty_alt_records.append((filename, md_file, line_num))

        except Exception as e:
            print(f"⚠️ Error reading file {md_file}: {e}")

    # Identify images from the list that were not found in any .md file
    unused_images = []
    for img_path in target_images:
        img_filename = os.path.basename(img_path)
        if img_filename not in used_image_filenames:
            unused_images.append(img_path)

    # --- Output Report ---

    print("=" * 65)
    print("📊 DOCUMENTATION ANALYSIS REPORT")
    print("=" * 65)

    print(f"\n🚫 UNUSED SCREENSHOTS FROM YOUR LIST ({len(unused_images)} items):")
    if unused_images:
        for img in unused_images:
            print(f"  • {img}")
    else:
        print("  ✅ All screenshots from the list are used in the articles!")

    if CHECK_EMPTY_ALT_RECORDS:
        print(f"\n⚠️  IMAGES MISSING ALT TEXT IN [] ({len(empty_alt_records)} items):")
        if empty_alt_records:
            for filename, md_file, line_num in empty_alt_records:
                print(f"  • File:     {filename}")
                print(f"    Location: {md_file} (line {line_num})")
                print("-" * 40)
        else:
            print("  ✅ All images in the articles have alt text descriptions!")


if __name__ == "__main__":
    target_images = load_image_list(IMAGES_LIST_FILE)
    if target_images:
        analyze_documentation(DOCS_DIR, target_images)
