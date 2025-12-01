module.exports = {
  content: [
    './*.html',
    './assets/js/*.js'
  ],
  theme: {
    extend: {
      colors: {
        brand: {
          50: '#f0f9ff',
          100: '#e0f2fe',
          300: '#7dd3fc',
          400: '#38bdf8',
          500: '#0ea5e9',
          600: '#0284c7'
        }
      },
      boxShadow: {
        'brand-glow': '0 18px 45px rgba(15, 118, 110, 0.2)'
      }
    }
  },
  plugins: []
};
