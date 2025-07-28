import fitz  # PyMuPDF

def extract_outline(doc):
    """
    Extracts outline based on font size — identifies H1, H2, H3 headings
    """
    outline = []
    for page_num in range(len(doc)):
        page = doc[page_num]
        blocks = page.get_text("dict")["blocks"]
        for block in blocks:
            if block['type'] != 0:
                continue
            for line in block['lines']:
                line_text = " ".join([span['text'] for span in line['spans']]).strip()
                font_size = max(span['size'] for span in line['spans'])

                # Heuristic for heading levels (adjust thresholds if needed)
                if font_size > 17:
                    level = "H1"
                elif font_size > 14:
                    level = "H2"
                elif font_size > 12:
                    level = "H3"
                else:
                    continue

                outline.append({
                    "level": level,
                    "text": line_text,
                    "page": page_num + 1
                })
    return outline

def extract_unicode_text(pdf_path):
    """
    Extracts full Unicode text from a PDF.
    Supports languages like Japanese, Hindi, etc.
    """
    doc = fitz.open(pdf_path)
    full_text = ""
    for page in doc:
        blocks = page.get_text("blocks")  # block-wise text
        blocks = sorted(blocks, key=lambda b: (b[1], b[0]))  # sort by Y, then X
        for block in blocks:
            text = block[4]
            if text.strip():
                full_text += text.strip() + "\n"
    doc.close()
    return full_text

