# Website SEO Review

## Overall Score
**72/100** – Solid technical foundations (unique titles/descriptions, sitemap, robots directives) but missing social previews/structured data and a few technical/content gaps that limit discoverability and click-through rates.

## Strengths
- **Clear indexing signals**: `index.html` declares language, viewport, descriptive title, meta description, robots indexing, and a canonical URL, which helps avoid duplicate signals for the homepage.【F:iaiv3/index.html†L2-L20】
- **Crawl guidance present**: `robots.txt` allows full crawling (with sensitive directories disallowed) and points to the sitemap for discovery.【F:iaiv3/robots.txt†L1-L19】
- **Sitemap coverage**: A sitemap lists core pages to guide search engines, covering key commercial and resource URLs.【F:iaiv3/sitemap.xml†L1-L38】

## Gaps & Risks
1. **Missing social preview metadata**: No Open Graph or Twitter Card tags on the homepage, so links shared on social platforms may lack rich previews, lowering click-through rates.【F:iaiv3/index.html†L4-L20】
2. **Canonical gaps on secondary pages**: The blog listing lacks a canonical link, raising duplicate-content risk if parameters or alternate paths appear.【F:iaiv3/blog.html†L1-L12】
3. **Future-dated sitemap timestamps**: `lastmod` values are set to 2025-12-02, which can reduce trust in freshness signals and may cause search engines to ignore updates.【F:iaiv3/sitemap.xml†L4-L35】
4. **No structured data**: Pages do not expose JSON-LD or microdata for Organization, Article, or Breadcrumbs, missing opportunities for rich results (sitelinks, logos, article cards).【F:iaiv3/index.html†L4-L20】【F:iaiv3/blog.html†L1-L12】
5. **Large autoplay hero video without fallbacks**: The homepage autoplays a background MP4 without a `poster` image or lazy loading, which can hurt Largest Contentful Paint and mobile bandwidth.【F:iaiv3/index.html†L78-L95】
6. **Blog discoverability**: The blog page lacks pagination, category links, or internal linking blocks that surface related articles, limiting crawl depth and topical clustering.【F:iaiv3/blog.html†L32-L80】

## Priority Recommendations
- Add Open Graph and Twitter Card tags (title, description, image, URL) on all major pages, starting with `index.html` and blog posts.
- Insert canonical tags on every indexable page (e.g., `blog.html`, article pages) to consolidate signals.
- Update `sitemap.xml` `lastmod` to actual publish/update dates and include full coverage of current URLs.
- Implement Organization and Article JSON-LD; add BreadcrumbList markup on multi-level content.
- Optimize the hero video with `poster`, `preload="metadata"`, and a responsive fallback image; consider lazy-loading non-critical media.
- Expand internal linking and taxonomy on the blog (categories/tags, related posts) to improve crawlability and topical authority.
