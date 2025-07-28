# Adobe India Hackathon 2025 – Round 1A Submission  
**Challenge Theme:** Connecting the Dots Through Docs

---

## 👣 Approach Overview

Our goal in Round 1A was to build a fast and offline-capable PDF outline extractor that detects the title and heading structure (H1, H2, H3) from a given document. This forms the foundation for a future intelligent reading system that can semantically understand and navigate PDFs.

---

## 🧱 System Architecture

### 1. **Input Handling**
The system scans the `/app/input` folder for any `.pdf` files (up to 50 pages each). Each file is processed individually and output to `/app/output` as a `.json` file.

### 2. **PDF Text & Metadata Extraction**
Using **PyMuPDF** (fitz), we extract structured text blocks from each page. The library gives us access to:
- Font size
- Position
- Span and line-level information

### 3. **Heading Detection Logic**
Instead of relying on document metadata (which is often missing), we use **font size heuristics** to infer heading levels:
- Font size > 17 → `H1`
- Font size > 14 → `H2`
- Font size > 12 → `H3`

These thresholds were calibrated on sample PDFs and can be further tuned per document corpus.

### 4. **JSON Output Generation**
For each detected heading, we store:
- Heading level (`H1`, `H2`, `H3`)
- Text content
- Page number (1-based)

The final output JSON for each file includes a `title` (based on the filename) and a structured `outline` array.

---

## 🛠 Technical Stack

- **Language:** Python 3.9
- **Library:** PyMuPDF (fitz)
- **Containerization:** Docker with `python:3.9-slim`
- **Runtime Requirements:** CPU-only, ≤ 200MB model size, ≤ 10s execution time

---

## ✅ Compliance with Constraints

| Constraint              | Status       |
|-------------------------|--------------|
| CPU-only                | ✅ Yes        |
| Model size < 200 MB     | ✅ 0 MB (no model used) |
| Runtime < 10 sec        | ✅ Achieved on 50-page PDFs |
| Offline Mode            | ✅ Fully offline (no network access) |

---

## 🚀 Considerations & Extensions

- Headings not always correspond to largest font — so position, boldness, and whitespace spacing can further enhance detection accuracy
- Can be extended to detect multilingual outlines using Unicode and script classification
- Forms the base architecture for Round 1B by providing clean document structure

---

## 🙌 Conclusion

This modular, lightweight extractor sets the stage for semantic PDF understanding. It provides the scaffolding needed to build future tools like topic search, content linking, and intelligent reading assistance.

