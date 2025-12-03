# Script to update team photos in team.html
import re

# Read the file
with open('team.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Define the replacements for each team member
replacements = [
    {
        'name': 'Jan de Wachter',
        'image': 'Jan de Wachter.jpg',
        'pattern': r'(<div class="scroll-reveal"[^>]*>\s*)<svg class="prem-team-photo"[^<]*(?:<[^>]*>[^<]*)*</svg>(\s*<div>\s*<h3[^>]*>Jan de Wachter</h3>)'
    },
    {
        'name': 'Ignatius (Natie) Rautenbach',
        'image': 'Ignatius (Natie) Rautenbach.jpg',
        'pattern': r'(<div class="scroll-reveal delay-100"[^>]*>\s*)<svg class="prem-team-photo"[^<]*(?:<[^>]*>[^<]*)*</svg>(\s*<div>\s*<h3[^>]*>Ignatius \(Natie\) Rautenbach</h3>)'
    },
    {
        'name': 'Christopher Booth',
        'image': 'Christopher Booth.jpg',
        'pattern': r'(<div class="scroll-reveal delay-200"[^>]*>\s*)<svg class="prem-team-photo"[^<]*(?:<[^>]*>[^<]*)*</svg>(\s*<div>\s*<h3[^>]*>Christopher Booth</h3>)'
    },
    {
        'name': 'Stephen Kruger',
        'image': 'Stephen Kruger.jpg',
        'pattern': r'(<div class="scroll-reveal delay-300"[^>]*>\s*)<svg class="prem-team-photo"[^<]*(?:<[^>]*>[^<]*)*</svg>(\s*<div>\s*<h3[^>]*>Stephen Kruger</h3>)'
    }
]

# Apply replacements
for repl in replacements:
    img_tag = f'''<div style="flex-shrink: 0;">
                        <img src="assets/images/{repl['image']}" alt="{repl['name']}" 
                             style="width: 200px; height: 200px; border-radius: 50%; object-fit: cover; object-position: center; border: 4px solid var(--prem-border); box-shadow: 0 4px 12px rgba(0,0,0,0.1);">
                    </div>'''
    
    content = re.sub(
        repl['pattern'],
        r'\1' + img_tag + r'\2',
        content,
        flags=re.DOTALL
    )

# Write the updated content
with open('team.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ Team photos updated successfully!")
print("Updated 4 team member photos:")
for repl in replacements:
    print(f"  - {repl['name']}")
