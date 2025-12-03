# Script to remove duplicate "Check AI Readiness" menu items

import os
import re

base_path = r"c:\Users\TalentBridgeDubai\Documents\Web_Dev\iMPLEMENTAi.ae\iaiv3"

# Get all HTML files
html_files = [f for f in os.listdir(base_path) if f.endswith('.html') and 'TBHRC-VM1' not in f]

for filename in html_files:
    file_path = os.path.join(base_path, filename)
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Pattern 1: Remove duplicate in desktop menu (consecutive li tags)
        # Keep only the first occurrence within <li></li>
        pattern1 = r'(\s*<li><a href="ai-readiness\.html"[^>]*>Check AI Readiness</a></li>)\s*<li><a href="ai-readiness\.html"[^>]*>Check AI Readiness</a>\s*<a href="about\.html">About</a></li>'
        replacement1 = r'\1\n                <li><a href="about.html">About</a></li>'
        content = re.sub(pattern1, replacement1, content)
        
        # Pattern 2: Remove standalone duplicate before About link (in mobile menu or malformed desktop menu)
        pattern2 = r'<li><a href="ai-readiness\.html"[^>]*>Check AI Readiness</a>\s*<a href="about\.html">'
        replacement2 = r'<li><a href="about.html">'
        content = re.sub(pattern2, replacement2, content)
        
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✓ Fixed duplicates in: {filename}")
        else:
            print(f"⊙ No duplicates found in: {filename}")
    
    except Exception as e:
        print(f"✗ Error processing {filename}: {str(e)}")

print("\n✅ Duplicate menu items removed!")
