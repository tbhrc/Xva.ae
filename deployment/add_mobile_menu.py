# Script to add mobile menu to all pages

import os
import re

base_path = r"c:\Users\TalentBridgeDubai\Documents\Web_Dev\iMPLEMENTAi.ae\iaiv3"

# Get all HTML files (excluding backup versions)
html_files = [f for f in os.listdir(base_path) if f.endswith('.html') and 'TBHRC-VM1' not in f]

# Mobile menu HTML to insert after the Book Consultation button
mobile_menu_button = '''
            <button class="mobile-menu-toggle" id="mobileMenuToggle" aria-label="Toggle menu">
                <span></span>
                <span></span>
                <span></span>
            </button>'''

# Mobile menu overlay to insert before closing nav tag
mobile_menu_overlay = '''
    </nav>

    <!-- Mobile Menu Overlay -->
    <div class="mobile-menu-overlay" id="mobileMenuOverlay">
        <a href="index.html">Home</a>
        <a href="strategy.html">Strategy</a>
        <a href="departments.html">Solutions</a>
        <a href="team.html">Team</a>
        <a href="about.html">About</a>
        <a href="contact.html" class="prem-btn">Book Consultation</a>
    </div>

    <script>
        // Mobile menu toggle
        const mobileMenuToggle = document.getElementById('mobileMenuToggle');
        const mobileMenuOverlay = document.getElementById('mobileMenuOverlay');
        
        if (mobileMenuToggle) {
            mobileMenuToggle.addEventListener('click', function() {
                this.classList.toggle('active');
                mobileMenuOverlay.classList.toggle('active');
                document.body.style.overflow = mobileMenuOverlay.classList.contains('active') ? 'hidden' : '';
            });

            // Close menu when clicking on a link
            mobileMenuOverlay.querySelectorAll('a').forEach(link => {
                link.addEventListener('click', function() {
                    mobileMenuToggle.classList.remove('active');
                    mobileMenuOverlay.classList.remove('active');
                    document.body.style.overflow = '';
                });
            });
        }
    </script>'''

for filename in html_files:
    file_path = os.path.join(base_path, filename)
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if mobile menu already exists
        if 'mobile-menu-toggle' in content:
            print(f"⊙ Mobile menu already in: {filename}")
            continue
        
        # Add mobile menu button after the Book Consultation button
        content = re.sub(
            r'(<a href="contact\.html" class="prem-btn">Book Consultation</a>)',
            r'\1' + mobile_menu_button,
            content
        )
        
        # Replace </nav> with mobile menu overlay
        content = content.replace('</nav>', mobile_menu_overlay)
        
        # Write back
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✓ Added mobile menu to: {filename}")
    
    except Exception as e:
        print(f"✗ Error updating {filename}: {str(e)}")

print("\n✅ Mobile menu added to all pages!")
print("- Hamburger button appears on screens < 768px")
print("- Full-screen overlay menu with smooth animations")
print("- Auto-closes when link is clicked")
