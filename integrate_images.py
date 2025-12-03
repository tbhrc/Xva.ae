# Script to integrate logo and framework images across the website

import os
import re

base_path = r"c:\Users\TalentBridgeDubai\Documents\Web_Dev\iMPLEMENTAi.ae\iaiv3"

# Get all HTML files (excluding backup versions)
html_files = [f for f in os.listdir(base_path) if f.endswith('.html') and 'TBHRC-VM1' not in f]

# Task 1: Replace text logo with image logo in navigation
logo_html = '<img src="assets/images/logo.png" alt="iMPLEMENTAi.ae" style="height: 40px; width: auto;">'

for filename in html_files:
    file_path = os.path.join(base_path, filename)
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace text logo with image logo
        # Pattern: <a href="index.html" class="prem-logo">iMPLEMENTAi.ae</a>
        content = re.sub(
            r'<a href="index\.html" class="prem-logo">iMPLEMENT<span>Ai</span>\.ae</a>',
            f'<a href="index.html" class="prem-logo">{logo_html}</a>',
            content
        )
        content = re.sub(
            r'<a href="index\.html" class="prem-logo">iMPLEMENTAi\.ae</a>',
            f'<a href="index.html" class="prem-logo">{logo_html}</a>',
            content
        )
        
        # Also update footer logo
        content = re.sub(
            r'<a href="index\.html" class="prem-logo" style="margin-bottom: 1\.5rem; display: block;">iMPLEMENT<span>Ai</span>\.ae</a>',
            f'<a href="index.html" class="prem-logo" style="margin-bottom: 1.5rem; display: block;">{logo_html}</a>',
            content
        )
        content = re.sub(
            r'<a href="index\.html" class="prem-logo" style="margin-bottom: 1\.5rem; display: block;">iMPLEMENTAi\.ae</a>',
            f'<a href="index.html" class="prem-logo" style="margin-bottom: 1.5rem; display: block;">{logo_html}</a>',
            content
        )
        
        # Write back
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✓ Updated logo in: {filename}")
    
    except Exception as e:
        print(f"✗ Error updating {filename}: {str(e)}")

print("\n✅ Logo integration complete!")

# Task 2: Add framework images to specific pages
framework_integrations = {
    'index.html': {
        'image': 'framework-flower.png',
        'section': 'Human + AI Philosophy',
        'insert_after': '<h2 class="section-title scroll-reveal" style="max-width: 800px; margin: 0 auto 3rem;">The "Human + AI" Hybrid Model</h2>',
        'html': '''
            <div style="text-align: center; margin-bottom: 3rem;">
                <img src="assets/images/framework-flower.png" alt="Human + AI Framework" style="max-width: 400px; width: 100%; height: auto; opacity: 0.9;">
            </div>
        '''
    },
    'strategy.html': {
        'image': 'framework-capability.png',
        'section': 'AI Capability Framework',
        'insert_after': '<h2 style="font-size: 2rem; margin-bottom: 2rem; text-align: center;">Strategic AI Roadmapping</h2>',
        'html': '''
            <div style="text-align: center; margin-bottom: 3rem;">
                <img src="assets/images/framework-capability.png" alt="AI Capability Framework" style="max-width: 600px; width: 100%; height: auto; opacity: 0.95;">
            </div>
        '''
    },
    'departments.html': {
        'image': 'framework-org.png',
        'section': 'Organizational Framework',
        'insert_after': '<h1 style="font-size: 3rem; margin-bottom: 1rem;">AI Solutions by Department</h1>',
        'html': '''
            <div style="text-align: center; margin-top: 2rem;">
                <img src="assets/images/framework-org.png" alt="Organizational AI Framework" style="max-width: 500px; width: 100%; height: auto; opacity: 0.9;">
            </div>
        '''
    }
}

for filename, config in framework_integrations.items():
    file_path = os.path.join(base_path, filename)
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if image is already inserted
        if config['image'] not in content:
            # Insert the framework image
            content = content.replace(
                config['insert_after'],
                config['insert_after'] + config['html']
            )
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print(f"✓ Added {config['image']} to: {filename}")
        else:
            print(f"⊙ {config['image']} already in: {filename}")
    
    except Exception as e:
        print(f"✗ Error adding framework to {filename}: {str(e)}")

print("\n✅ All images integrated successfully!")
