# Data Dunkers Student Portal

Repository for student-facing Jupyter notebook activities and supporting HTML exports for the Data Dunkers program.

## What’s Here

- `activities/` — primary student notebooks grouped by topic (interpreting visuals, data skills, applied analysis) plus `HTML-Exports/` for rendered copies (ignored in git).
- `notebooks/` — challenge and enrichment notebooks using current basketball datasets.
- `docs/` — simple static index page that links to many lesson variants.
- `requirements.txt` — minimal Python stack (Jupyter, pandas/numpy, plotly.express, requests/bs4/lxml).
- `.venv/` (optional) — local virtual environment if you create one.

## Getting Started

1) Install Python 3.10+ and create a virtual environment: `python -m venv .venv && .\.venv\Scripts\activate` (Windows) or `source .venv/bin/activate` (macOS/Linux).  
2) Install dependencies: `pip install -r requirements.txt`.  
3) Launch Jupyter: `jupyter lab` (or `jupyter notebook`) and open files in `activities/` to work through lessons top-to-bottom.

## Tips for Using the Notebooks

- Keep outputs and written reflections in-place; duplicate files if you want a fresh copy.
- Run cells sequentially; most notebooks assume earlier setup cells have executed.
- Visual notebooks (using `plotly.express` exclusively) focus on reading charts; data skill notebooks cover cleaning, sorting/merging, correlations, descriptive stats, and simple synthetic data; applied analysis includes shot charts.
- Challenge notebooks in `notebooks/` explore live or recent NBA data (player profiles, shot selection, partial-season trends, etc.) and may require network access for API calls.

## Updating or Publishing

- Export HTML versions of notebooks into `activities/HTML-Exports/` to keep outputs alongside source without committing them.
- If you host the static site, point to `docs/index.html` or generate fresh links after adding new lessons.

## Lesson Page Template Requirements

To ensure consistency across the student portal, all lesson pages in `docs/` must follow the standardized format established in `docs/shot-charts.html`.

### 1. Visual Branding & Layout

- **Banners:** Include top and bottom banners from the Data-Dunkers repository.
- **Header:** Use an `<h2>` for the title and a brief introductory paragraph.
- **Styling:** Standard 2% margins and `sans-serif` font.

### 2. Interactive Visualization

- **Iframe:** Embed the Plotly visualization from `docs/visualizations/` using an `<iframe>`.
- **Interaction Rules:** Provide a short explanation of how to use the visualization (hover, legend filters, etc.).

### 3. Critical Thinking Questions

- **Dynamic Rendering:** Define questions in a JS array and render them as `<label>` and `<input>` elements.
- **Persistence:** Use `localStorage` to save answers automatically. **Important:** The storage key must be unique to the page (e.g., `filename + 'Answers'`) to avoid overwriting data between lessons.
- **Copy Feature:** Include a "Copy Answers" button that formats the Q&A for the clipboard.

### 4. Navigation & Links

- **Tooling:** Include dynamic links to the source notebook on GitHub, Google Colab, and Callysto Hub.
- **Page Links:** Provide clear "home" and "next" lesson links in the footer.

## Support

- Issues typically stem from missing packages or blocked network calls for live-data notebooks. Re-run `pip install -r requirements.txt`, and if fetching data fails, retry on a different network or mock data locally.
