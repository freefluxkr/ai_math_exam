# -*- coding: utf-8 -*-
import os
import glob
import io
import zipfile
import xml.etree.ElementTree as ET
from PIL import Image
import pymupdf

BASE_DIR = r"C:\Users\PC\Downloads\DOIT_안티그레비티 도서내용 및 강의자료\DOIT_안티그레비티 도서내용 및 강의자료"

# Clean up temp test files
for temp_name in ["test_ch1.html", "test_ch1.pdf", "test_perfect_ch1.pdf", "preview_ch1_p1.png"]:
    temp_path = os.path.join(BASE_DIR, temp_name)
    if os.path.exists(temp_path):
        os.remove(temp_path)

docx_files = sorted(glob.glob(os.path.join(BASE_DIR, "*.docx")))
print(f"Found {len(docx_files)} docx files to convert to PDF.")

total_pages_all = 0

for docx_path in docx_files:
    filename = os.path.basename(docx_path)
    base_name = os.path.splitext(filename)[0]
    out_pdf_path = os.path.join(BASE_DIR, f"{base_name}.pdf")

    print(f"\n[Processing] {filename}...")

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

        print(f"  -> Extracted {len(img_targets)} pages/images in exact document order.")

        pdf_doc = pymupdf.open()
        A4_W, A4_H = 595.28, 841.89  # A4 in points

        for idx, target in enumerate(img_targets):
            img_bytes = z.read(target)
            pil_img = Image.open(io.BytesIO(img_bytes))

            # Convert to RGB JPEG (95 quality) for crisp visual reproduction and compact PDF size
            buf = io.BytesIO()
            if pil_img.mode != "RGB":
                pil_img = pil_img.convert("RGB")
            pil_img.save(buf, format="JPEG", quality=95, optimize=True)
            jpeg_bytes = buf.getvalue()

            img_w, img_h = pil_img.size
            scale = min(A4_W / img_w, A4_H / img_h)
            scaled_w = img_w * scale
            scaled_h = img_h * scale
            x0 = (A4_W - scaled_w) / 2
            y0 = (A4_H - scaled_h) / 2

            page = pdf_doc.new_page(width=A4_W, height=A4_H)
            target_rect = pymupdf.Rect(x0, y0, x0 + scaled_w, y0 + scaled_h)
            page.insert_image(target_rect, stream=jpeg_bytes)

        pdf_doc.save(out_pdf_path, deflate=True)
        pdf_doc.close()

        file_size_mb = os.path.getsize(out_pdf_path) / (1024 * 1024)
        print(f"  -> Successfully generated: {os.path.basename(out_pdf_path)} ({len(img_targets)} pages, {file_size_mb:.2f} MB)")
        total_pages_all += len(img_targets)

print(f"\nAll {len(docx_files)} docx documents successfully converted! Total pages: {total_pages_all}")

