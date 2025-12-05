"""Automated expert enrichment and publishing pipeline."""

from __future__ import annotations

import json
import random
import re
from datetime import datetime
from pathlib import Path
from typing import Dict, Optional

from sqlalchemy.orm import Session

from .. import models

SITE_ROOT = Path(__file__).resolve().parents[2]
PROFILE_DIR = SITE_ROOT / "ai-experts" / "profiles"
DEFAULT_AVATAR = "/assets/images/2.png"


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", value).strip("-").lower()
    return slug or "expert"


def profile_page_url(expert: models.Expert) -> str:
    return f"/ai-experts/profiles/expert-{expert.id}.html"


def synthesize_summary(expert: models.Expert, linkedin_profile: Dict[str, str]) -> str:
    headline = linkedin_profile.get("headline") or expert.title
    expertise = expert.expertise or linkedin_profile.get("expertise") or "AI"
    location = expert.location or linkedin_profile.get("location") or "Remote-first"
    highlight = linkedin_profile.get("highlight") or "deploying production-grade AI systems"

    return (
        f"{expert.name} is a {headline} focused on {expertise}. "
        f"They have a track record of {highlight} and partnering with business leaders across {location}."
    )


def mock_linkedin_research(expert: models.Expert) -> Dict[str, str]:
    fallback_tools = ["OpenAI", "Azure AI", "LangChain", "Pinecone", "Vertex AI"]
    random.shuffle(fallback_tools)
    return {
        "headline": expert.title,
        "expertise": expert.expertise or "AI Strategy",
        "location": expert.location or "Remote",
        "highlight": "shipping reliable AI copilots and analytics for revenue teams",
        "tools": expert.tools or ", ".join(fallback_tools[:3]),
        "photo_url": None,
    }


def ensure_directories() -> None:
    PROFILE_DIR.mkdir(parents=True, exist_ok=True)


def publish_profile_page(expert: models.Expert, avatar_url: str) -> Path:
    ensure_directories()
    file_path = PROFILE_DIR / f"expert-{expert.id}.html"
    experience = expert.summary or "Seasoned AI expert helping teams execute with confidence."

    html = f"""<!doctype html>
<html lang=\"en\">
<head>
  <meta charset=\"UTF-8\" />
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\" />
  <title>{expert.name} | AI Experts Hub</title>
  <link rel=\"preload\" href=\"/assets/css/v7.3-premium.css\" as=\"style\" onload=\"this.onload=null;this.rel='stylesheet'\" />
  <noscript><link rel=\"stylesheet\" href=\"/assets/css/v7.3-premium.css\" /></noscript>
</head>
<body class=\"prem-body\" style=\"background: #f7f9fc;\">
  <main class=\"prem-container\" style=\"max-width: 900px; padding: 3rem 1rem;\">
    <a href=\"/ai-experts/index.html\" class=\"prem-btn prem-btn-outline\" style=\"margin-bottom: 1.5rem; display: inline-block;\">⬅ Back to AI Experts Hub</a>
    <section class=\"prem-card\" style=\"padding: 2rem; display: grid; gap: 1.5rem; grid-template-columns: 220px 1fr; align-items: center;\">
      <div style=\"text-align: center;\">
        <img src=\"{avatar_url}\" alt=\"{expert.name}\" style=\"width: 180px; height: 180px; object-fit: cover; border-radius: 24px; border: 1px solid var(--prem-border);\" />
      </div>
      <div>
        <p class=\"prem-eyebrow\" style=\"margin-bottom: 0.35rem;\">AI Experts Hub</p>
        <h1 style=\"margin: 0 0 0.35rem; font-size: 2rem;\">{expert.name}</h1>
        <p style=\"color: var(--prem-text-secondary); margin: 0 0 0.75rem;\">{expert.title}</p>
        <div style=\"display: flex; gap: 0.5rem; flex-wrap: wrap; margin-bottom: 1rem;\">
          {f'<span class="chip">{expert.location}</span>' if expert.location else ''}
          {f'<span class="chip">{expert.expertise}</span>' if expert.expertise else ''}
          {f'<span class="chip">{expert.tools}</span>' if expert.tools else ''}
        </div>
        <p style=\"line-height: 1.7; color: var(--prem-text);\">{experience}</p>
        <div style=\"margin-top: 1rem; display: flex; gap: 0.75rem; flex-wrap: wrap; align-items: center;\">
          <a class=\"prem-btn\" href=\"{expert.linked_in_url}\" target=\"_blank\" rel=\"noopener\">View LinkedIn</a>
          <span class=\"chip\" style=\"background: #e0f2fe; color: #0f172a;\">Published {datetime.utcnow().strftime('%b %d, %Y')}</span>
        </div>
      </div>
    </section>
  </main>
</body>
</html>
"""

    file_path.write_text(html, encoding="utf-8")
    return file_path


def decorate_expert(expert: models.Expert, avatar_url: Optional[str] = None) -> models.Expert:
    expert.avatar_url = avatar_url or DEFAULT_AVATAR
    expert.profile_page_url = profile_page_url(expert)
    return expert


def enrich_and_publish(expert: models.Expert, db: Session) -> models.Expert:
    research = mock_linkedin_research(expert)
    expert.summary = synthesize_summary(expert, research)
    expert.tools = expert.tools or research.get("tools")
    expert.location = expert.location or research.get("location")
    expert.vetted_status = "approved"

    db.commit()
    db.refresh(expert)

    avatar = research.get("photo_url") or DEFAULT_AVATAR
    publish_profile_page(expert, avatar)
    return decorate_expert(expert, avatar)


def dump_profile_payload(expert: models.Expert) -> None:
    ensure_directories()
    payload = {
        "id": expert.id,
        "name": expert.name,
        "title": expert.title,
        "summary": expert.summary,
        "linked_in_url": expert.linked_in_url,
        "location": expert.location,
        "expertise": expert.expertise,
        "tools": expert.tools,
        "vetted_status": expert.vetted_status,
        "avatar_url": getattr(expert, "avatar_url", DEFAULT_AVATAR),
        "profile_page_url": getattr(expert, "profile_page_url", profile_page_url(expert)),
        "published_at": datetime.utcnow().isoformat(),
    }
    json_path = PROFILE_DIR / f"expert-{expert.id}.json"
    json_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
