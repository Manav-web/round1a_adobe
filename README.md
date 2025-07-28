# 📄 Adobe Hackathon 2025 – Round 1A: PDF Outline Extractor

This is the solution for **Round 1A** of the Adobe India Hackathon 2025.  
The project extracts a structured outline (headings) from PDF documents using font size heuristics.  
✅ Japanese language supported.

---

## 🚀 Setup and Run (via Docker)

### 1️⃣ Build Docker Image

Open Command Prompt in `C:\Users\kanav\round1a_adobe`:

```bash
docker build -t adobe_round1a:local .
```

---

### 2️⃣ Add Input PDF(s)

Place your `.pdf` file(s) inside the `input/` folder.

---

### 3️⃣ Run the Container

```bash
docker run --rm ^
-v "C:\Users\kanav\round1a_adobe\input:/app/input" ^
-v "C:\Users\kanav\round1a_adobe\output:/app/output" ^
--network none ^
adobe_round1a:local
```

---

### 4️⃣ View Output

```bash
python view_round1a_output.py
```

The output will be saved to `output/round1a_output.json`.

---

## 📁 Folder Structure

```
round1a_adobe/
├── app/
│   ├── main.py
│   └── utils.py
|    ── requirements.txt
├── input/
├── output/
├── Dockerfile
├── view_round1a_output.py
└── README.md
```

---

## 📝 Notes

- Uses PyMuPDF (`fitz`) for PDF parsing
- Font size thresholds determine heading levels (H1, H2, H3)
- Supports Japanese and multilingual PDFs