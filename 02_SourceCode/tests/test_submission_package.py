# -*- coding: utf-8 -*-
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
SUBMISSION_PKG = BASE_DIR / "07_SubmissionPackage" / "Devpost_Submission_Package.md"
README_FILE = BASE_DIR / "README.md"

def test_submission_package_exists_and_sections():
    """Verify Devpost Submission Package exists and has all 7 mandatory sections."""
    assert SUBMISSION_PKG.exists(), "Missing Devpost_Submission_Package.md"
    content = SUBMISSION_PKG.read_text(encoding="utf-8")
    
    # 7 mandatory Devpost sections
    sections = [
        "1. Inspiration",
        "2. What It Does",
        "3. How We Built It",
        "4. Challenges We Ran Into",
        "5. Accomplishments That We're Proud Of",
        "6. What We Learned",
        "7. What's Next"
    ]
    for s in sections:
        assert s in content, f"Missing required Devpost section: {s}"

def test_elevator_pitch_length():
    """Verify elevator pitch strictly <= 200 characters limit."""
    content = SUBMISSION_PKG.read_text(encoding="utf-8")
    pitch_line = ""
    lines = content.splitlines()
    for i, line in enumerate(lines):
        if "Elevator Pitch" in line and i + 1 < len(lines):
            pitch_line = lines[i+1].strip()
            break
    assert len(pitch_line) > 20, "Elevator pitch is empty or missing"
    assert len(pitch_line) <= 200, f"Elevator pitch exceeds 200 chars limit: len={len(pitch_line)}"

def test_quickstart_reproduction_commands():
    """Verify 3-line quickstart contains -b main, pytest, and clone URL."""
    content = SUBMISSION_PKG.read_text(encoding="utf-8")
    assert "git clone -b main" in content, "Missing git clone -b main"
    assert "pytest" in content, "Missing pytest in reproduction commands"

def test_lead_architect_contact_and_github():
    """Verify Lead Architect Jack Hu and contact metadata."""
    content = SUBMISSION_PKG.read_text(encoding="utf-8")
    assert "Jack Hu" in content, "Missing Lead Architect Jack Hu"
    assert "jackhu24@gmail.com" in content, "Missing contact email"
    assert "github.com/jackhu24-ship-it" in content, "Missing GitHub profile URL"
