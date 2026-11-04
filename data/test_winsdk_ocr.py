# -*- coding: utf-8 -*-
import asyncio
import os
import winsdk.windows.graphics.imaging as imaging
import winsdk.windows.media.ocr as ocr
import winsdk.windows.storage as storage

async def test_ocr(image_path):
    abs_path = os.path.abspath(image_path)
    file = await storage.StorageFile.get_file_from_path_async(abs_path)
    stream = await file.open_async(storage.FileAccessMode.READ)
    decoder = await imaging.BitmapDecoder.create_async(stream)
    bitmap = await decoder.get_software_bitmap_async()

    engine = ocr.OcrEngine.try_create_from_user_profile_languages()
    if not engine:
        print("Failed to create OCR engine")
        return

    result = await engine.recognize_async(bitmap)
    print("Recognized text length:", len(result.text))
    print("First 300 characters of recognized text:")
    print("----------------------------------------")
    print(result.text[:300])
    print("----------------------------------------")
    print(f"Total lines recognized: {len(result.lines)}")
    if result.lines:
        first_line = result.lines[0]
        print(f"Line 1: '{first_line.text}' with {len(first_line.words)} words")
        if first_line.words:
            w = first_line.words[0]
            print(f"Word 1: '{w.text}' bbox: ({w.bounding_rect.x}, {w.bounding_rect.y}, {w.bounding_rect.width}, {w.bounding_rect.height})")

if __name__ == "__main__":
    img_path = r"C:\DMDG_Jobs\DMDG_PRJ\ai_math_exam\data\test_p1.png"
    asyncio.run(test_ocr(img_path))
