@tailwind base;
@tailwind components;
@tailwind utilities;

:root {
  font-family: 'Inter', 'Segoe UI', sans-serif;
  color: #e2e8f0;
  background: #020817;
  line-height: 1.5;
  font-weight: 400;
  font-synthesis: none;
  text-rendering: optimizeLegibility;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

html, body, #root {
  min-height: 100%;
  margin: 0;
}

body {
  min-width: 320px;
  min-height: 100vh;
  background:
    radial-gradient(circle at top, rgba(34, 197, 94, 0.12), transparent 30%),
    linear-gradient(180deg, #020817 0%, #0f172a 100%);
}

* {
  box-sizing: border-box;
}

button, input, textarea, select {
  font: inherit;
}

::-webkit-scrollbar {
  width: 10px;
}

::-webkit-scrollbar-track {
  background: rgba(15, 23, 42, 0.7);
}

::-webkit-scrollbar-thumb {
  background: rgba(148, 163, 184, 0.35);
  border-radius: 999px;
}

::-webkit-scrollbar-thumb:hover {
  background: rgba(148, 163, 184, 0.5);
}

textarea {
  scrollbar-width: thin;
}
