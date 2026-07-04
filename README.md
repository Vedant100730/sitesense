# 🌐 SiteSense AI

> Open-source multi-tenant RAG chatbot platform.
> Train on your content. Deploy everywhere.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Next.js](https://img.shields.io/badge/Next.js-16-black)](https://nextjs.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.109+-blue)](https://fastapi.tiangolo.com)

## What is SiteSense AI?

SiteSense AI lets you create AI chatbots trained on your own websites and documents. Embed on any website with 2 lines of HTML. Each bot answers ONLY from your content — never hallucinates.

## ✨ Features

- 🤖 **Multi-tenant**: Create and manage multiple bots, each with an isolated knowledge base.
- 📄 **Rich Ingestion**: Supports websites, PDFs, and text documents.
- 🔍 **Accurate RAG**: Combines vector search with FlashRank reranking for best-in-class accuracy.
- 🔒 **Secure Widget**: 5-layer JWT security system prevents unauthorized usage and session hijacking.
- 🎨 **Branded Experience**: Fully customizable colors, bot name, and welcome/fallback messages.
- 📊 **Deep Analytics**: Track conversation volume, identified knowledge gaps, and captured leads.
- 🔑 **Your AI Keys**: Choose between Claude (Anthropic) or Gemini (Google) with your own API keys.

## 🛠 Tech Stack

| Layer | Technology |
|-------|-----------|
| **Frontend** | Next.js 16, Tailwind CSS 4, shadcn/ui |
| **Backend** | FastAPI, Python 3.11 |
| **AI/LLM** | Claude API / Gemini API / OpenRouter (Multi-provider) |
| **Embeddings** | Voyage AI (Default) / OpenAI (Fallback) |
| **Vector DB** | Pinecone |
| **Reranking** | FlashRank |
| **Database** | Supabase (PostgreSQL) |
| **Auth** | Supabase Auth (Admin Portal) |
| **Ingestion** | Crawl4AI, PyMuPDF |

## 🚀 Quick Start

### Prerequisites
- Python 3.11+
- Node.js 18+
- Supabase account (free tier)
- Pinecone account (free tier)
- One or more LLM API keys: [Anthropic](https://console.anthropic.com/), [Google Gemini](https://aistudio.google.com/), or [OpenRouter](https://openrouter.ai/)
- [Voyage AI](https://dash.voyageai.com/) API key (Recommended for embeddings)

### Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/sitesense
   cd sitesense
   ```

2. **Supabase Database**:
   - Create a new project at [supabase.com](https://supabase.com).
   - Navigate to the **SQL Editor** and run the contents of `supabase/schema.sql`.
   - Copy your project URL, Anon key, and Service Role key.



4. **Backend Setup**:
   ```bash
   cd backend
   cp .env.example .env
   # Edit .env with your API and Supabase keys
   pip install -r requirements.txt
   playwright install chromium
   uvicorn main:app --reload --port 8000
   ```

5. **Frontend Setup**:
   ```bash
   cd ../frontend
   cp .env.example .env.local
   # Edit .env.local with your Supabase keys
   npm install
   npm run dev
   ```

6. **Go Live**:
   Open [http://localhost:3000](http://localhost:3000), Register/Login, Create a bot, Add your sources, and Get your embed code.

## 📖 Documentation

- [Setup Guide](SETUP.md)
- [Architecture Guide](docs/architecture.md)
- [API Reference](docs/api-reference.md)
- [Deployment Guide](docs/deployment.md)
- [Widget Customization](docs/widget-customization.md)

## 🔗 Deployment

- **Frontend**: One-click deployment to **Vercel**.
- **Backend**: Container-ready for **Railway** or Koyeb via provided Dockerfile.
- **Database**: Managed and scaled by **Supabase**.

See the full [Deployment Guide](docs/deployment.md).

## 🤝 Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## 📄 License

SiteSense AI is open-source software licensed under the **MIT License**. See [LICENSE](LICENSE) for details.
