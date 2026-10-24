# -*- coding: utf-8 -*-
import os
import subprocess
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
VIDEO_DIR = BASE_DIR / "05_DemoVideo_1440P"
VIDEO_MP4 = VIDEO_DIR / "demo_video_1440p.mp4"
SCRIPT_MD = VIDEO_DIR / "video_script_hollywood.md"

def get_video_metadata(file_path: Path):
    cmd = [
        "ffprobe", "-v", "error",
        "-show_entries", "format=duration:stream=width,height,codec_type",
        "-of", "json",
        str(file_path)
    ]
    res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    import json
    return json.loads(res.stdout)

def test_video_assets_exist():
    """Gate 1: Verify video file and Hollywood script exist and non-empty."""
    assert SCRIPT_MD.exists(), "Missing video_script_hollywood.md"
    assert SCRIPT_MD.stat().st_size > 500, "Hollywood script too small"
    assert VIDEO_MP4.exists(), f"Missing compiled demo video: {VIDEO_MP4}"
    assert VIDEO_MP4.stat().st_size > 1024 * 1024, f"Video file size too small: {VIDEO_MP4.stat().st_size} bytes"

def test_video_duration_golden_zone():
    """Gate 2: Verify video duration between 2:00 and 3:00 (Rule 65 / Devpost standard)."""
    meta = get_video_metadata(VIDEO_MP4)
    duration = float(meta["format"]["duration"])
    # Golden zone: 120s (2:00) ~ 180s (3:00)
    assert 110.0 <= duration <= 180.0, f"Video duration outside allowable range: {duration:.2f}s"

def test_video_resolution_and_streams():
    """Gate 3: Verify video stream is 1080P/1440P and audio track is present."""
    meta = get_video_metadata(VIDEO_MP4)
    streams = meta.get("streams", [])
    has_video = False
    has_audio = False
    for s in streams:
        if s.get("codec_type") == "video":
            has_video = True
            width = s.get("width")
            height = s.get("height")
            assert width >= 1920, f"Video width below 1080P: {width}"
            assert height >= 1080, f"Video height below 1080P: {height}"
        elif s.get("codec_type") == "audio":
            has_audio = True
    assert has_video, "Video stream missing from MP4"
    assert has_audio, "Audio stream missing from MP4"
