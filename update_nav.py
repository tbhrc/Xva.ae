import os
import re

ROOT_PREFIX = '/'

NAV_ITEMS = [
    {"label": "Home", "href": f"{ROOT_PREFIX}index.html", "key": "home_style"},
    {"label": "Strategy", "href": f"{ROOT_PREFIX}strategy.html", "key": "strategy_style"},
    {"label": "Solutions", "href": f"{ROOT_PREFIX}departments.html", "key": "solutions_style"},
    {"label": "Insights", "href": f"{ROOT_PREFIX}resources.html", "key": "insights_style"},
    {"label": "Blog", "href": f"{ROOT_PREFIX}blog.html", "key": "blog_style"},
    {"label": "Team", "href": f"{ROOT_PREFIX}team.html", "key": "team_style"},
    {"label": "AI Experts Hub", "href": f"{ROOT_PREFIX}ai-experts/index.html", "key": "experts_style"},
    {"label": "Check AI Readiness", "href": f"{ROOT_PREFIX}ai-readiness.html", "key": "readiness_style"},
    {"label": "About", "href": f"{ROOT_PREFIX}about.html", "key": "about_style"},
]

ACTIVE_STYLE = ' style="color: var(--prem-text);"'

FILE_MAPPING = {
    'index.html': 'home_style',
    'strategy.html': 'strategy_style',
    'departments.html': 'solutions_style',
    'solutions-hr.html': 'solutions_style',
    'solutions-finance.html': 'solutions_style',
    'solutions-ops.html': 'solutions_style',
    'solutions-sales.html': 'solutions_style',
    'resources.html': 'insights_style',
    'blog.html': 'blog_style',
    'team.html': 'team_style',
    'ai-readiness.html': 'readiness_style',
    'about.html': 'about_style',
    'contact.html': '',
    'automation.html': 'strategy_style',
    'fractional-caio.html': 'strategy_style',
    'workshops.html': 'strategy_style',
    'privacy.html': '',
    'terms.html': '',
    'ai-experts/index.html': 'experts_style',
    'ai-experts/apply.html': 'experts_style',
}

NAV_PATTERN = re.compile(r'(?:<!-- Navigation -->\s*)?<nav class="prem-nav">.*?<!-- Mobile Menu Overlay -->.*?</div>', re.DOTALL)
FOOTER_PATTERN = re.compile(r'<footer class="prem-footer">.*?</footer>', re.DOTALL)


def build_nav_html(active_key: str) -> str:
    nav_links = []
    overlay_links = []
    for item in NAV_ITEMS:
        style = ACTIVE_STYLE if active_key == item.get("key") else ''
        nav_links.append(f'        <li><a href="{item["href"]}"{style}>{item["label"]}</a></li>')
        overlay_links.append(f'    <a href="{item["href"]}">{item["label"]}</a>')

    nav_block = "\n".join(nav_links)
    overlay_block = "\n".join(overlay_links)

    return f"""  <!-- Navigation -->
  <nav class=\"prem-nav\">
    <div class=\"prem-container prem-nav-inner\">
      <a href=\"{ROOT_PREFIX}index.html\" class=\"prem-logo\"><img src=\"{ROOT_PREFIX}assets/images/2.png\" alt=\"iMPLEMENTAi.ae\" style=\"height: 45px; width: auto;\"></a>
      <ul class=\"prem-menu\">
{nav_block}
      </ul>
      <a href=\"{ROOT_PREFIX}contact.html\" class=\"prem-btn\">Book Consultation</a>
      <button class=\"mobile-menu-toggle\" id=\"mobile-menu-toggle\" aria-label=\"Toggle menu\">
        <span></span>
        <span></span>
        <span></span>
      </button>
    </div>
  </nav>

  <!-- Mobile Menu Overlay -->
  <div class=\"mobile-menu-overlay\" id=\"mobile-menu\">
{overlay_block}
    <a href=\"{ROOT_PREFIX}contact.html\" class=\"prem-btn\" style=\"background: var(--prem-accent-blue); border-color: var(--prem-accent-blue);\">Book Consultation</a>
  </div>"""


def build_footer_html() -> str:
    explore_links = "\n          ".join([f'<a href="{item["href"]}">{item["label"]}</a>' for item in NAV_ITEMS])
    return f"""<footer class=\"prem-footer\">
    <div class=\"prem-container\">
      <div class=\"prem-footer-grid\">
        <div>
          <a href=\"{ROOT_PREFIX}index.html\" class=\"prem-logo\" style=\"margin-bottom: 1.5rem; display: block;\"><img
              src=\"{ROOT_PREFIX}assets/images/2.png\" alt=\"iMPLEMENTAi.ae\" style=\"height: 45px; width: auto;\"></a>
          <p style=\"color: var(--prem-text-secondary); max-width: 300px;\">
            The premier AI consultancy for the UAE mid-market. Bridging the gap between technology and business value.
          </p>
        </div>
        <div>
          <h4>Services</h4>
          <a href=\"{ROOT_PREFIX}strategy.html\">AI Strategy</a>
          <a href=\"{ROOT_PREFIX}automation.html\">Automation & Agents</a>
          <a href=\"{ROOT_PREFIX}fractional-caio.html\">Fractional CAIO</a>
          <a href=\"{ROOT_PREFIX}workshops.html\">Workshops</a>
        </div>
        <div>
          <h4>Explore</h4>
          {explore_links}
        </div>
        <div>
          <h4>Connect</h4>
          <a href=\"https://www.linkedin.com/company/implementai-ae\">LinkedIn</a>
          <a href=\"mailto:sales@implementai.ae\">Email Us</a>
        </div>
      </div>
      <div
        style=\"border-top: 1px solid var(--prem-border); padding-top: 2rem; text-align: center; color: var(--prem-text-secondary); font-size: 0.85rem;\">
        &copy; 2025 iMPLEMENTAi.ae. All rights reserved.
      </div>
    </div>
  </footer>"""


def determine_active_style(filepath: str) -> str:
    normalized = filepath.lstrip('./')
    if normalized in FILE_MAPPING:
        return FILE_MAPPING[normalized]
    basename = os.path.basename(normalized)
    return FILE_MAPPING.get(basename, '')


def update_file(filepath: str, footer_html: str) -> None:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    active_key = determine_active_style(filepath)
    nav_html = build_nav_html(active_key)

    new_content = NAV_PATTERN.sub(nav_html, content)
    new_content = FOOTER_PATTERN.sub(footer_html, new_content)

    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filepath}")


def main():
    footer_html = build_footer_html()
    for root, dirs, files in os.walk('.'):
        dirs[:] = [d for d in dirs if d not in {'node_modules', '__pycache__', '.git', '.vscode', 'transcription and image files'}]
        for file in files:
            if file.endswith('.html'):
                filepath = os.path.join(root, file)
                update_file(filepath, footer_html)


if __name__ == '__main__':
    main()
