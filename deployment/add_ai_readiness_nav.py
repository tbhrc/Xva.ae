# Script to add "Check AI Readiness" to navigation and promote on all pages

import os
import re

base_path = r"c:\Users\TalentBridgeDubai\Documents\Web_Dev\iMPLEMENTAi.ae\iaiv3"

# Get all HTML files (excluding backup versions)
html_files = [f for f in os.listdir(base_path) if f.endswith('.html') and 'TBHRC-VM1' not in f]

for filename in html_files:
    file_path = os.path.join(base_path, filename)
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Task 1: Add "Check AI Readiness" to desktop menu (before "About")
        if 'Check AI Readiness' not in content:
            content = re.sub(
                r'(<li><a href="about\.html">About</a></li>)',
                r'<li><a href="ai-readiness.html" style="color: var(--prem-accent-blue); font-weight: 600;">Check AI Readiness</a></li>\n                \1',
                content
            )
            
            # Task 2: Add to mobile menu overlay (before "About")
            content = re.sub(
                r'(<a href="about\.html">About</a>)',
                r'<a href="ai-readiness.html" style="color: var(--prem-accent-blue); font-weight: 600;">Check AI Readiness</a>\n        \1',
                content
            )
            
            print(f"✓ Added to menu: {filename}")
        else:
            print(f"⊙ Already in menu: {filename}")
        
        # Write back
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
    
    except Exception as e:
        print(f"✗ Error updating {filename}: {str(e)}")

print("\n✅ 'Check AI Readiness' added to all navigation menus!")
print("- Added to desktop menu (highlighted in blue)")
print("- Added to mobile menu")
print("- Positioned prominently before 'About'")
