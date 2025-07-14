# Image to text

This script automatically processes all images located in the input/ folder and extracts their text using OCR (Optical Character Recognition) using the Tesseract tool. It supports text in Spanish and English, and uses a language detector to identify which language predominates in each image.

## How to build and run

### 1. Build the image
``` shell
docker build -t ocr-batch-app .
```

### 2. Run the container with an image as a volume
``` shell
docker run --rm \
  -v $(pwd)/input:/app/input \
  -v $(pwd)/output:/app/output \
  ocr-batch-app
```
