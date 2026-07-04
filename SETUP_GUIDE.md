# 💻 SiteSense AI — Local Setup Guide

This guide will walk you through setting up the SiteSense AI platform on a new development machine.

---

## 📋 Prerequisites

Before you begin, ensure you have the following installed:
*   **Python 3.11+**: [Download here](https://www.python.org/downloads/)
*   **Node.js 18+**: [Download here](https://nodejs.org/)
*   **Git**: [Download here](https://git-scm.com/)
*   **Tesseract OCR**: Required for PDF image processing.
    *   **Windows**: Install via [UB-Mannheim](https://github.com/UB-Mannheim/tesseract/wiki).
    *   **Mac**: `brew install tesseract`
    *   **Linux**: `sudo apt install tesseract-ocr`

---

## 🛠️ 1. Backend Setup (Python/FastAPI)

1.  **Clone the Repository**:
    ```bash
    git clone <your-repo-url>
    cd SiteSence/backend
    ```

2.  **Create a Virtual Environment**:
    ```bash
    python -m venv .venv
    # Windows:
    .venv\Scripts\activate
    # Mac/Linux:
    source .venv/bin/activate
    ```

3.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    playwright install chromium
    ```

4.  **Environment Configuration**:
    Create a `.env` file in the `backend/` directory by copying `.env.example`:
    ```bash
    cp .env.example .env
    ```
    Fill in the following essential keys:
    *   `ANTHROPIC_API_KEY` or `GEMINI_API_KEY`
    *   `VOYAGE_API_KEY` (Required for embeddings)
    *   `SUPABASE_URL` & `SUPABASE_SERVICE_KEY` (From your Supabase Project)

5.  **Run the Backend**:
    ```bash
    python main.py
    ```
    The API will be available at `http://localhost:8000`.

---

## 🎨 2. Frontend Setup (Next.js)

1.  **Navigate to Frontend**:
    ```bash
    cd ../frontend
    ```

2.  **Install Dependencies**:
    ```bash
    npm install
    ```

3.  **Environment Configuration**:
    Create a `.env.local` file in the `frontend/` directory:
    ```bash
    cp .env.example .env.local
    ```
    Ensure these are set:
    *   `NEXT_PUBLIC_API_URL=http://localhost:8000`
    *   `NEXT_PUBLIC_SUPABASE_URL=your_supabase_url`
    *   `NEXT_PUBLIC_SUPABASE_ANON_KEY=your_supabase_anon_key`

4.  **Run the Dashboard**:
    ```bash
    npm run dev
    ```
    The Admin Portal will be available at `http://localhost:3000`.

---

## ☁️ 3. External Services Checklist

To make the platform functional, you need to configure these external accounts:

### **Supabase (Database & Auth)**
1.  Create a new project at [supabase.com](https://supabase.com).
2.  Run the SQL migration scripts found in the `/supabase` folder of this repo.
3.  Enable **Email Auth** in the Authentication settings.

### **AI Providers**
1.  **Anthropic/Google**: Get API keys for Claude or Gemini to power the chat.
2.  **Voyage AI**: Get an API key from [voyageai.com](https://www.voyageai.com/) for high-quality embeddings.

---

## 🐳 Optional: Running with Docker

If you prefer using Docker, you can start the entire stack (including ChromaDB) with one command:

```bash
docker-compose up --build
```

---

## ✅ Verification
1.  Open `http://localhost:3000` and create an admin account.
2.  Create a "New Bot".
3.  Add a "URL Source" and wait for indexing to finish.
4.  Test the chat in the "Widget Preview" tab.

---

> [!TIP]
> If you encounter issues with web scraping, ensure Playwright is correctly installed by running `playwright install`.
