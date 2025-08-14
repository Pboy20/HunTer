import os
from docx import Document

def load_docx_text(filepath):
    if not os.path.exists(filepath):
        raise FileNotFoundError("File not Found.")
    if not filepath.endswith(".docx"):
        raise ValueError("Only .docx files are supported.")

    doc = Document(filepath)
    text = "\n".join([para.text for para in doc.paragraphs if para.text.strip() != ""])
    return text.strip()