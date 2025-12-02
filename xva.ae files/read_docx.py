import zipfile
import re
import sys
import os

filename = "ImplementAI.ae – Website SEO Blueprint.docx"
try:
    with zipfile.ZipFile(filename) as z:
        xml_content = z.read('word/document.xml').decode('utf-8')
        text = re.sub('<[^>]+>', ' ', xml_content)
        print(text)
except Exception as e:
    print(f"Error: {e}")
