# Product Requirements Document  
ImplementAi.ae – AI Experts Hub  
Version 1.0

## Overview  
ImplementAi.ae will host a public-facing AI Experts Hub. The target users are AI consultants, automation engineers, LLM specialists, prompt engineers, and AI developers sourced mainly from LinkedIn outreach. The page will serve as a talent intake mechanism and a public directory.

Experts land on the intake page, submit their LinkedIn profile URL and optional details, and the system auto-generates a public Fiverr-style expert profile. These profiles populate a directory that clients can browse and the company can use to staff future AI projects.

The system must be simple for experts, automated for ImplementAi, and scalable to thousands of profiles.

## Objectives  

1. Build a public landing page that converts LinkedIn leads into talent listings.  
2. Enable experts to submit minimal information for profile creation.  
3. Scrape LinkedIn to extract profile data for auto-generated expert pages.  
4. Automatically create expert profile cards and populate them in a directory.  
5. Create an internal pool of experts for future project deployment.  
6. Lay foundations for future verified badges, ratings, tiers, and matching systems.

## User Personas  

### AI Consultant  
- Receives a link via LinkedIn.  
- Wants visibility and potential project work.  
- Wants fast, simple onboarding.  
- Provides LinkedIn URL, optional CV, and rate.

### ImplementAi Project Team  
- Uses the directory to locate experts.  
- Needs a filtered list sorted by skills, toolsets, rates, and seniority.  
- Wants automatic profile generation to reduce manual effort.

### Future Clients  
- Want to browse experts.  
- Want to understand expertise quickly.  
- Use filters by skill and category.

## Scope  

### In Scope  
- Landing page design and content.  
- Form with minimal fields.  
- Automated scraping of LinkedIn public data.  
- Profile summarisation using LLM.  
- Expert profile generation.  
- Directory with filtering.  
- GitHub integration for automatic page creation.  
- JSON or database storage of expert data.

### Out of Scope (for MVP)  
- Payment processing.  
- Expert login and self-editing.  
- Ratings or reviews from clients.  
- Automated vetting systems.  
- Portfolio enhancements beyond scraped LinkedIn data.

## Pages Required  

### Page 1: Landing Page – Join the AI Experts Hub  
Purpose: Convert LinkedIn leads into submissions.

Sections:  
- Hero section with headline, sub-headline, explainer.  
- Three-step process explaining how it works.  
- Benefits of joining.  
- Submission form.

Form fields:  
- Required: LinkedIn Profile URL  
- Optional: Upload CV (PDF), expected rate, currency dropdown, rate-type dropdown, free text input for expectations

Submit action:  
- Save data payload  
- Trigger scraper and summariser pipeline  
- Redirect to submission confirmation page

### Page 2: Submission Confirmation Page  
Simple confirmation that the profile is being generated.

Message:  
Thank you, your expert profile is being generated. You will appear in the directory once the data extraction and review are completed.

### Page 3: Public Experts Directory  
Grid-style layout with cards.  
Each card displays:  
- Name  
- Title  
- Location  
- Summary  
- Skills as tags  
- Rate if provided  
- View Profile link

Filters:  
- Skill  
- Platform (n8n, Make.com, OpenAI, LangChain, etc.)  
- Seniority  
- Rate range  
- Location  
- Verified (future)

### Page 4: Expert Profile Page  
Scraped data presented in a structured format.

Sections:  
- Header: Name, photo, title, rate  
- Summary: Generated from LinkedIn  
- Expertise tags  
- Experience summary  
- Tools and technologies  
- Portfolio links if found  
- Contact CTA: “Contact ImplementAi to hire this expert”

## Functional Requirements  

### Intake and Submission  
- Must accept form data, validate the LinkedIn URL, and store JSON.  
- Must accept CV upload.  
- Must accept rate information.

### Data Extraction  
- System fetches public LinkedIn profile content.  
- Handles cases where profile is private or restricted.

### AI Summarisation  
Models must generate:  
- Summary paragraph  
- Skills list  
- Tools list  
- Experience highlights  
- Recommended category tags  
- Display title for profile card

### Directory Population  
- Automatic generation of profile pages (HTML or MD).  
- Automatic addition of a profile card to the directory.  
- JSON storage of each expert’s record.

### UI and Design  
- Clean, simple, modern layout.  
- Fiverr or Upwork inspired card grid.  
- Mobile responsive.  
- Uses ImplementAi branding.

### SEO Requirements  
- Each expert page must have meta title and meta description.  
- Directory must be indexable with pagination.

## Non Functional Requirements  

### Performance  
- Directory must load within reasonable time with up to 10,000 experts.  
- Profile generation pipeline must complete within 3 to 10 seconds where possible.

### Security  
- Uploaded CV files must be scanned.  
- Data must be stored securely.  
- LinkedIn scraping must follow compliance rules.

### Scalability  
- JSON-based or database architecture must allow large expansion.  
- Directory must support filters and search at scale.

## Pipelines and Workflow  

### Trigger  
Form submission.

### Pipeline Steps  
1. Validate submission.  
2. Scrape public LinkedIn profile.  
3. Parse raw data into structured JSON.  
4. AI summarisation to generate:  
   - Summary  
   - Skills  
   - Tools  
   - Experience  
   - Title  
   - Tags  
5. Generate expert profile page from template.  
6. Push to Experts directory.  
7. Save JSON record.  
8. Optional notification to admin.

## Folder and Repo Structure

/ai-experts-hub
  /public
    /index.html
    /experts
      /[expert-id]
        profile.html
    /assets
      /images
      /css
      /js
  /data
    experts.json
    profiles/
      expert-[id].json
  /templates
    profile-template.html
    card-template.html
  /scripts
    scraper.js
    generator.js
    pipeline.js
  /forms
    intake-handler.js
  PRD.md
  README.md

## Future Roadmap  

### Verification  
- Assign verified badges to experts after working on projects.

### Tiering  
- Basic, Silver, Gold, Platinum.

### Advanced Matching  
- Internal dashboard with filters.  
- Project-staffing engine.  
- Skill ranking algorithms.

### Portfolio Enhancements  
- Expert uploads of demos, GitHub, case studies.

## Dependencies  
- LinkedIn scraper or API alternative.  
- LLM for summarisation.  
- JSON storage or database.  
- Hosting on Hostinger.  
- GitHub integration with Antigravity.

## Acceptance Criteria  

1. Expert can land, submit form, and receive confirmation page.  
2. System can scrape LinkedIn for most profiles.  
3. Summary and skills appear correctly on expert page.  
4. Expert appears in directory with correct card design.  
5. Directory filters work.  
6. Mobile version works.  
7. GitHub commit triggers update in production site.