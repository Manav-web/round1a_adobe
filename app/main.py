import os
import fitz  # PyMuPDF
import json
from utils import extract_outline

INPUT_DIR = "/app/input"
OUTPUT_DIR = "/app/output"

def process_pdf(file_path):
    doc = fitz.open(file_path)
    title = os.path.splitext(os.path.basename(file_path))[0]
    outline = extract_outline(doc)
    return {
        "title": title,
        "outline": outline
    }

def main():
    for filename in os.listdir(INPUT_DIR):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(INPUT_DIR, filename)
            result = process_pdf(pdf_path)
            json_filename = filename.replace(".pdf", ".json")
            json_path = os.path.join(OUTPUT_DIR, json_filename)
            with open(json_path, "w", encoding="utf-8") as f:
                json.dump(result, f, indent=2)

if __name__ == "__main__":
    main()
