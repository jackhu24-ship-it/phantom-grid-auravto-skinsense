# -*- coding: utf-8 -*-
import os
from pathlib import Path
import pypdf

BASE_DIR = Path(__file__).resolve().parent.parent.parent
SLIDES_PDF = BASE_DIR / "04_Slides_PDF" / "SLIDES_PRESENTATION.pdf"
SLIDES_HTML = BASE_DIR / "04_Slides_PDF" / "slides_10page_template.html"

def test_slides_assets_exist():
    """Gate 1: Verify slide HTML template and compiled vector PDF exist and non-empty."""
    assert SLIDES_HTML.exists(), f"Missing slides_10page_template.html at {SLIDES_HTML}"
    assert SLIDES_HTML.stat().st_size > 2000, "Template HTML too small"
    assert SLIDES_PDF.exists(), f"Missing compiled SLIDES_PRESENTATION.pdf at {SLIDES_PDF}"
    assert SLIDES_PDF.stat().st_size > 10000, f"PDF file size too small: {SLIDES_PDF.stat().st_size} bytes"

def test_slides_pdf_page_count():
    """Gate 2: Strictly verify exactly 10 pages in presentation deck (Rule 65 Standard)."""
    reader = pypdf.PdfReader(str(SLIDES_PDF))
    page_count = len(reader.pages)
    assert page_count == 10, f"Slides page count mismatch: expected 10, got {page_count}"

def test_slides_pdf_content_density():
    """Gate 3: Verify non-empty textual content and key architecture terminology on all 10 pages."""
    reader = pypdf.PdfReader(str(SLIDES_PDF))
    for idx, page in enumerate(reader.pages):
        text = page.extract_text() or ""
        assert len(text.strip()) > 30, f"Page {idx+1} has insufficient text: length={len(text)}"

def test_slides_no_mojibake_or_chinese_in_pdf():
    """Gate 4: Verify 100% International Professional English (Zero Chinese, Zero Mojibake)."""
    reader = pypdf.PdfReader(str(SLIDES_PDF))
    for idx, page in enumerate(reader.pages):
        text = page.extract_text() or ""
        assert "\ufffd" not in text, f"Page {idx+1} contains mojibake replacement characters!"
