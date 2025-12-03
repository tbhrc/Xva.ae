# Script to update logo from logo.png to 2.png across all pages

import os
import re

base_path = r"c:\Users\TalentBridgeDubai\Documents\Web_Dev\iMPLEMENTAi.ae\iaiv3"

# Get all HTML files (excluding backup versions)
html_files = [f for f in os.listdir(base_path) if f.endswith('.html') and 'TBHRC-VM1' not in f]

# New logo HTML with optimized sizing
new_logo_html = '<img src="assets/images/2.png" alt="iMPLEMENTAi.ae" style="height: 45px; width: auto;">'

for filename in html_files:
    file_path = os.path.join(base_path, filename)
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace old logo.png references with 2.png
        content = content.replace('assets/images/logo.png', 'assets/images/2.png')
        
        # Also update the height to 45px for better visibility
        content = re.sub(
            r'<img src="assets/images/2\.png" alt="iMPLEMENTAi\.ae" style="height: 40px; width: auto;">',
            new_logo_html,
            content
        )
        
        # Write back
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✓ Updated logo in: {filename}")
    
    except Exception as e:
        print(f"✗ Error updating {filename}: {str(e)}")

print("\n✅ Logo updated to 2.png across all pages!")
print("- New logo: assets/images/2.png")
print("- Height: 45px (optimized for visibility)")
print("- Transparent background maintained")
