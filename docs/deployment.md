# Deployment Guide

Follow this guide to deploy SiteSense AI to production using **Supabase**, **Railway**, and **Vercel**.

## Prerequisites
- GitHub account + repository
- [Supabase](https://supabase.com) account (free tier)
- [Railway](https://railway.app) account (free tier)  
- [Vercel](https://vercel.com) account (free tier)
- API Keys: Anthropic/Gemini/Mistral (LLM) and Voyage AI/OpenAI (Embeddings)

---

## Step 1: Supabase Setup
1. Create a new project at [supabase.com](https://supabase.com).
2. Go to the **SQL Editor** in the side menu.
3. Run the contents of `supabase/schema.sql` to create the tables.
4. Go to **Authentication → Settings**. Add your Vercel URL (e.g., `https://your-app.vercel.app`) to the "Site URL".
5. Navigate to **Project Settings → API** and save:
   - `Project URL`
   - `Anon public key`
   - `Service role key` (KEEP SECRET)
   - `JWT Secret`

---

## Step 2: Deploy ChromaDB to Railway
1. **New project → Deploy from Docker image**.
2. Image: `chromadb/chroma:latest`.
3. Add a **Volume**: Mount to `/chroma/chroma`.
4. Set Environment variables:
   - `IS_PERSISTENT=TRUE`
   - `ANONYMIZED_TELEMETRY=FALSE`
5. Keep as a **PRIVATE** service (no public networking needed yet).
6. Copy the **internal URL** (e.g., `chromadb.railway.internal`).

---

## Step 3: Deploy FastAPI to Railway
1. **New service → Deploy from GitHub repo**.
2. Select root directory: `/backend` (Railway handles subdirectories).
3. Set the following environment variables:
   - `SUPABASE_URL=` (from Step 1)
   - `SUPABASE_ANON_KEY=` (from Step 1)
   - `SUPABASE_SERVICE_KEY=` (from Step 1)
   - `SUPABASE_JWT_SECRET=` (from Step 1)
   - `VOYAGE_API_KEY=` (or OpenAI key)
   - `ANTHROPIC_API_KEY=` (or Gemini/Mistral)
   - `WIDGET_JWT_SECRET=` (generate a long random string)
   - `CHROMA_HOST=chromadb.railway.internal`
   - `CHROMA_PORT=8000`
   - `ENVIRONMENT=production`
   - `FRONTEND_URL=https://your-app.vercel.app`
4. Surface as a **PUBLIC** service.
5. Note the generated URL (e.g., `https://your-api.railway.app`).

---

## Step 4: Deploy Next.js to Vercel
1. Import your GitHub repository to Vercel.
2. Select the **Root Directory** as `frontend`.
3. Framework preset: **Next.js**.
4. Set the following environment variables:
   - `NEXT_PUBLIC_API_URL=https://your-api.railway.app`
   - `NEXT_PUBLIC_SUPABASE_URL=` (from Step 1)
   - `NEXT_PUBLIC_SUPABASE_ANON_KEY=` (from Step 1)
5. **Deploy**.

---

## Step 5: Final Configuration
1. Go back to Railway (FastAPI service) and update `FRONTEND_URL` to your production Vercel URL.
2. Ensure your Vercel URL is whitelisted in Supabase Auth.
3. Use the admin dashboard to create your first bot and configure "Allowed Origins".

---

## Local Development
To run the full stack locally:

1. **Start ChromaDB**:
   ```bash
   docker-compose up -d
   ```

2. **Backend**:
   ```bash
   cd backend
   uvicorn main:app --reload --port 8000
   ```

3. **Frontend**:
   ```bash
   cd frontend
   npm run dev
   ```
