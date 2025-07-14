FROM python:3.11-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    tesseract-ocr-spa \
    tesseract-ocr-eng \
    libtesseract-dev \
    libleptonica-dev \
    && apt-get clean

# Create working directory
WORKDIR /app

# Copy files
COPY requirements.txt .
COPY ocr_script.py .

# Create input and output folders inside the container
RUN mkdir input output

# Install Python Dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run script by default
CMD ["python", "ocr_script.py"]
