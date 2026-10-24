# SPEC_01 :: PHANToM GRID AuraVTO & SkinSense AI Technical Whitepaper
> Autonomous Agentic Skin Diagnostics & Spatial AR/VR Virtual Try-On Engine
> Sovereign Constitution v6.4.0 | Rule 65 (Tri-Standard Architecture)

---

## 1. System Overall Topology Diagram (Diagram 01)
```mermaid
graph TD
    subgraph IngressLayer ["Ingress & FastMCP Gateway Layer"]
        CLI["User CLI / REST Ingress"] --> SEC_CHK["Security Token & VRAM Pre-check"]
        MCP["YouCam MCP Gateway (mcp-api-01)"] --> SEC_CHK
    end
    subgraph CoreBrain ["Level 3 Sovereign Nexus Brain"]
        SEC_CHK --> ORCH["AuraVTO Master Orchestrator"]
        ORCH --> SM["FSM State Machine (4-Phase)"]
        ORCH --> CTX["Isolated Context Manager"]
    end
    subgraph EngineSwarm ["Level 2 Perception & Inference Swarm"]
        CTX --> SKIN["YouCam Skin AI Engine (16+ Biomarkers)"]
        SKIN --> EYE["PG-MOD-18 Spatial Eye (3DGS Manifold)"]
        EYE --> VTO["Look & Apparel VTO Synthesis Engine"]
        VTO --> REV["Convergence & Quality Reviewer"]
    end
    subgraph SafetyLayer ["Safety & Physical Layer"]
        REV --> DAMP["1.35x Geometric Damping Controller"]
        DAMP --> MELT["ASIL-D 50GB VRAM Circuit Breaker"]
        MELT --> ZDR["2-Pass ZDR (0xAA->0x00) Purger"]
        ZDR --> WORM["WORM Cryptographic Audit Receipt"]
    end
```

## 2. Full Lifecycle Sequence Diagram (Diagram 02)
```mermaid
sequenceDiagram
    autonumber
    actor User as Client / E-Commerce Consumer
    participant Ingress as Ingress Sentinel & Token Guard
    participant Core as AuraVTO Master Orchestrator
    participant SkinAI as YouCam Skin AI Analyzer
    participant Spatial as PG-MOD-18 3DGS Manifold
    participant VTO as Virtual Try-On Pipeline
    participant Safety as ASIL-D Safety & ZDR Purger

    User->>Ingress: Submit Selfie / Image Stream + Look Request
    Ingress->>Ingress: Verify VRAM (<50GB) & Bearer Token
    Ingress->>Core: Dispatch Sanitized Request
    Core->>SkinAI: Analyze Skin Diagnostics (Texture, Redness, Oiliness)
    SkinAI-->>Core: Return Diagnostic Manifold Vector
    Core->>Spatial: Reconstruct 3D Facial Keypoints & Lighting SE(3)
    Spatial-->>Core: Calibrated 3D Face Anchor
    Core->>VTO: Apply Look VTO Template + Skin Conditioning
    VTO-->>Core: High-Fidelity Photorealistic AR/VR Texture
    Core->>Safety: Check Memory & System Load
    alt Load > 85%
        Safety->>Core: Apply 1.35x Damping Jump
    else Nominal
        Safety->>Core: Nominal 1.0x Pass
    end
    Safety->>Safety: 2-Pass ZDR Memory Purge (0.000000 MB Residue)
    Core->>User: Deliver Diagnostic Report & High-Res Try-On Render
```

## 3. Finite State Machine Diagram (Diagram 03)
```mermaid
stateDiagram-v2
    [*] --> IngressValidation : User Selfie Received
    IngressValidation --> SkinDiagnostics : Nonce & Token Validated
    IngressValidation --> FaultTrip : Invalid Image / Auth Failure
    SkinDiagnostics --> SpatialMeshAlignment : 16 Biomarkers Extracted
    SpatialMeshAlignment --> LookVTORender : 3D Keypoints Aligned
    LookVTORender --> QualityAudit : Texture Composite Finished
    QualityAudit --> ZDRPurgeAndRelease : SSIM >= 0.92 & Load Nominal
    QualityAudit --> DampedRetry : Load > 85% or Jitter Detected
    DampedRetry --> LookVTORender : 1.35x Damping Applied
    ZDRPurgeAndRelease --> [*] : ZDR Zero-Residue Verified
    FaultTrip --> [*] : Emergency Halt (ESTOP)
```

## 4. Security Boundary & Meltdown Guard Diagram (Diagram 04)
```mermaid
graph LR
    subgraph UntrustedZone ["Untrusted External Domain"]
        RawInput["Raw User Photo / Video Feed"]
        ExtAPI["Public Cloud / Third-Party Endpoints"]
    end
    subgraph DMZBoundary ["DMZ Sanitization Gateway"]
        AuthFilter["Bearer Token Sanitizer"]
        VRAMFence["50GB VRAM Early Threshold Sentinel"]
    end
    subgraph TrustedCore ["Sovereign Execution Core"]
        Engine["AuraVTO Deterministic Engine"]
        ZDR_Wipe["2-Pass Bitwise Memory Scrubber"]
    end
    RawInput --> AuthFilter
    ExtAPI --> AuthFilter
    AuthFilter --> VRAMFence
    VRAMFence --> Engine
    Engine --> ZDR_Wipe
```

## 5. Table 1: Resource Defense & Invariant Matrix
| Component ID | Subsystem Target | Hardware Ceilings | Failsafe Trip Condition | Purge Invariant |
| :--- | :--- | :---: | :---: | :---: |
| **DEF-01** | Ingress Token Gateway | < 10ms Latency | Malformed Nonce / Auth Failure | Immediate Socket Drop |
| **DEF-02** | YouCam Skin Diagnostic Hub | 16 Biomarkers | Response Latency > 1500ms | Failover to Local Heuristic |
| **DEF-03** | PG-MOD-18 3DGS Manifold | 4000 Gaussians | Mesh Drift > 1.2mm | Dynamic Rigidity Anchor |
| **DEF-04** | Damping Controller | 1.35x Damping Scalar | Load Ratio > 0.85 | Automatic Backoff Step |
| **DEF-05** | Memory Meltdown Breaker | 50.0 GB VRAM | Memory Footprint >= 50.0 GB | Instant ESTOP Interruption |
| **DEF-06** | Zero Data Residue (ZDR) | 2-Pass Bitwise Scrub | Residual Footprint > 0.000000 MB | Cryptographic Vault Lockdown |
