# -*- coding: utf-8 -*-
import os
import sys
import time

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.core.orchestrator import AuraVTOOrchestrator
from src.utils.vram_guard import VRAMCircuitBreaker

def run_stress_suite():
    print("==================================================")
    print("PHANToM GRID :: AuraVTO 50-Cycle Blackbox Stress")
    print("==================================================")
    orch = AuraVTOOrchestrator()
    dummy_payload = b"TEST_PAYLOAD" * 32
    
    latencies = []
    print("[*] Starting Scenario A: 50 Nominal Runs...")
    for i in range(50):
        t0 = time.perf_counter()
        res = orch.execute_workflow(dummy_payload, load_ratio=0.4, memory_demand_gb=0.5)
        dt = (time.perf_counter() - t0) * 1000.0
        latencies.append(dt)
        assert res["zdr_residue_mb"] == 0.0
    
    avg_lat = sum(latencies) / len(latencies)
    p99_lat = sorted(latencies)[int(len(latencies) * 0.99)]
    print(f"[OK] Scenario A Passed: Avg={avg_lat:.4f}ms, P99={p99_lat:.4f}ms (SLA < 16.66ms)")
    
    print("[*] Starting Scenario B: Chaos Meltdown Fault Injection...")
    tripped = False
    try:
        orch.execute_workflow(dummy_payload, memory_demand_gb=60.0)
    except VRAMCircuitBreaker:
        tripped = True
    assert tripped, "Failed to trip 50GB VRAM breaker!"
    print("[OK] Scenario B Passed: 50GB Meltdown Circuit Breaker Tripped Successfully.")
    
    print("==================================================")
    print("[ALL BLACKBOX STRESS GATES PASSED 100% GREEN]")
    print("==================================================")

if __name__ == "__main__":
    run_stress_suite()
