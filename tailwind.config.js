/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{js,jsx,ts,tsx}",
    "./public/index.html"
  ],
  theme: {
    extend: {
      colors: {
        primary: {
          50: '#eff6ff',
          100: '#dbeafe',
          200: '#bfdbfe',
          300: '#93c5fd',
          400: '#60a5fa',
          500: '#3b82f6',
          600: '#2563eb',
          700: '#1d4ed8',
          800: '#1e40af',
          900: '#1e3a8a',
        },
        secondary: {
          50: '#f0fdf4',
          100: '#dcfce7',
          200: '#bbf7d0',
          300: '#86efac',
          400: '#4ade80',
          500: '#22c55e',
          600: '#16a34a',
          700: '#15803d',
          800: '#166534',
          900: '#14532d',
        },
        // Earthy color palette
        brown: {
          50: '#FDF8F3',
          100: '#F5E6D3',
          200: '#E8C9A8',
          300: '#DBA87D',
          400: '#CE8752',
          500: '#8B4513', // Primary brown
          600: '#A0522D', // Secondary brown
          700: '#654321', // Dark brown
          800: '#4A2F1A',
          900: '#2F1D10',
        },
        green: {
          50: '#F0FFF0',
          100: '#DCFFDC',
          200: '#B8FFB8',
          300: '#94FF94',
          400: '#70FF70',
          500: '#228B22', // Primary green
          600: '#32CD32', // Secondary green
          700: '#006400',
          800: '#004D00',
          900: '#003300',
        },
        gold: {
          50: '#FFFDF0',
          100: '#FFF8DC',
          200: '#FFF0B8',
          300: '#FFE894',
          400: '#FFE070',
          500: '#DAA520', // Accent gold
          600: '#B8860B',
          700: '#8B6914',
          800: '#6B4F0F',
          900: '#4A350A',
        },
        cream: '#F5F5DC',
        'light-green': '#90EE90',
      },
      fontFamily: {
        sans: ['Inter', 'system-ui', 'sans-serif'],
      },
      animation: {
        'fade-in': 'fadeIn 0.6s ease-in',
        'slide-in-left': 'slideInLeft 0.6s ease-out',
        'slide-in-right': 'slideInRight 0.6s ease-out',
        'float': 'float 6s ease-in-out infinite',
      },
      keyframes: {
        fadeIn: {
          '0%': { opacity: '0', transform: 'translateY(20px)' },
          '100%': { opacity: '1', transform: 'translateY(0)' },
        },
        slideInLeft: {
          '0%': { opacity: '0', transform: 'translateX(-30px)' },
          '100%': { opacity: '1', transform: 'translateX(0)' },
        },
        slideInRight: {
          '0%': { opacity: '0', transform: 'translateX(30px)' },
          '100%': { opacity: '1', transform: 'translateX(0)' },
        },
        float: {
          '0%, 100%': { transform: 'translateY(0px)' },
          '50%': { transform: 'translateY(-20px)' },
        },
      },
      backgroundImage: {
        'gradient-radial': 'radial-gradient(var(--tw-gradient-stops))',
        'gradient-conic': 'conic-gradient(from 180deg at 50% 50%, var(--tw-gradient-stops))',
        'gradient-earth': 'linear-gradient(135deg, #8B4513 0%, #228B22 100%)',
        'gradient-hero': 'linear-gradient(135deg, #F5F5DC 0%, #90EE90 100%)',
      },
    },
  },
  plugins: [],
} 