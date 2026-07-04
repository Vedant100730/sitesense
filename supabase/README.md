# Supabase Setup

SiteSense AI uses **Supabase** (PostgreSQL + Auth) as its primary database and authentication provider.

## 🚀 Setup Steps

1. **Create Project**: Sign in to [supabase.com](https://supabase.com) and create a new project.
2. **Database Schema**:
   - Open the **SQL Editor** in the side menu.
   - Click **New Query**.
   - Copy and paste the contents of `schema.sql`.
   - **Run** the query to create all tables (tenants, sources, conversations, etc.).
3. **Authentication Settings**:
   - Go to **Authentication → Settings**.
   - Ensure **Email Auth** is enabled.
   - Set the **Site URL** to your frontend (e.g., `http://localhost:3000` or your Vercel URL).
4. **API Settings**:
   - Go to **Settings → API**.

## 🔑 Environment Variables
Copy these values into your `.env` (Backend) and `.env.local` (Frontend) files:

| Supabase Field | Environment Key |
|----------------|-----------------|
| Project URL | `SUPABASE_URL` |
| `anon` public key | `SUPABASE_ANON_KEY` |
| `service_role` secret | `SUPABASE_SERVICE_KEY` (Backend only) |
| JWT Secret | `SUPABASE_JWT_SECRET` (Backend only) |

## 🔒 Security
- **Backend**: Uses the `service_role` key to manage multi-tenant data securely.
- **Frontend**: Uses the `anon` key for user-side authentication and routing via the Supabase Auth SDK.
