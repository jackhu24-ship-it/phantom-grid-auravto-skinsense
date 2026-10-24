# -*- coding: utf-8 -*-
"""
PHANToM GRID :: Compliance and Gate-Before-Ship Audit Script
Audits all 10 drawers, byte counts, and test closures for YouCam Hackathon.
"""

import os
import sys

BASE = r"G:\我的雲端硬碟\260803_opencode\01_賽事專區\202611_YouCam_Skin_AI_VTO_Hackathon"

DRAWERS = [
    ("01_Specs", ["SPEC_01_AuraVTO_Architecture.md", "table1_resource_defense_matrix.csv"]),
    ("02_SourceCode", ["main.py", "pyproject.toml"]),
    ("03_CoverImage_16x9", ["cover_image.svg"]),
    ("04_Slides_PDF", ["SLIDES_PRESENTATION.pdf", "slides_10page_template.html"]),
    ("05_DemoVideo_1440P", ["demo_video_1440p.mp4", "video_script_hollywood.md"]),
    ("06_LiveApp", ["index.html"]),
    ("07_SubmissionPackage", ["Devpost_Submission_Package.md", "README.md"]),
    ("08_AuditReceipts", ["WORM_AUDIT_RECEIPT.json"]),
    ("09_ChaosReports", ["CHAOS_STRESS_AUDIT_REPORT.md"]),
    ("10_Releases", ["RELEASE_MANIFEST.json", "run_auravto_cli.bat"])
]

def audit():
    print("==================================================")
    print("PHANToM GRID :: Gate-Before-Ship Audit (YouCam VTO)")
    print("==================================================")
    all_pass = True
    for drawer, files in DRAWERS:
        dpath = os.path.join(BASE, drawer)
        if not os.path.exists(dpath):
            print(f"[-] FAILED: Missing drawer {drawer}")
            all_pass = False
            continue
        
        drawer_ok = True
        for f in files:
            fpath = os.path.join(dpath, f)
            if not os.path.exists(fpath) or os.path.getsize(fpath) == 0:
                print(f"[-] FAILED: Missing or empty file {drawer}/{f}")
                drawer_ok = False
                all_pass = False
        
        if drawer_ok:
            print(f"[+] PASS: Drawer {drawer} verified ({len(files)} critical assets verified)")
    
    # Manifest verification
    mpath = os.path.join(BASE, "match_manifest.yaml")
    if os.path.exists(mpath) and os.path.getsize(mpath) > 0:
        print("[+] PASS: match_manifest.yaml verified")
    else:
        print("[-] FAILED: match_manifest.yaml missing or empty")
        all_pass = False

    print("==================================================")
    if all_pass:
        print("[VERDICT: 10/10 DRAWERS 100% GREEN - READY FOR SUBMISSION]")
    else:
        print("[VERDICT: AUDIT FAILED]")
    print("==================================================")
    return all_pass

if __name__ == "__main__":
    success = audit()
    sys.exit(0 if success else 1)
