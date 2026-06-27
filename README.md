# 📄 SnapNotes — AI-Powered Document Note Generator

> Upload PDFs and PowerPoint files, and SnapNotes uses AI to instantly generate clean, structured notes — preserving your original headings and summarizing key content under each one.

---

## ✨ Features

- 📁 **Multi-file upload** — Process multiple PDFs and PPTX files at once
- 🧠 **AI-powered summarization** — Powered by Groq's `llama-3.1-8b-instant` model (extremely fast)
- 📝 **Heading-preserving notes** — Original document headings are kept intact; content is summarized underneath
- 📊 **PPTX support** — Slide titles become headings, slide content becomes notes
- 📄 **PDF support** — Full structure extraction with Markdown heading detection via `pymupdf4llm`
- ⬇️ **Download notes** — Export generated notes as `.md` files per document
- 🌐 **Streamlit UI** — Clean, browser-based interface with no setup beyond Python

---

## 🗂️ Project Structure

```
SnapNotes/
│
├── SnapNotes.py          # Main Streamlit app — UI and file handling
├── document_parser.py    # PDF and PPTX text extraction to Markdown
├── note_maker.py         # Groq API call — summarizes content with AI
├── run.py                # Launcher — patches browser tab title, starts app
├── requirements.txt      # Python dependencies
├── .env.example          # Template for your API key
└── .gitignore
```

---

## ⚙️ How It Works

```
User uploads PDF/PPTX
        ↓
document_parser.py extracts text → Markdown format
        ↓
note_maker.py sends text to Groq LLM
        ↓
AI returns structured notes preserving all headings
        ↓
Notes displayed + available to download as .md
```

---

## 🚀 Setup & Running

### 1. Clone the repo
```bash
git clone https://github.com/mian-shafay/SnapNotes.git
cd SnapNotes
```

### 2. Create and activate a virtual environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set your API key
Copy `.env.example` to `.env` and add your Groq API key:
```bash
cp .env.example .env
```
Then open `.env` and replace the placeholder:
```
GROQ_API_KEY=your_actual_groq_api_key_here
```
> Get a free API key at [console.groq.com](https://console.groq.com)

### 5. Run the app
```bash
python run.py
```
This launches the Streamlit app in your browser at `http://localhost:8501`.

---

## 🛠️ Tech Stack

| Technology | Usage |
|------------|-------|
| Python | Core language |
| Streamlit | Web UI framework |
| Groq API | LLM inference (llama-3.1-8b-instant) |
| pymupdf4llm | PDF → Markdown extraction |
| python-pptx | PowerPoint text extraction |
| python-dotenv | API key management |

---

## 📦 Dependencies

```
streamlit
pymupdf4llm
python-pptx
groq
python-dotenv
```

---

## 👤 Author

**Muhammad Shafay**  
CS Student · 2025

---

## 📄 License

This project is for educational purposes only.
