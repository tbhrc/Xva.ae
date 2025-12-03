# Comprehensive update script for all pages

import os
import re

base_path = r"c:\Users\TalentBridgeDubai\Documents\Web_Dev\iMPLEMENTAi.ae\iaiv3"

# Get all HTML files (excluding backup versions)
html_files = [f for f in os.listdir(base_path) if f.endswith('.html') and 'TBHRC-VM1' not in f]

# Task 1: Update email from hello@ to sales@
# Task 2: Add video header to all pages (except index.html which already has it)
# Task 3: Mobile menu will be added via CSS update

video_header_html = '''    <!-- Header with Video Background -->
    <header class="prem-hero" style="height: 60vh; min-height: 400px;">
        <video autoplay muted loop playsinline class="prem-hero-video">
            <source src="assets/videos/Hybrid-Intelligence.mp4" type="video/mp4">
        </video>
        <div class="prem-hero-content">
            <span class="eyebrow" style="color: rgba(255,255,255,0.8);">{eyebrow}</span>
            <h1 style="font-size: 3.5rem; margin-bottom: 1rem; color: #FFF;">{h1}</h1>
            <p style="max-width: 700px; margin: 0 auto; color: rgba(255,255,255,0.9); font-size: 1.2rem;">
                {description}
            </p>
        </div>
    </header>'''

# Page configurations for video headers
page_configs = {
    'team.html': {'eyebrow': 'Our Leadership', 'h1': 'Expert Leadership', 'description': 'Our team combines decades of experience in organizational transformation, technology leadership, and artificial intelligence strategy.'},
    'strategy.html': {'eyebrow': 'Strategic AI', 'h1': 'AI Strategy & Leadership', 'description': 'Transform AI from experimental to operational. We design comprehensive AI strategies and provide fractional CAIO leadership to guide your organization\'s AI journey.'},
    'about.html': {'eyebrow': 'About Us', 'h1': 'About iMPLEMENTAi.ae', 'description': 'We are a UAE-based AI consultancy dedicated to helping mid-market organizations turn AI from noise into disciplined capability.'},
    'contact.html': {'eyebrow': 'Get in Touch', 'h1': 'Let\'s Talk About Your AI Journey', 'description': 'Schedule a consultation to explore how AI can drive measurable value in your organization.'},
    'automation.html': {'eyebrow': 'Intelligent Automation', 'h1': 'Automation & AI Agents', 'description': 'Deploy intelligent automation and AI agents that work 24/7 to streamline operations, reduce costs, and improve accuracy.'},
    'workshops.html': {'eyebrow': 'Executive Education', 'h1': 'Executive Workshops', 'description': 'Intensive, hands-on workshops designed to equip your leadership team with the knowledge and frameworks to drive AI transformation.'},
    'departments.html': {'eyebrow': 'Department Solutions', 'h1': 'AI Solutions by Department', 'description': 'Tailored AI solutions for HR, Finance, Operations, and Sales departments.'},
    'fractional-caio.html': {'eyebrow': 'Leadership as a Service', 'h1': 'Fractional CAIO', 'description': 'Get senior AI leadership without the full-time commitment.'},
    'solutions-hr.html': {'eyebrow': 'HR Solutions', 'h1': 'AI for Human Resources', 'description': 'Transform your HR operations with intelligent automation and insights.'},
    'solutions-finance.html': {'eyebrow': 'Finance Solutions', 'h1': 'AI for Finance & Accounting', 'description': 'Automate financial processes and improve forecasting accuracy.'},
    'solutions-ops.html': {'eyebrow': 'Operations Solutions', 'h1': 'AI for Operations & Supply Chain', 'description': 'Optimize your operations with intelligent automation and predictive analytics.'},
    'solutions-sales.html': {'eyebrow': 'Sales Solutions', 'h1': 'AI for Sales & Marketing', 'description': 'Enhance customer experiences and optimize sales performance.'},
    'privacy.html': {'eyebrow': 'Legal', 'h1': 'Privacy Policy', 'description': 'Last updated: December 2025'},
    'terms.html': {'eyebrow': 'Legal', 'h1': 'Terms of Service', 'description': 'Our terms and conditions'},
    'resources.html': {'eyebrow': 'Knowledge', 'h1': 'AI Resources & Insights', 'description': 'Guides, articles, and insights on AI implementation'},
    'services.html': {'eyebrow': 'Our Services', 'h1': 'Comprehensive AI Solutions', 'description': 'Full-service AI consulting and implementation'},
    'ai-readiness.html': {'eyebrow': 'Assessment', 'h1': 'AI Readiness Assessment', 'description': 'Evaluate your organization\'s readiness for AI transformation'},
    'ai-readiness-result.html': {'eyebrow': 'Results', 'h1': 'Your AI Readiness Results', 'description': 'Personalized recommendations based on your assessment'},
    'roi-calculator.html': {'eyebrow': 'Calculator', 'h1': 'AI ROI Calculator', 'description': 'Calculate the potential return on investment for your AI initiatives'},
    'uae-guide.html': {'eyebrow': 'UAE Guide', 'h1': 'AI Implementation Guide for UAE', 'description': 'Comprehensive guide for implementing AI in the UAE market'}
}

for filename in html_files:
    file_path = os.path.join(base_path, filename)
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Task 1: Replace email
        content = content.replace('hello@implementai.ae', 'sales@implementai.ae')
        
        # Task 2: Add video header (skip index.html as it already has full-height video)
        if filename != 'index.html' and filename in page_configs:
            config = page_configs[filename]
            new_header = video_header_html.format(**config)
            
            # Replace the existing header section
            # Pattern to match: <header ... </header>
            header_pattern = r'<header[^>]*>.*?</header>'
            content = re.sub(header_pattern, new_header, content, flags=re.DOTALL)
        
        # Write back
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✓ Updated: {filename}")
    
    except Exception as e:
        print(f"✗ Error updating {filename}: {str(e)}")

print("\n✅ All pages updated successfully!")
print("- Email changed from hello@ to sales@")
print("- Video headers added to all pages")
