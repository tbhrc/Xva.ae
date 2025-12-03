import os
import re

directory = r'c:\Users\TalentBridgeDubai\Documents\Web_Dev\iMPLEMENTAi.ae\iaiv3'

logo_html = '<img src="assets/images/logo.png" alt="iMPLEMENTAi Logo" class="w-10 h-10 object-contain">'

pattern = re.compile(r'<div\s+class="w-9 h-9 rounded-2xl bg-gradient-to-br from-teal-500 to-cyan-600 flex items-center justify-center shadow-brand-glow">\s*<span class="text-white font-semibold text-lg">IA</span>\s*</div>', re.DOTALL)

for filename in os.listdir(directory):
    if filename.endswith(".html"):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        new_content = pattern.sub(logo_html, content)
        
        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {filename}")
