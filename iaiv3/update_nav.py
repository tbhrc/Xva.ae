import os
import re

# The correct navigation HTML template
NAV_TEMPLATE = """  <!-- Navigation -->
  <nav class="prem-nav">
    <div class="prem-container prem-nav-inner">
      <a href="index.html" class="prem-logo"><img src="assets/images/2.png" alt="iMPLEMENTAi.ae"
          style="height: 45px; width: auto;"></a>
      <ul class="prem-menu">
        <li><a href="index.html"{home_style}>Home</a></li>
        <li><a href="strategy.html"{strategy_style}>Strategy</a></li>
        <li><a href="departments.html"{solutions_style}>Solutions</a></li>
        <li><a href="resources.html"{insights_style}>Insights</a></li>
        <li><a href="team.html"{team_style}>Team</a></li>
        <li><a href="ai-readiness.html"{readiness_style}>Check AI Readiness</a></li>
        <li><a href="about.html"{about_style}>About</a></li>
      </ul>
      <a href="contact.html" class="prem-btn">Book Consultation</a>
      <button class="mobile-menu-toggle" id="mobileMenuToggle" aria-label="Toggle menu">
        <span></span>
        <span></span>
        <span></span>
      </button>
    </div>
  </nav>

  <!-- Mobile Menu Overlay -->
  <div class="mobile-menu-overlay" id="mobileMenuOverlay">
    <a href="index.html">Home</a>
    <a href="strategy.html">Strategy</a>
    <a href="departments.html">Solutions</a>
    <a href="resources.html">Insights</a>
    <a href="team.html">Team</a>
    <a href="ai-readiness.html">Check AI Readiness</a>
    <a href="about.html">About</a>
    <a href="contact.html" class="prem-btn" style="background: var(--prem-accent-blue); border-color: var(--prem-accent-blue);">Book Consultation</a>
  </div>"""

# Active style string
ACTIVE_STYLE = ' style="color: var(--prem-text);"'

# Mapping of filename to the active style placeholder key
FILE_MAPPING = {
    'index.html': 'home_style',
    'strategy.html': 'strategy_style',
    'departments.html': 'solutions_style',
    'solutions-hr.html': 'solutions_style',
    'solutions-finance.html': 'solutions_style',
    'solutions-ops.html': 'solutions_style',
    'solutions-sales.html': 'solutions_style',
    'resources.html': 'insights_style',
    'team.html': 'team_style',
    'ai-readiness.html': 'readiness_style',
    'about.html': 'about_style',
    'contact.html': '',
    'automation.html': 'strategy_style',
    'fractional-caio.html': 'strategy_style',
    'workshops.html': 'strategy_style',
    'privacy.html': '',
    'terms.html': ''
}

# Updated Regex to be more flexible
# Matches optional "<!-- Navigation -->", then "<nav class="prem-nav">", content, "<!-- Mobile Menu Overlay -->", content, "</div>", then optional whitespace and "<script>"
REGEX_PATTERN = r'(?:<!-- Navigation -->\s*)?(<nav class="prem-nav">.*?<!-- Mobile Menu Overlay -->.*?</div>)(\s*<script>)'

def update_file(filename):
    if not os.path.exists(filename):
        print(f"Skipping {filename} (not found)")
        return

    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Determine active style
    active_key = FILE_MAPPING.get(filename, '')
    
    # Prepare the new nav HTML
    format_args = {
        'home_style': '',
        'strategy_style': '',
        'solutions_style': '',
        'insights_style': '',
        'team_style': '',
        'readiness_style': '',
        'about_style': ''
    }
    
    if active_key in format_args:
        format_args[active_key] = ACTIVE_STYLE
        
    new_nav = NAV_TEMPLATE.format(**format_args)
    
    # Perform replacement
    # We use re.DOTALL to match across lines
    # We replace the captured group 1 (the old nav block) with the new nav block
    # We keep group 2 (the script tag)
    # The optional comment at the start is consumed by the match but not in group 1 or 2, so it gets replaced by the new nav which includes the comment.
    
    # Note: The regex matches the whole block including the optional comment.
    # So we replace the whole match with new_nav + group 2.
    
    # Wait, re.sub replaces the *whole match*.
    # My regex is: (optional comment)(nav...div)(script)
    # So group 1 is nav...div
    # Group 2 is script
    # The optional comment is part of the match (group 0) but not group 1.
    
    # So if I replace with new_nav + r'\2', I am replacing the whole match (comment + nav + script) with (new_nav + script).
    # This is correct.
    
    new_content = re.sub(REGEX_PATTERN, f'{new_nav}\\2', content, flags=re.DOTALL)
    
    if new_content != content:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filename}")
    else:
        print(f"No changes needed for {filename} (or pattern not found)")

# List of files to update
files_to_update = [
    'about.html',
    'strategy.html',
    'departments.html',
    'team.html',
    'ai-readiness.html',
    'contact.html',
    'resources.html',
    'privacy.html',
    'terms.html',
    'automation.html',
    'fractional-caio.html',
    'workshops.html',
    'solutions-hr.html',
    'solutions-finance.html',
    'solutions-ops.html',
    'solutions-sales.html'
]

for filename in files_to_update:
    update_file(filename)
