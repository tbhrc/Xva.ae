module.exports = {
  content: [
    './*.html',
    './assets/js/*.js'
  ],
  theme: {
    extend: {
      colors: {
        brand: {
          50: '#fff7e6',
          100: '#ffe7b8',
          300: '#ffd272',
          400: '#ffc043',
          500: '#ffb01a',
          600: '#e09400'
        }
      },
      boxShadow: {
        'brand-glow': '0 18px 45px rgba(255,192,67,0.25)'
      }
    }
  },
  plugins: []
};
