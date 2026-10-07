---
name: yt-audit
description: >-
  Audit a YouTube channel end to end - packaging, consistency, the first
  fifteen seconds, and what to fix first. Use for "audit my channel", "why
  isn't my channel growing", "review my videos", or a pasted channel URL.
---

# yt-audit

An audit that lists twenty problems is a way of avoiding the one that matters. This ends in ONE fix.

## Before you write

1. Read ~/.codex/youtube/voice.md if it exists. If it does not exist, ask for three of their own videos, read or transcribe them, infer the voice, and write the file.
2. Never invent a number, a result or a source.

## What to look at
1. Last ten titles as a set; run them through ../yt-package/title.py.
2. Thumbnails at feed size.
3. First fifteen seconds of three recent videos; score with ../yt-script/hookscore.py.
4. Upload consistency.
5. Retention shape if available.

## What to hand back
- The single biggest fix.
- Three things already working.
- What NOT to do yet.

Nothing here publishes. Every output ends with: ship it, or change it?