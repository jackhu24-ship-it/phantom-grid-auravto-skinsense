# -*- coding: utf-8 -*-
import os
import csv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
SPECS_DIR = BASE_DIR / "01_Specs"

def test_specs_whitepaper_contains_four_diagrams():
    """Verify SPEC_01 markdown whitepaper embeds all 4 Mermaid diagrams."""
    wp = SPECS_DIR / "SPEC_01_AuraVTO_Architecture.md"
    assert wp.exists(), "Missing SPEC_01_AuraVTO_Architecture.md"
    content = wp.read_text(encoding="utf-8")
    
    assert "graph TD" in content or "flowchart TD" in content, "Missing System Topology diagram"
    assert "sequenceDiagram" in content, "Missing Sequence Diagram"
    assert "stateDiagram" in content, "Missing State Machine Diagram"
    assert "graph LR" in content, "Missing Security Boundary Diagram"

def test_four_standalone_mmd_blueprints():
    """Verify standalone blueprints exist in 01_Specs/blueprints/ without truncation."""
    bp_dir = SPECS_DIR / "blueprints"
    assert bp_dir.exists(), "Missing blueprints directory"
    
    required_mmd = [
        "01_system_topology.mmd",
        "02_sequence_flow.mmd",
        "03_state_machine.mmd",
        "04_security_boundary.mmd"
    ]
    for mmd in required_mmd:
        p = bp_dir / mmd
        assert p.exists(), f"Missing standalone blueprint: {mmd}"
        assert p.stat().st_size > 100, f"Blueprint {mmd} is truncated or empty"

def test_table1_resource_defense_matrix_csv():
    """Verify Table 1 CSV contract exists, has header and valid component rows."""
    csv_file = SPECS_DIR / "table1_resource_defense_matrix.csv"
    assert csv_file.exists(), "Missing table1_resource_defense_matrix.csv"
    
    with open(csv_file, "r", encoding="utf-8") as f:
        reader = list(csv.reader(f))
        assert len(reader) >= 6, f"Table 1 CSV row count insufficient: {len(reader)}"
        header = reader[0]
        assert "Component_ID" in header
        assert "Hardware_Ceilings" in header
        assert "Failsafe_Trip_Condition" in header
