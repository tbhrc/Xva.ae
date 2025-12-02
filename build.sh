#!/bin/bash
# Build script for ImplementAI website

echo "Building production assets..."

# Build CSS with Tailwind
npm run build:css

# (Optional) Minify JS
# npx terser assets/js/main.js -o assets/js/main.min.js -c -m

echo "✓ Build complete"
echo "Update domain in:"
echo "  - All canonical URLs (replace 'example.com')"
echo "  - All og:image URLs"
echo "  - sitemap.xml base URLs"
echo "  - robots.txt sitemap URL"
