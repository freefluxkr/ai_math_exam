# -*- coding: utf-8 -*-
import asyncio
import io
import os
import sys
import time
import zipfile
import xml.etree.ElementTree as ET
from PIL import Image
import pymupdf
import winsdk.windows.graphics.imaging as imaging
import winsdk.windows.media.ocr as ocr
import winsdk.windows.storage as storage

A4_W, A4_H = 595.28, 841.89
TEMP_OCR_FILE = os.path.abspath(r"C:\DMDG_Jobs\DMDG_PRJ\ai_math_exam\data\temp_ocr.png")

async def ocr_image(engine, pil_img):
    # Save optimized PNG for OCR
    pil_img.save(TEMP_OCR_FILE, format="PNG")
    file = await storage.StorageFile.get_file_from_path_async(TEMP_OCR_FILE)
    stream = await file.open_async(storage.FileAccessMode.READ)
    decoder = await imaging.BitmapDecoder.create_async(stream)
    bitmap = await decoder.get_software_bitmap_async()
    result = await engine.recognize_async(bitmap)
    return result

async def convert_docx_to_searchable_pdf(docx_path, out_pdf_path, engine):
    print(f"\n==========================================")
    print(f"Processing: {os.path.basename(docx_path)}")
    t0 = time.time()

    with zipfile.ZipFile(docx_path, "r") as z:
        xml_content = z.read("word/document.xml")
        rels_content = z.read("word/_rels/document.xml.rels")
        root_rels = ET.fromstring(rels_content)
        rel_map = {rel.attrib.get("Id"): rel.attrib.get("Target") for rel in root_rels}
        root = ET.fromstring(xml_content)
        blips = root.findall(".//{http://schemas.openxmlformats.org/drawingml/2006/main}blip")

        img_targets = []
        for b in blips:
            embed_id = b.attrib.get("{http://schemas.openxmlformats.org/officeDocument/2006/relationships}embed")
            target = rel_map.get(embed_id)
            if target:
                if not target.startswith("word/"):
                    target = "word/" + target
                img_targets.append(target)

        total_pages = len(img_targets)
        print(f"Total pages: {total_pages}")

        pdf_doc = pymupdf.open()

        for idx, target in enumerate(img_targets):
            img_bytes = z.read(target)
            pil_img = Image.open(io.BytesIO(img_bytes))
            if pil_img.mode != "RGB":
                pil_img = pil_img.convert("RGB")

            # Page background image (high quality JPEG)
            buf = io.BytesIO()
            pil_img.save(buf, format="JPEG", quality=95, optimize=True)
            jpeg_bytes = buf.getvalue()

            # OCR for selectable text
            ocr_res = await ocr_image(engine, pil_img)

            page = pdf_doc.new_page(width=A4_W, height=A4_H)
            page.insert_font(fontname="malgun", fontfile=r"C:\Windows\Fonts\malgun.ttf")

            img_w, img_h = pil_img.size
            scale = min(A4_W / img_w, A4_H / img_h)
            scaled_w = img_w * scale
            scaled_h = img_h * scale
            x0 = (A4_W - scaled_w) / 2
            y0 = (A4_H - scaled_h) / 2

            # 1. Insert visual page image
            target_rect = pymupdf.Rect(x0, y0, x0 + scaled_w, y0 + scaled_h)
            page.insert_image(target_rect, stream=jpeg_bytes)

            # 2. Insert selectable / searchable text layer (render_mode=3 invisible text)
            for line in ocr_res.lines:
                if not line.words or not line.text.strip():
                    continue
                min_x = min(w.bounding_rect.x for w in line.words)
                min_y = min(w.bounding_rect.y for w in line.words)
                max_x = max(w.bounding_rect.x + w.bounding_rect.width for w in line.words)
                max_y = max(w.bounding_rect.y + w.bounding_rect.height for w in line.words)

                lx = x0 + min_x * scale
                ly = y0 + min_y * scale
                lw = (max_x - min_x) * scale
                lh = (max_y - min_y) * scale

                fontsize = max(7, lh * 0.8)
                baseline_y = ly + lh * 0.82
                page.insert_text(pymupdf.Point(lx, baseline_y), line.text, fontsize=fontsize, fontname="malgun", render_mode=3)

            if (idx + 1) % 10 == 0 or (idx + 1) == total_pages:
                print(f"  Processed {idx + 1}/{total_pages} pages...")

        temp_pdf = out_pdf_path + ".tmp"
        pdf_doc.save(temp_pdf, deflate=True)
        pdf_doc.close()

        if os.path.exists(out_pdf_path):
            os.remove(out_pdf_path)
        os.rename(temp_pdf, out_pdf_path)

        t1 = time.time()
        print(f"Saved: {os.path.basename(out_pdf_path)} ({os.path.getsize(out_pdf_path) / (1024*1024):.2f} MB) in {t1 - t0:.1f}s")

async def main():
    base_dir = r"C:\Users\PC\Downloads\DOIT_안티그레비티 도서내용 및 강의자료\DOIT_안티그레비티 도서내용 및 강의자료"
    files = sorted([f for f in os.listdir(base_dir) if f.endswith(".docx")])

    print(f"Found {len(files)} docx files to convert to Searchable/Selectable PDF.")
    engine = ocr.OcrEngine.try_create_from_user_profile_languages()

    start_total = time.time()
    for fname in files:
        docx_path = os.path.join(base_dir, fname)
        pdf_name = os.path.splitext(fname)[0] + ".pdf"
        out_pdf_path = os.path.join(base_dir, pdf_name)
        await convert_docx_to_searchable_pdf(docx_path, out_pdf_path, engine)

    total_time = time.time() - start_total
    print(f"\nAll {len(files)} documents successfully converted in {total_time:.1f} seconds!")

if __name__ == "__main__":
    asyncio.run(main())

