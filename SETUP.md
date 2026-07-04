# SiteSense AI - Setup Guide

Welcome to the comprehensive setup guide for SiteSense AI. This guide will walk you through the entire process of setting up the platform locally and preparing it for deployment.

## Tech Stack Overview

- **Frontend**: Next.js 16 (App Router), Tailwind CSS 4, shadcn/ui
- **Backend**: FastAPI, Python 3.11, Uvicorn
- **Database & Auth**: Supabase (PostgreSQL + RLS)
- **Vector DB**: Pinecone
- **Embeddings**: Voyage AI (Default) / OpenAI
- **LLM/Generation**: Claude (Anthropic), Gemini (Google), OpenRouter

---

## 1. Prerequisites & API Keys

Before starting, ensure you have the following installed:
- **Node.js** (v18 or higher)
- **Python** (v3.11 or higher)
- **Git**

You will also need to create accounts and gather API keys for the following services:

1. **Supabase**: [supabase.com](https://supabase.com) (Database, Auth)
   - Create a new project.
   - You will need the **Project URL**, **Anon Key**, and **Service Role Key**.
2. **Pinecone**: [pinecone.io](https://pinecone.io) (Vector Database)
   - Create a free serverless index.
   - Dimensions: `1024` (if using Voyage AI `voyage-02` embeddings).
   - Metric: `Cosine`.
   - You will need the **API Key** and **Index Name**.
3. **Voyage AI**: [dash.voyageai.com](https://dash.voyageai.com) (Embeddings)
   - You will need the **API Key**.
4. **LLM Provider**: (Choose one or more)
   - **Google Gemini**: [aistudio.google.com](https://aistudio.google.com/)
   - **Anthropic Claude**: [console.anthropic.com](https://console.anthropic.com/)
   - **OpenRouter**: [openrouter.ai](https://openrouter.ai/)

---

## 2. Supabase Database Setup

SiteSense AI uses Supabase for all relational data and authentication.

1. Log into your Supabase dashboard and select your project.
2. Go to the **SQL Editor** in the left sidebar.
3. Open the file `supabase/schema.sql` from this repository.
4. Paste the contents into the SQL Editor and click **Run**.
   - *This will create all necessary tables (users, tenants, conversations, etc.) and configure Row Level Security (RLS) policies.*

---

## 3. Backend Setup (FastAPI)

The backend handles document ingestion, vectorization, and the RAG pipeline.

1. **Navigate to the backend directory**:
   ```bash
   cd backend
   ```

2. **Create a Python Virtual Environment**:
   ```bash
   python -m venv .venv
   ```

3. **Activate the Virtual Environment**:
   - On Windows: `.venv\Scripts\activate`
   - On macOS/Linux: `source .venv/bin/activate`

4. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   playwright install chromium
   ```

5. **Configure Environment Variables**:
   Copy the example environment file:
   ```bash
   cp .env.example .env
   ```
   Open `.env` and fill in your actual keys:
   - `SUPABASE_URL`
   - `SUPABASE_SERVICE_KEY`
   - `PINECONE_API_KEY`
   - `PINECONE_INDEX_NAME`
   - `VOYAGE_API_KEY`
   - *Add any LLM keys you wish to use by default.*

6. **Start the Backend Server**:
   ```bash
   python main.py
   # Or directly: uvicorn main:app --reload --port 8000
   ```
   *The backend will be running at `http://localhost:8000`.*

---

## 4. Frontend Setup (Next.js)

The frontend is the admin portal and dashboard for tenant management.

1. **Navigate to the frontend directory** (in a new terminal):
   ```bash
   cd frontend
   ```

2. **Install Dependencies**:
   ```bash
   npm install
   ```

3. **Configure Environment Variables**:
   Copy the example environment file:
   ```bash
   cp .env.example .env.local
   ```
   Open `.env.local` and fill in your Supabase keys:
   - `NEXT_PUBLIC_SUPABASE_URL`
   - `NEXT_PUBLIC_SUPABASE_ANON_KEY`

4. **Start the Development Server**:
   ```bash
   npm run dev
   ```
   *The frontend will be running at `http://localhost:3000`.*

---

## 5. Running the Application

With both the frontend and backend running:

1. Open [http://localhost:3000](http://localhost:3000) in your browser.
2. Create an account or log in via the Supabase Auth UI.
3. Create your first Bot (Tenant).
4. Go to the **Sources** tab and upload a document or enter a website URL to crawl.
5. Wait for the ingestion pipeline to complete (you can monitor the backend terminal logs).
6. Go to the **Embed** tab, copy the widget script, and test your chatbot!

---

## 6. Troubleshooting Common Issues

**Q: Ingestion fails or hangs when crawling websites.**
- Ensure you ran `playwright install chromium` in your backend virtual environment.

**Q: The chatbot says "I don't have information on that topic" for everything.**
- Check your Pinecone dashboard to ensure vectors were actually upserted.
- Ensure your Voyage AI API key is valid.

**Q: Supabase Auth fails to sign in/up.**
- Ensure your `NEXT_PUBLIC_SUPABASE_URL` and `NEXT_PUBLIC_SUPABASE_ANON_KEY` are exactly correct without trailing spaces.

**Q: Vector Dimension Mismatch Error.**
- Ensure your Pinecone index was created with exactly `1024` dimensions if using the default `voyage-02` embedding model.

## 7. Production Deployment

For deploying the project to live servers, please refer to the [Deployment Guide](docs/deployment.md). We recommend **Vercel** for the frontend and **Render** or **Railway** for the FastAPI backend.
