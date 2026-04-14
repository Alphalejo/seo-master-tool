# 🔍 SEO Master Tool
> AI-powered SEO auditor and compliance checker built for real estate websites.

---

## Overview

SEO Master Tool is a professional web application that helps real estate teams audit, optimize, and ensure compliance of their websites — all in one place. Built with Python and Streamlit, it combines intelligent web crawling, AI-generated SEO titles, broken link detection, and real estate compliance lookups into a single streamlined workflow.

---

## 🌐 Live App

The app is deployed on **Streamlit Community Cloud** — no installation needed.

👉 [Launch SEO Master Tool](#) *(replace with your Streamlit URL)*

> The app may be in sleep mode if inactive. Just click **"Wake up app"** and it'll be ready in seconds.

---

## Features

### 📋 SEO Analyzer
- **Website Crawler** — Scans up to 50 pages using BFS crawling with smart filtering rules for real estate site structures
- **SEO Title Audit** — Evaluates every page title against optimal character length (45–60 chars) with color-coded results
- **Broken Link Detector** — Identifies 404s, soft 404s, timeouts, and redirect loops across all crawled pages
- **Magic AI Optimizer** — Uses Gemini 2.5 Flash to generate optimized SEO titles based on your existing content
- **Analytics Dashboard** — Interactive Plotly charts for SEO health distribution and link status breakdown

### ⚖️ Compliance Checker
- **State Compliance Lookup** — Identifies high compliance and non-disclosure states with direct documentation links
- **Brokerage Compliance** — Covers 27+ brokerages across partnership and non-partnership tiers
- **MLS Board Reference** — Searchable database of 70+ MLS boards with compliance documentation links

---

## Tech Stack

| Layer | Tools |
|---|---|
| Frontend | Streamlit |
| Scraping | BeautifulSoup4, Requests |
| Data & Viz | Pandas, Plotly Express |
| AI | Google Gemini 2.5 Flash (`google-generativeai`) |
| Utils | urllib, collections.deque |

---

## Project Structure

```
seo-master-tool/
│
├── app.py                  # Main UI controller
├── requirements.txt
├── .gitignore
│
├── toolkit/
│   ├── SEO_scraper.py      # BFS crawler + broken link checker
│   ├── SEO_dashboard.py    # Plotly analytics charts
│   ├── seo_ai.py           # Gemini AI title generator
│   └── compliance_checker.py  # State, brokerage & MLS compliance logic
│
└── data/
    └── tokens_records.json # Daily token usage tracker
```

---

## Getting Started

### 1. Clone the repo
```bash
git clone https://github.com/your-username/seo-master-tool.git
cd seo-master-tool
```

### 2. Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up environment variables
Create a `.env` file in the root:
```
GEMINI_API_KEY=your_gemini_api_key_here
```

### 5. Run the app
```bash
streamlit run app.py
```

---

## Usage

### SEO Analyzer Tab
1. Enter a target real estate website URL
2. Optionally enable **Check Broken Links** before running
3. Click **Run Audit** — the crawler will scan the site and return SEO title data
4. Use the **Magic AI** optimizer to generate improved titles from existing ones
5. Toggle the **Analytics Dashboard** for visual insights

### Compliance Tab
1. Select a US state
2. Optionally select a brokerage from the dropdown
3. Select any relevant MLS boards
4. Click **Verify Compliance** to retrieve documentation links

---

## Configuration

### Crawl Filters
By default, the crawler excludes:
- `/blog/`
- `/neighborhoods/`
- `/developments/`
- `/properties/` *(except `/properties/sale` and `/properties/sold`)*

### Token Limits
Daily Gemini API usage is capped at **1,000 input / 1,000 output tokens** per day, tracked in `data/tokens_records.json`. Adjust the `TOKEN_LIMIT` constant in `toolkit/seo_ai.py`.

---

## Roadmap

- [ ] Export audit results to CSV / PDF
- [ ] Bulk AI title generation for all pages at once
- [ ] Scheduled audits with email alerts
- [ ] Expanded compliance database

---

## License

This project is proprietary and intended for internal use.