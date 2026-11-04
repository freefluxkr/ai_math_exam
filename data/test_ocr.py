# -*- coding: utf-8 -*-
import asyncio
import os

# Test Windows Media OCR via Python using winsdk
print("Testing Windows OCR availability...")
try:
    import winsdk.windows.media.ocr as ocr
    import winsdk.windows.graphics.imaging as imaging
    import winsdk.windows.storage as storage
    print("winsdk installed!")
except ImportError:
    print("winsdk not installed, testing powershell call...")

