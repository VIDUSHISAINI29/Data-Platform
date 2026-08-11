/** @type {import('tailwindcss').Config} */
export default {
   important: true,
   darkMode: "class",
   prefix: "tw-",

   content: ["./index.html", "./src/**/*.{vue,ts}"],

   theme: {
      extend: {
         boxShadow: {
            custom: "0 8px 30px rgba(0, 0, 0, 0.12)",
         },
         colors: {
        pulse: {
          bg: '#040710',
          card: '#0e1521',
          border: '#1F2937',
          grayText: '#9CA3AF',
          blue: '#195bfd',
          pink: '#FF0095',
          purple: '#7c3aed',
          green: '#22C55E',
          lime:'#d5fc5b',
          cyan: '#22D3EE',
          success: '#22C55E',
          error: '#EF4444',
          warning: '#F59E0B',
        }
      }
      },
   },

   plugins: [],
};
