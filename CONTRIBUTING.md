# Contributing to SiteSense AI

Thank you for your interest in contributing to **SiteSense AI**! We're excited to have you.

## 🏁 Getting Started
1. **Fork** the repository on GitHub.
2. **Clone** your fork locally:
   ```bash
   git clone https://github.com/yourusername/sitesense-ai.git
   cd sitesense-ai
   ```
3. Follow the **Quick Start** instructions in the `README.md` to get both the backend and frontend running.
4. Create a new branch for your feature or fix:
   ```bash
   git checkout -b feature/my-new-feature
   ```

## 🛠 Development Guidelines

### Backend (Python/FastAPI)
- **Environment**: Python 3.11+.
- **Async First**: Use `async/await` for all non-blocking operations, especially DB and LLM calls.
- **Type Hinting**: Always include type hints for function arguments and return values.
- **Service Isolation**: Keep LLM providers, database logic, and ingestion pipelines separated in `backend/services/`.
- **Dependencies**: Add new packages via `requirements.txt`.

### Frontend (TypeScript/Next.js)
- **Environment**: Node 18+ / Next.js 16.
- **Styling**: Use **Tailwind CSS 4** and **shadcn/ui** components.
- **Type Safety**: Maintain **strict mode** for TypeScript; avoid using the `any` type.
- **Components**: Keep components focused, reusable, and stored in `frontend/components/`.

## 🚢 Pull Request Process
1. Ensure your code passes all linting tests.
2. Update the documentation in `docs/` or `PLATFORM_DETAILS.md` if you're changing the architecture.
3. Submit a Pull Request (PR) with a clear, descriptive title.
4. Provide a summary of the changes and why they are necessary.

## 🎨 Code Style
- **Python**: Follow [PEP 8](https://peps.python.org/pep-0008/) naming conventions.
- **TypeScript**: Use camelCase for variables/functions and PascalCase for components/types.
- **Commit Messages**: Write meaningful commit messages (e.g., `feat: add mistral support`, `fix: domain validation logic`).

## 🐞 Reporting Issues
- Use the **GitHub Issues** tab to report bugs or suggest enhancements.
- Provide clear steps to reproduce any issue, including environment details.

We appreciate your contributions!
