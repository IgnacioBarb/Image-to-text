from PIL import Image
import pytesseract
from langdetect import detect, LangDetectException
from pathlib import Path

INPUT_DIR = Path("input")
OUTPUT_DIR = Path("output")

def extract_text(image_path):
    try:
        image = Image.open(image_path)
        text = pytesseract.image_to_string(image, lang="spa+eng").strip()
        try:
            language = detect(text)
        except LangDetectException:
            language = "unknown"
        return text, language
    except Exception as e:
        return f"Error processing {image_path.name}: {e}", "error"

def process_images():
    OUTPUT_DIR.mkdir(exist_ok=True)
    images = list(INPUT_DIR.glob("*.[pjJP][pnPNgG]*"))  # jpg, png, jpeg

    if not images:
        print("No images found in the 'input/' folder.")
        return

    for img in images:
        print(f"Processing {img.name}...")
        text, language = extract_text(img)
        output_file = OUTPUT_DIR / (img.stem + ".txt")
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(f"[Detected language: {language}]\n\n")
            f.write(text)
        print(f"Text saved to: {output_file} (Language: {language})")

if __name__ == "__main__":
    process_images()
