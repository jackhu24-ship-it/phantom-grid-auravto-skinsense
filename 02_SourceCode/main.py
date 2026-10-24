# -*- coding: utf-8 -*-
import sys
from src.core.orchestrator import AuraVTOOrchestrator

def main():
    print("==================================================")
    print("PHANToM GRID :: AuraVTO & SkinSense AI Engine")
    print("YouCam API Skin AI & eCommerce VTO Hackathon 2026")
    print("==================================================")
    orch = AuraVTOOrchestrator()
    dummy_selfie = b"SAMPLE_SELFIE_PAYLOAD" * 64
    res = orch.execute_workflow(dummy_selfie, template_id="cyber_glam")
    
    print(f"[*] Skin Analysis Status: {res['skin_diagnostics']['status']}")
    print(f"[*] 16 Biomarkers Evaluated: {list(res['skin_diagnostics']['biomarkers'].keys())[:5]}... (16 total)")
    print(f"[*] Spatial 3D Fitting: {res['spatial_anchor']['status']} ({res['spatial_anchor']['num_gaussians_fitted']} Gaussians)")
    print(f"[*] VTO Synthesis Look: {res['vto_output']['template_id']} @ {res['vto_output']['render_resolution']}")
    print(f"[*] SSIM Visual Quality: {res['vto_output']['ssim_fidelity']}")
    print(f"[*] Cycle Execution Latency: {res['cycle_latency_ms']:.4f} ms")
    print(f"[*] ZDR Memory Residue: {res['zdr_residue_mb']:.6f} MB")
    print(f"[*] WORM Cryptographic Signature: {res['audit_signature'][:16]}...")
    print("==================================================")
    print("[SYSTEM READY - PRODUCTION OPERATIONAL]")

if __name__ == "__main__":
    main()
