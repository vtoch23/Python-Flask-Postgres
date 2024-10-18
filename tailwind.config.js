/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./index.html",
    "./src/**/*.{html,js,ts,jsx,tsx}",
  ],
  theme: {
    fontFamily: {
      'sans': ['Roboto'],
    },
    extend: {
      gridTemplateColumns: {
        // Simple 16 column grid
        "16": "repeat(16, minmax(0, 1fr))",
      },
      gridColumnStart: {
        "13": "13",
        "14": "14",
        "15": "15",
        "16": "16",
        "17": "17",
      },
      gridColumnEnd: {
        "13": "13",
        "14": "14",
        "15": "15",
        "16": "16",
        "17": "17",
      },
    }
  },
  plugins: [
  ],
}