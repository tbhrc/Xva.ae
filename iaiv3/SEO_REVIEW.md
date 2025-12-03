# Website SEO Review

## Overall Score
**72/100** – Solid technical foundations (unique titles/descriptions, sitemap, robots directives) but missing social previews/structured data and a few technical/content gaps that limit discoverability and click-through rates.

### Score Breakdown
- **Technical (28/35)** – Indexability, canonicalization, and crawl directives are in place for the homepage and robots file, but timestamps in the sitemap undermine freshness signals.【F:iaiv3/index.html†L2-L20】【F:iaiv3/robots.txt†L1-L19】【F:iaiv3/sitemap.xml†L4-L35】
- **On-page metadata (16/25)** – Titles and meta descriptions exist, yet the absence of Open Graph/Twitter tags across key pages suppresses social click-through and SERP rich previews.【F:iaiv3/index.html†L4-L20】【F:iaiv3/blog.html†L1-L12】
- **Content architecture (18/25)** – Core pages are linked in the sitemap, but the blog lacks pagination and related content pathways that help clustering and crawl depth.【F:iaiv3/sitemap.xml†L1-L38】【F:iaiv3/blog.html†L32-L80】
- **Performance/media (10/15)** – Hero video autoplays without poster/fallbacks, pushing LCP and hurting mobile users.【F:iaiv3/index.html†L78-L95】

## Strengths
- **Clear indexing signals**: `index.html` declares language, viewport, descriptive title, meta description, robots indexing, and a canonical URL, which helps avoid duplicate signals for the homepage.【F:iaiv3/index.html†L2-L20】
- **Crawl guidance present**: `robots.txt` allows full crawling (with sensitive directories disallowed) and points to the sitemap for discovery.【F:iaiv3/robots.txt†L1-L19】
- **Sitemap coverage**: A sitemap lists core pages to guide search engines, covering key commercial and resource URLs.【F:iaiv3/sitemap.xml†L1-L38】

## Gaps & Risks
1. **Missing social preview metadata**: No Open Graph or Twitter Card tags on the homepage, so links shared on social platforms may lack rich previews, lowering click-through rates.【F:iaiv3/index.html†L4-L20】
2. **Future-dated sitemap timestamps**: `lastmod` values are set to 2025-12-02, which can reduce trust in freshness signals and may cause search engines to ignore updates.【F:iaiv3/sitemap.xml†L4-L35】
3. **Partial structured data**: Article pages include minimal Article JSON-LD but miss publication dates, images, and breadcrumb context; the homepage lacks Organization schema for brand signals.【F:iaiv3/blog-ai-assistants-vs-chatbots-uae.html†L4-L80】【F:iaiv3/index.html†L4-L20】
4. **Large autoplay hero video without fallbacks**: The homepage autoplays a background MP4 without a `poster` image or lazy loading, which can hurt Largest Contentful Paint and mobile bandwidth.【F:iaiv3/index.html†L78-L95】
5. **Blog discoverability**: The blog page lacks pagination, category links, or internal linking blocks that surface related articles, limiting crawl depth and topical clustering.【F:iaiv3/blog.html†L32-L80】

## Priority Recommendations
- Add Open Graph and Twitter Card tags (title, description, image, URL) on all major pages, starting with `index.html` and blog posts.
- Add Organization JSON-LD on the homepage; enrich Article JSON-LD with author, datePublished, image, and breadcrumbs.
- Update `sitemap.xml` `lastmod` to actual publish/update dates and include full coverage of current URLs.
- Optimize the hero video with `poster`, `preload="metadata"`, and a responsive fallback image; consider lazy-loading non-critical media.
- Expand internal linking and taxonomy on the blog (categories/tags, related posts, pagination) to improve crawlability and topical authority.

## Fast Wins (2–7 days)
- Ship Open Graph + Twitter meta tags and canonical links on homepage and blog templates.
- Replace sitemap timestamps with accurate `lastmod` values and add any missing live URLs.
- Add a `poster` attribute and `preload="metadata"` to the hero video to reduce LCP impact.

## 30/60/90 Day Plan
- **30 days**: Publish Organization JSON-LD on all pages; enrich Article JSON-LD for each blog post; introduce related-articles block on blog listing and posts.
- **60 days**: Launch blog categories/tags and pagination; add breadcrumb schema; audit media for compression and responsive images.
- **90 days**: Monitor Search Console for coverage/rich results; A/B test social preview images/titles; add internal-link modules on high-traffic commercial pages.
