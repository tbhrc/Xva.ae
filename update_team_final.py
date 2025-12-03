# Script to update Jan's photo and add David Potgieter
import re

# Read the file
with open('team.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Jan's photo
content = content.replace(
    'assets/images/Jan de Wachter.jpg',
    'assets/images/Jan de Wachter - Photo 02.png'
)

# 2. Find where to insert David (after Stephen Kruger's closing div)
# Find Stephen's section end
stephen_pattern = r'(<!-- Stephen Kruger -->.*?</div>\s*</div>)'
match = re.search(stephen_pattern, content, re.DOTALL)

if match:
    stephen_end = match.end()
    
    # David's HTML
    david_html = '''

                <!-- David Potgieter -->
                <div class="scroll-reveal delay-400" style="display: flex; gap: 2rem; align-items: start;">
                    <div style="flex-shrink: 0;">
                        <img src="assets/images/David Potgieter.jpg" alt="David Potgieter" 
                             style="width: 200px; height: 200px; border-radius: 50%; object-fit: cover; object-position: center; border: 4px solid var(--prem-border); box-shadow: 0 4px 12px rgba(0,0,0,0.1);">
                    </div>
                    <div>
                        <h3 style="font-size: 1.75rem; margin-bottom: 0.5rem;">David Potgieter</h3>
                        <div
                            style="color: var(--prem-accent-blue); font-size: 0.9rem; margin-bottom: 1rem; text-transform: uppercase; letter-spacing: 1px; font-weight: 600;">
                            Co-Founder & Certified AI Coach</div>
                        <p style="color: var(--prem-text-secondary); line-height: 1.7; margin-bottom: 1.5rem;">
                            Co-founder of iMPLEMENTAi.ae and Talent Bridge HR Consultancy. Certified AI Coach in Dubai since 2009 with over 24 years of business experience. Specializes in transforming companies and personal brands through strategic AI adoption.
                        </p>
                        <a href="https://www.linkedin.com/in/uaehr/" target="_blank"
                            class="prem-btn prem-btn-outline"
                            style="display: inline-flex; align-items: center; gap: 0.5rem;">
                            <svg width="16" height="16" fill="currentColor" viewBox="0 0 24 24">
                                <path
                                    d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z" />
                            </svg>
                            LinkedIn Profile
                        </a>
                    </div>
                </div>
'''
    
    # Insert David after Stephen
    content = content[:stephen_end] + david_html + content[stephen_end:]

# Write the updated content
with open('team.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ Team updates completed successfully!")
print("  - Updated Jan de Wachter's photo")
print("  - Added David Potgieter to the team")
