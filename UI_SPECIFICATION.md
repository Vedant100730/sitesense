# SiteSense UI/UX Specification Guide

This document defines the comprehensive UI/UX design system for the **SiteSense AI** platform. It covers the visual language, component geometry, layout architecture, and dynamic behavior to ensure a premium, consistent, and "wow" experience across the entire project.

---

## 1. Design Philosophy
SiteSense uses a **Modern Professional** aesthetic, combining "Glassmorphism" elements with a sleek, data-driven layout. The design is built on **Shadcn/UI** and powered by **Tailwind CSS v4** with **OKLCH** color tokens for superior color reproduction and accessibility.

---

## 2. Color Palette (OKLCH System)
SiteSense utilizes a dynamic color system that adapts perfectly to Light and Dark modes.

### A. Base Colors
| Element | Light Mode (OKLCH) | Dark Mode (OKLCH) |
| :--- | :--- | :--- |
| **Background** | `oklch(1 0 0)` | `oklch(0.145 0 0)` |
| **Foreground** | `oklch(0.145 0 0)` | `oklch(0.985 0 0)` |
| **Primary** | `oklch(0.205 0 0)` | `oklch(0.922 0 0)` |
| **Secondary** | `oklch(0.97 0 0)` | `oklch(0.269 0 0)` |
| **Destructive**| `oklch(0.577 0.245 27.325)`| `oklch(0.704 0.191 22.216)`|
| **Sidebar** | `oklch(0.985 0 0)` | `oklch(0.205 0 0)` |

---

## 3. Component Geometry (Shapes & Sizes)
SiteSense prioritizes soft edges and modern spacing for a premium feel.

### B. Shapes (Corner Radii)
- **Base Radius (`--radius`)**: `0.625rem` (10px)
- **Buttons**: `rounded-lg` (Matches base radius).
- **Cards**: `rounded-xl` (14px) or `rounded-2xl` (18px) for major containers.
- **Input Fields**: `rounded-md` (8px).
- **Badges**: `rounded-full` (Capsule shape).

### C. Button Variants (Dynamic Behavior)
All buttons feature a `transition-all` effect and an active state that shifts the element down slightly (`active:translate-y-px`) for a tactile feel.

1.  **Default**: High contrast (Primary background).
2.  **Outline**: Border-heavy, minimalist.
3.  **Secondary**: Subtle background for less critical actions.
4.  **Ghost**: Transparent background, reveals on hover (Used for navigation and utility).
5.  **Destructive**: Red-toned, used for deletions.

---

## 4. Layout Architecture (Locations)
The interface is divided into functional zones that remain consistent across all dashboard routes.

### D. Main Viewport Locations
| Zone | Location | Description |
| :--- | :--- | :--- |
| **Sidebar** | **Fixed Left** | Width: `w-72` (288px). Contains Branding, Bot Selection, and Main Navigation. |
| **Top Header** | **Top Right** | Contains **Breadcrumbs** for secondary navigation and user context. |
| **Central Content**| **Center/Right** | The main utility area. Padded with `px-8 py-6` for readability. |
| **Footer (Nav)** | **Sidebar Bottom**| Contains "Sign Out" and versioning/metadata. |

---

## 5. Dynamic & Interactive Elements
The UI is designed to feel alive and responsive.

- **Navigation Hover**: Nav items in the sidebar use `hover:bg-sidebar-accent` with a smooth `0.2s` transition.
- **Interactive States**:
    - **Active Link**: High-contrast background in sidebar navigation.
    - **Loading States**: Custom **Skeleton** loaders for table data and statistics cards.
    - **Micro-Animations**: Uses `tw-animate-css` for entry animations on dashboard cards.
- **Responsiveness**:
    - Sidebar transitions from `fixed` to `hidden` (collapsible) on mobile viewports.
    - Content uses `max-w-7xl` containers to maintain optimal line length on wide screens.

---

## 6. Typography
- **Primary Font**: Sans-serif (`var(--font-sans)`). Recommended: **Geist** or **Inter**.
- **Weights**:
    - **400 (Regular)**: Body text, secondary labels.
    - **500 (Medium)**: Buttons, navigation labels.
    - **600 (Semibold)**: Page titles, emphasis.
- **Monospace**: Used for API keys and code snippets (`var(--font-mono)`).

---

## 8. Page-by-Page Breakdown
This section details the functional and visual requirements for every core route in the application.

### A. Landing Page (`/`)
*   **Purpose**: Product awareness and high-conversion landing.
*   **Header**: Sticky navigation with Glassmorphism blur, Logo (SiteSense), Features link, Pricing link, and a "Get Started" CTA button.
*   **Hero Section**: Large sans-serif heading (`text-5xl` to `text-6xl`) with dynamic text color. Centered "Start for Free" CTA. Animated background mesh.
*   **Feature Grid**: 3-column layout showcasing RAG (Retrieval-Augmented Generation), Multi-Source Ingestion, and Custom Styling.
*   **Footer**: Links to Docs, Twitter, GitHub, and Trademark info.

### B. Login & Authentication (`/login`)
*   **Purpose**: Secure user entry.
*   **Layout**: Vertically and horizontally centered `max-w-md` card.
*   **Auth Methods**:
    - Email/Password form with validation.
    - OAuth Social login buttons (GitHub/Google) with high-contrast icons.
*   **Dynamics**: Smooth loading spinners on submission; Toast notifications for auth errors.

### C. Dashboard Overview (`/dashboard`)
*   **Purpose**: Application cockpit and bot selection.
*   **State Management**:
    - **No Bot Selected**: Dynamic "Action Required" alert prompting the user to select or create a bot.
    - **Active Bot**: Summary metrics (Total Chats, Sources, Accuracy Score).

### D. Bots Management (`/dashboard/bots`)
*   **Purpose**: Create and configure AI assistants.
*   **View**: Responsive grid of cards (`grid-cols-2`).
*   **Bot Cards**:
    - Header: Bot name + color indicator circle + "Copy ID" icon button.
    - Body: Mono-font Bot ID badge, Date Created.
    - Footer: Grouped buttons for **Edit**, **Delete**, **View Sources**, and **Get Embed Code**.
*   **Creation Modal**: Multi-field form including:
    - **Identity**: Bot Display Name, Assistant Name.
    - **Messaging**: Welcome Message, Fallback Message.
    - **Branding**: Native color picker for primary theme color.
    - **Intelligence**: LLM Provider (Anthropic/Google) and Model selectors.
    - **Security**: "Allowed Origins" whitelist input field.

### E. Knowledge Sources (`/dashboard/sources`)
*   **Purpose**: Ingest data for the RAG pipeline.
*   **Left/Top Section**: Split card layout.
    - **Website Ingestion**: URL input field with "Source Name" override.
    - **File Upload**: Drag-and-drop zone with dashed borders. Supports PDF, TXT, MD, CSV, XLSX.
*   **Status Table**:
    - Columns: Name, Type (with icons), Status Badge, Chunk Count, Last Indexed.
    - **Status Badges**:
        - `Pending`: Gray/Muted.
        - `Indexing`: Amber with spinner.
        - `Indexed`: Emerald green (High success).
        - `Failed`: High-contrast Red.
*   **Actions**: Individual **Re-index** (refresh icon) and **Delete** (trash icon) for each row.

### F. Embed Configuration (`/dashboard/embed`)
*   **Purpose**: Easy integration for end-users.
*   **Code Block**: Syntax-highlighted `<script>` block with `activeTenant` data-attributes auto-populated.
*   **Widget Preview**: A simulated website window showing:
    - The floating chat bubble in the bottom right.
    - The chat window with custom branding applied.
*   **Instructions**: Ordered list of steps for deployment.

### G. Analytics & Usage (`/dashboard/analytics`)
*   **Purpose**: Track bot performance and user interactions.
*   - **Charts**: Shadcn-integrated line charts for "Messages per Day" and "Inquiry Volume".
*   - **Stats Cards**: Big, bold numbers for "Active Users", "Total Tokens Used", and "Avg. Response Time".

---

## 9. Dynamic UI Rules for Development
When adding new features, follow these geometry and spacing rules:
1.  **Spacing Grid**: Use `gap-4` (1rem) for basic layout and `gap-6` (1.5rem) for section division.
2.  **Elevation**: Avoid heavy shadows. Use `border-border` with subtle `ring` colors for depth.
3.  **Iconography**: Use **Lucide React** icons at `size-4` (16px) for standard buttons and `size-5` (20px) for header elements.
