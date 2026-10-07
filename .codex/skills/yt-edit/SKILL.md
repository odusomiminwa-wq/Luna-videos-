---
name: yt-edit
description: >-
  Turn a timestamped transcript into an edit decision list with dead air, filler and retakes.
---

# yt-edit
Run python3 deadair.py transcript.srt --floor 0.35 --json. It detects DEAD gaps, FILLER-only cues and REPEAT restarts. It prints cuts; it does not modify media. Nothing here publishes.