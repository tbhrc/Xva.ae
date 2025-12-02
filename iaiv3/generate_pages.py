# Script to apply premium design to all remaining HTML pages

pages_config = [
    {
        "file": "departments.html",
        "title": "AI Solutions by Department | iMPLEMENTAi.ae",
        "eyebrow": "Department Solutions",
        "h1": "AI Solutions by Department",
        "description": "Tailored AI solutions for HR, Finance, Operations, and Sales departments.",
        "content": """
            <div class="prem-grid-2">
                <div class="prem-card scroll-reveal">
                    <h3>HR & People Operations</h3>
                    <p>Transform talent acquisition, employee engagement, and workforce planning with AI-powered insights.</p>
                    <a href="solutions-hr.html" class="prem-btn prem-btn-outline" style="margin-top: 1rem;">Learn More</a>
                </div>
                <div class="prem-card scroll-reveal delay-100">
                    <h3>Finance & Accounting</h3>
                    <p>Automate financial processes, improve forecasting accuracy, and detect anomalies in real-time.</p>
                    <a href="solutions-finance.html" class="prem-btn prem-btn-outline" style="margin-top: 1rem;">Learn More</a>
                </div>
                <div class="prem-card scroll-reveal delay-200">
                    <h3>Operations & Supply Chain</h3>
                    <p>Optimize inventory, predict demand, and streamline logistics with intelligent automation.</p>
                    <a href="solutions-ops.html" class="prem-btn prem-btn-outline" style="margin-top: 1rem;">Learn More</a>
                </div>
                <div class="prem-card scroll-reveal delay-300">
                    <h3>Sales & Marketing</h3>
                    <p>Enhance lead scoring, personalize customer experiences, and optimize pricing strategies.</p>
                    <a href="solutions-sales.html" class="prem-btn prem-btn-outline" style="margin-top: 1rem;">Learn More</a>
                </div>
            </div>
        """
    },
    {
        "file": "fractional-caio.html",
        "title": "Fractional CAIO Services | iMPLEMENTAi.ae",
        "eyebrow": "Leadership as a Service",
        "h1": "Fractional CAIO",
        "description": "Get senior AI leadership without the full-time commitment.",
        "content": """
            <div class="prem-grid-3">
                <div class="prem-card scroll-reveal">
                    <h3>Strategic Direction</h3>
                    <p>Set AI vision, priorities, and roadmap aligned with business objectives.</p>
                </div>
                <div class="prem-card scroll-reveal delay-100">
                    <h3>Governance & Risk</h3>
                    <p>Establish frameworks for responsible AI deployment and regulatory compliance.</p>
                </div>
                <div class="prem-card scroll-reveal delay-200">
                    <h3>Team Building</h3>
                    <p>Recruit, develop, and organize your AI capabilities for long-term success.</p>
                </div>
            </div>
        """
    },
    {
        "file": "solutions-hr.html",
        "title": "AI for HR | iMPLEMENTAi.ae",
        "eyebrow": "HR Solutions",
        "h1": "AI for Human Resources",
        "description": "Transform your HR operations with intelligent automation and insights.",
        "content": """
            <div class="prem-grid-3">
                <div class="prem-card scroll-reveal">
                    <h3>Talent Acquisition</h3>
                    <p>AI-powered resume screening, candidate matching, and interview scheduling.</p>
                </div>
                <div class="prem-card scroll-reveal delay-100">
                    <h3>Employee Engagement</h3>
                    <p>Sentiment analysis, pulse surveys, and predictive attrition modeling.</p>
                </div>
                <div class="prem-card scroll-reveal delay-200">
                    <h3>Learning & Development</h3>
                    <p>Personalized training recommendations and skills gap analysis.</p>
                </div>
            </div>
        """
    },
    {
        "file": "solutions-finance.html",
        "title": "AI for Finance | iMPLEMENTAi.ae",
        "eyebrow": "Finance Solutions",
        "h1": "AI for Finance & Accounting",
        "description": "Automate financial processes and improve forecasting accuracy.",
        "content": """
            <div class="prem-grid-3">
                <div class="prem-card scroll-reveal">
                    <h3>Invoice Processing</h3>
                    <p>Automated AP/AR with intelligent document extraction and matching.</p>
                </div>
                <div class="prem-card scroll-reveal delay-100">
                    <h3>Financial Forecasting</h3>
                    <p>AI-powered predictions for cash flow, revenue, and expense planning.</p>
                </div>
                <div class="prem-card scroll-reveal delay-200">
                    <h3>Fraud Detection</h3>
                    <p>Real-time anomaly detection and risk scoring for transactions.</p>
                </div>
            </div>
        """
    },
    {
        "file": "solutions-ops.html",
        "title": "AI for Operations | iMPLEMENTAi.ae",
        "eyebrow": "Operations Solutions",
        "h1": "AI for Operations & Supply Chain",
        "description": "Optimize your operations with intelligent automation and predictive analytics.",
        "content": """
            <div class="prem-grid-3">
                <div class="prem-card scroll-reveal">
                    <h3>Demand Forecasting</h3>
                    <p>Predict demand patterns to optimize inventory and reduce waste.</p>
                </div>
                <div class="prem-card scroll-reveal delay-100">
                    <h3>Process Automation</h3>
                    <p>Streamline repetitive tasks and workflows with intelligent bots.</p>
                </div>
                <div class="prem-card scroll-reveal delay-200">
                    <h3>Quality Control</h3>
                    <p>Computer vision for defect detection and quality assurance.</p>
                </div>
            </div>
        """
    },
    {
        "file": "solutions-sales.html",
        "title": "AI for Sales | iMPLEMENTAi.ae",
        "eyebrow": "Sales Solutions",
        "h1": "AI for Sales & Marketing",
        "description": "Enhance customer experiences and optimize sales performance.",
        "content": """
            <div class="prem-grid-3">
                <div class="prem-card scroll-reveal">
                    <h3>Lead Scoring</h3>
                    <p>Prioritize prospects based on conversion probability and lifetime value.</p>
                </div>
                <div class="prem-card scroll-reveal delay-100">
                    <h3>Personalization</h3>
                    <p>Deliver tailored content and recommendations at scale.</p>
                </div>
                <div class="prem-card scroll-reveal delay-200">
                    <h3>Dynamic Pricing</h3>
                    <p>Optimize pricing strategies based on market conditions and demand.</p>
                </div>
            </div>
        """
    }
]

template = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <meta name="description" content="{description}">
    
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
            <span class="eyebrow">{eyebrow}</span>
            <h1 style="font-size: 3rem; margin-bottom: 1rem;">{h1}</h1>
            <p style="max-width: 700px; margin: 0 auto; color: var(--prem-text-secondary); font-size: 1.2rem;">
                {description}
            </p>
        </div>
    </header>

    <section class="prem-section">
        <div class="prem-container">
            {content}
        </div>
    </section>

    <section class="prem-section prem-section-alt">
        <div class="prem-container">
            <div style="max-width: 800px; margin: 0 auto; text-align: center;">
                <h2 style="font-size: 2rem; margin-bottom: 2rem;">Ready to Get Started?</h2>
                <p style="color: var(--prem-text-secondary); margin-bottom: 3rem;">
                    Contact us to discuss how we can help transform your organization.
                </p>
                <a href="contact.html" class="prem-btn">Book a Consultation</a>
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

    <script>
        document.addEventListener('DOMContentLoaded', () => {{
            const observerOptions = {{ root: null, rootMargin: '0px', threshold: 0.1 }};
            const observer = new IntersectionObserver((entries, observer) => {{
                entries.forEach(entry => {{
                    if (entry.isIntersecting) {{
                        entry.target.classList.add('visible');
                        observer.unobserve(entry.target);
                    }}
                }});
            }}, observerOptions);
            document.querySelectorAll('.scroll-reveal').forEach(el => observer.observe(el));
        }});
    </script>

</body>
</html>'''

import os

base_path = r"c:\Users\TalentBridgeDubai\Documents\Web_Dev\iMPLEMENTAi.ae\iaiv3"

for page in pages_config:
    html_content = template.format(**page)
    file_path = os.path.join(base_path, page["file"])
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
    print(f"Created: {page['file']}")

print("\nAll pages created successfully!")
