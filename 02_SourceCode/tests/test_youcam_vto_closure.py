# -*- coding: utf-8 -*-
import pytest
from src.core.orchestrator import AuraVTOOrchestrator
from src.utils.vram_guard import VRAMCircuitBreaker

def test_nominal_e2e_cycle():
    """Gate 1: Nominal E2E Execution within automotive latency SLA (< 16.66ms)."""
    orch = AuraVTOOrchestrator()
    dummy_img = b"JPEG_DUMMY_IMAGE_BYTES_FOR_TESTING" * 50
    result = orch.execute_workflow(dummy_img, template_id="cyber_glam", load_ratio=0.5, memory_demand_gb=1.5)
    
    assert result["status"] == "PIPELINE_SUCCESS"
    assert result["cycle_latency_ms"] < 16.66, f"Latency SLA breached: {result['cycle_latency_ms']}ms"
    assert len(result["skin_diagnostics"]["biomarkers"]) == 16
    assert result["vto_output"]["ssim_fidelity"] >= 0.92

def test_vram_meltdown_breaker_50gb():
    """Gate 2: ASIL-D 50GB Meltdown Breaker hardware E-STOP."""
    orch = AuraVTOOrchestrator()
    dummy_img = b"JPEG_LARGE" * 20
    
    with pytest.raises(VRAMCircuitBreaker) as exc_info:
        orch.execute_workflow(dummy_img, memory_demand_gb=52.0)
    
    assert "exceeds 50.0GB ceiling" in str(exc_info.value)

def test_geometric_damping_135x():
    """Gate 3: Automatic 1.35x geometric damping scalar activation upon load > 0.85."""
    orch = AuraVTOOrchestrator()
    dummy_img = b"LOAD_TEST" * 20
    
    # Under heavy load (0.92 > 0.85 threshold)
    result = orch.execute_workflow(dummy_img, load_ratio=0.92, memory_demand_gb=1.0)
    assert result["damping_scalar"] == 1.35
    assert orch.damping.is_damped is True

def test_zdr_2pass_zero_residue():
    """Gate 4: 2-Pass bitwise memory scrub leaves exactly 0.000000 MB residue."""
    orch = AuraVTOOrchestrator()
    dummy_img = b"PII_CONFIDENTIAL_IMAGE_DATA" * 100
    result = orch.execute_workflow(dummy_img, memory_demand_gb=2.0)
    
    assert result["zdr_residue_mb"] == 0.000000
    assert len(result["audit_signature"]) == 64
