/** @type {import('tailwindcss').Config} */
export default {
  content: ['./index.html', './src/**/*.{js,ts,jsx,tsx}'],
  theme: {
    extend: {
      colors: {
        forge: {
          900: '#020817',
          800: '#0f172a',
          700: '#111827',
          600: '#1f2937',
          500: '#22c55e',
          400: '#38bdf8',
        },
      },
    },
  },
  plugins: [],
};
