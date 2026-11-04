# -*- coding: utf-8 -*-
import asyncio
import io
import os
import zipfile
import xml.etree.ElementTree as ET
from PIL import Image
import pymupdf
import winsdk.windows.graphics.imaging as imaging
import winsdk.windows.media.ocr as ocr
import winsdk.windows.storage as storage

async def ocr_image_bytes(engine, img_bytes):
    # Convert image bytes to temporary PNG in memory or temp file
    temp_path = os.path.abspath(r"C:\DMDG_Jobs\DMDG_PRJ\ai_math_exam\data\temp_ocr.png")
    with open(temp_path, "wb") as f:
        f.write(img_bytes)

    file = await storage.StorageFile.get_file_from_path_async(temp_path)
    stream = await file.open_async(storage.FileAccessMode.READ)
    decoder = await imaging.BitmapDecoder.create_async(stream)
    bitmap = await decoder.get_software_bitmap_async()
    result = await engine.recognize_async(bitmap)
    return result

async def test_chapter_1_searchable():
    engine = ocr.OcrEngine.try_create_from_user_profile_languages()
    docx_path = r"C:\Users\PC\Downloads\DOIT_안티그레비티 도서내용 및 강의자료\DOIT_안티그레비티 도서내용 및 강의자료\1장 안티그래비티와 프롬프트 기초.docx"
    out_pdf = r"C:\Users\PC\Downloads\DOIT_안티그레비티 도서내용 및 강의자료\DOIT_안티그레비티 도서내용 및 강의자료\test_ch1_searchable.pdf"

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

        pdf_doc = pymupdf.open()
        A4_W, A4_H = 595.28, 841.89

        for idx, target in enumerate(img_targets[:5]):  # test 5 pages first
            img_bytes = z.read(target)
            pil_img = Image.open(io.BytesIO(img_bytes))
            if pil_img.mode != "RGB":
                pil_img = pil_img.convert("RGB")

            # Save JPEG for page background
            buf = io.BytesIO()
            pil_img.save(buf, format="JPEG", quality=95, optimize=True)
            jpeg_bytes = buf.getvalue()

            # Save PNG for OCR
            png_buf = io.BytesIO()
            pil_img.save(png_buf, format="PNG")
            ocr_res = await ocr_image_bytes(engine, png_buf.getvalue())

            page = pdf_doc.new_page(width=A4_W, height=A4_H)
            page.insert_font(fontname="malgun", fontfile=r"C:\Windows\Fonts\malgun.ttf")

            img_w, img_h = pil_img.size
            scale = min(A4_W / img_w, A4_H / img_h)
            scaled_w = img_w * scale
            scaled_h = img_h * scale
            x0 = (A4_W - scaled_w) / 2
            y0 = (A4_H - scaled_h) / 2

            # 1. Insert image
            target_rect = pymupdf.Rect(x0, y0, x0 + scaled_w, y0 + scaled_h)
            page.insert_image(target_rect, stream=jpeg_bytes)

            # 2. Insert invisible text layer for selection and search
            for line in ocr_res.lines:
                if not line.words:
                    continue
                # Calculate line bounding rect from words
                min_x = min(w.bounding_rect.x for w in line.words)
                min_y = min(w.bounding_rect.y for w in line.words)
                max_x = max(w.bounding_rect.x + w.bounding_rect.width for w in line.words)
                max_y = max(w.bounding_rect.y + w.bounding_rect.height for w in line.words)

                lx = x0 + min_x * scale
                ly = y0 + min_y * scale
                lw = (max_x - min_x) * scale
                lh = (max_y - min_y) * scale

                # insert text at baseline
                fontsize = max(7, lh * 0.8)
                baseline_y = ly + lh * 0.82
                page.insert_text(pymupdf.Point(lx, baseline_y), line.text, fontsize=fontsize, fontname="malgun", render_mode=3)

            print(f"Page {idx+1}: {len(ocr_res.lines)} lines of selectable text added.")

        pdf_doc.save(out_pdf, deflate=True)
        pdf_doc.close()

    # Verify selectable text
    doc_check = pymupdf.open(out_pdf)
    for pno in range(len(doc_check)):
        txt = doc_check[pno].get_text()
        print(f"Check Page {pno+1} text length: {len(txt)}, sample: {txt[:100].strip()}")
    doc_check.close()

if __name__ == "__main__":
    asyncio.run(test_chapter_1_searchable())
