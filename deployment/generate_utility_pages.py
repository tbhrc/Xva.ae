# Generate remaining utility pages

pages = {
    "terms.html": {
        "title": "Terms of Service | iMPLEMENTAi.ae",
        "h1": "Terms of Service",
        "content": "Terms of service content will be added here."
    },
    "resources.html": {
        "title": "Resources | iMPLEMENTAi.ae",
        "h1": "AI Resources & Insights",
        "content": "Resources and insights content will be added here."
    },
    "services.html": {
        "title": "Our Services | iMPLEMENTAi.ae",
        "h1": "Our Services",
        "content": "Comprehensive overview of our AI consulting services."
    },
    "ai-readiness.html": {
        "title": "AI Readiness Assessment | iMPLEMENTAi.ae",
        "h1": "AI Readiness Assessment",
        "content": "Assess your organization's readiness for AI transformation."
    },
    "ai-readiness-result.html": {
        "title": "Assessment Results | iMPLEMENTAi.ae",
        "h1": "Your AI Readiness Results",
        "content": "Results from your AI readiness assessment."
    },
    "roi-calculator.html": {
        "title": "ROI Calculator | iMPLEMENTAi.ae",
        "h1": "AI ROI Calculator",
        "content": "Calculate the potential return on investment for your AI initiatives."
    },
    "uae-guide.html": {
        "title": "UAE AI Guide | iMPLEMENTAi.ae",
        "h1": "AI Implementation Guide for UAE Organizations",
        "content": "Comprehensive guide for implementing AI in the UAE market."
    }
}

template = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="assets/css/v7.3-premium.css">
</head>
<body>

    <nav class="prem-nav">
        <div class="prem-container prem-nav-inner">
            <a href="index.html" class="prem-logo">iMPLEMENTAi.ae</a>
            <ul class="prem-menu">
                <li><a href="index.html">Home</a></li>
                <li><a href="strategy.html">Strategy</a></li>
                <li><a href="departments.html">Solutions</a></li>
                <li><a href="team.html">Team</a></li>
                <li><a href="about.html">About</a></li>
            </ul>
            <a href="contact.html" class="prem-btn">Book Consultation</a>
        </div>
    </nav>

    <header class="prem-section" style="padding-top: 150px; padding-bottom: 50px; text-align: center;">
        <div class="prem-container">
            <h1 style="font-size: 3rem; margin-bottom: 1rem;">{h1}</h1>
        </div>
    </header>

    <section class="prem-section">
        <div class="prem-container">
            <div style="max-width: 800px; margin: 0 auto;">
                <div class="prem-card">
                    <p>{content}</p>
                </div>
            </div>
        </div>
    </section>

    <footer class="prem-footer">
        <div class="prem-container">
            <div class="prem-footer-grid">
                <div>
                    <a href="index.html" class="prem-logo" style="margin-bottom: 1.5rem; display: block;">iMPLEMENTAi.ae</a>
                    <p style="color: var(--prem-text-secondary); max-width: 300px;">
                        The premier AI consultancy for the UAE mid-market. Bridging the gap between technology and business value.
                    </p>
                </div>
                <div>
                    <h4>Services</h4>
                    <a href="strategy.html">AI Strategy</a>
                    <a href="automation.html">Automation & Agents</a>
                    <a href="fractional-caio.html">Fractional CAIO</a>
                    <a href="workshops.html">Workshops</a>
                </div>
                <div>
                    <h4>Company</h4>
                    <a href="about.html">About Us</a>
                    <a href="team.html">Our Team</a>
                    <a href="contact.html">Contact</a>
                    <a href="privacy.html">Privacy Policy</a>
                </div>
                <div>
                    <h4>Connect</h4>
                    <a href="https://www.linkedin.com/company/implementai-ae">LinkedIn</a>
                    <a href="mailto:hello@implementai.ae">Email Us</a>
                </div>
            </div>
            <div style="border-top: 1px solid var(--prem-border); padding-top: 2rem; text-align: center; color: var(--prem-text-secondary); font-size: 0.85rem;">
                &copy; 2025 iMPLEMENTAi.ae. All rights reserved.
            </div>
        </div>
    </footer>

</body>
</html>'''

import os

base_path = r"c:\Users\TalentBridgeDubai\Documents\Web_Dev\iMPLEMENTAi.ae\iaiv3"

for filename, data in pages.items():
    html_content = template.format(**data)
    file_path = os.path.join(base_path, filename)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
    print(f"Created: {filename}")

print("\nAll utility pages created successfully!")
