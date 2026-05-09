# ResumeAI — GenAI Academic Project

AI-powered Resume & Cover Letter Generator using Flask + OpenAI GPT-4o-mini.

## Project Structure

```
resume-generator/
├── app.py            ← Flask backend (REST API)
├── index.html        ← Frontend (HTML + CSS + JS)
├── requirements.txt  ← Python dependencies
└── README.md
```

## Setup & Run

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Set your OpenAI API Key

**Option A — Environment variable (recommended):**
```bash
# Mac/Linux
export OPENAI_API_KEY="sk-your-key-here"

# Windows CMD
set OPENAI_API_KEY=sk-your-key-here
```

**Option B — Edit app.py directly:**
Replace `"YOUR_OPENAI_API_KEY_HERE"` with your actual key in line:
```python
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY", "YOUR_OPENAI_API_KEY_HERE"))
```

### 3. Run the Flask server
```bash
python app.py
```

### 4. Open in browser
Visit: **http://localhost:5000**

---

## How it Works

```
User fills form (index.html)
        ↓
Fetch API → POST /generate (JSON)
        ↓
Flask (app.py) — Prompt Engineering
        ↓
OpenAI GPT-4o-mini API
        ↓
Resume + Cover Letter (Markdown text)
        ↓
Displayed in browser with tab switcher + copy button
```

## Tech Stack
- **Frontend**: HTML, CSS, JavaScript (Fetch API)
- **Backend**: Python + Flask
- **AI**: OpenAI GPT-4o-mini
- **Communication**: REST API / JSON