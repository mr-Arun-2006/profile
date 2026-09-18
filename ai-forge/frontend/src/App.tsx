@tailwind base;
@tailwind components;
@tailwind utilities;

:root {
  font-family: 'Inter', 'Segoe UI', sans-serif;
  color: #e2e8f0;
  background: #020817;
}

body {
  margin: 0;
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
