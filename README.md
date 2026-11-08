# CryptoHawks FRC 8726 — Team Website

**Live site:** [frc8726.org](https://frc8726.org)  
**Team:** FRC 8726 CryptoHawks — Urbana High School, Ijamsville, MD  
**Motto:** "One Team, One Urbana"

---

## For Students — How to Contribute

This is the source code for the CryptoHawks team website. Students can contribute by editing HTML and CSS files. You do **not** need to know how to code to get started — even fixing a typo or updating a date is a real contribution.

### What You Need

1. A **GitHub account** — sign up free at [github.com](https://github.com)
2. **GitHub Desktop** — download free at [desktop.github.com](https://desktop.github.com) (recommended for beginners)
3. A text editor — **VS Code** is recommended, download free at [code.visualstudio.com](https://code.visualstudio.com)
4. Send your GitHub username to Coach Holmes so he can add you as a collaborator

---

### The Golden Rule

> **Never commit directly to `main`.** Always work on your own branch and submit a Pull Request.

Main is the live website. Anything merged to main goes live automatically within about 30 seconds. Coach Holmes reviews and approves all Pull Requests before they go live.

---

### Step-by-Step Workflow

#### First Time Setup (do this once)

1. Open **GitHub Desktop**
2. Click **File → Clone Repository**
3. Search for `frc8726-website` or paste the URL:  
   `https://github.com/cybertitans3793/frc8726-website`
4. Choose where to save it on your computer
5. Click **Clone**

You now have a local copy of the website on your computer.

#### Every Time You Want to Make a Change

**Step 1 — Get the latest version**
- In GitHub Desktop, make sure you're on the `main` branch
- Click **Fetch origin** then **Pull** to get any recent changes

**Step 2 — Create a new branch**
- Click **Current Branch → New Branch**
- Name it something descriptive like `update-sponsors-page` or `fix-team-page-typo`
- Click **Create Branch**

**Step 3 — Make your changes**
- Open the files in VS Code (or any text editor)
- Website files are in the `html/` folder
- Edit what you need to edit
- Save your files
- **Check it in your browser** before committing (see [Previewing](#previewing-your-changes) below)

**Step 4 — Commit your changes**
- Go back to GitHub Desktop
- You'll see your changed files listed on the left
- Write a short description of what you changed in the **Summary** box (e.g. "Updated sponsor logos")
- Click **Commit to your-branch-name**

**Step 5 — Push your branch**
- Click **Publish Branch** (or **Push Origin** if you've pushed before)
- This uploads your branch to GitHub

**Step 6 — Open a Pull Request**
- Click **Create Pull Request** in GitHub Desktop, or go to the repo on GitHub
- GitHub will show you a comparison of your changes
- Add a title and description explaining what you changed and why
- Click **Create Pull Request**

**Step 7 — Wait for approval**
- Coach Holmes will review your PR
- He may leave comments asking for changes
- Once approved, he'll merge it — your changes go live automatically!

---

### Previewing Your Changes

Don't double-click the `.html` files — they will open **without the header and footer** (see below for why). Instead:

1. Open a terminal in the `frc8726-website` folder (in VS Code: **Terminal → New Terminal**)
2. Run `python preview.py` (on a Mac or if that fails: `python3 preview.py`)
3. Your browser opens **http://localhost:8000** — that's your copy of the site
4. Edit, save, and refresh the browser to see changes
5. Press **Ctrl+C** in the terminal when you're done

You need Python 3 (free from python.org, or the Microsoft Store on Windows). The blog list will say it can't load posts — that's normal in preview, the posts only exist on the real server.

---

### File Structure

```
preview.py              ← Run this to preview the site on your computer
html/
├── index.html          ← Home page
├── team.html           ← Team / sub-teams
├── robots.html         ← Robots, newest first
├── sponsors.html       ← Sponsor logos by tier
├── outreach.html       ← Outreach programs
├── blog.html           ← Blog list (posts are made in the admin page, not here)
├── calendar.html       ← Embedded Google Calendar
├── contact.html        ← Contact form
├── join.html           ← Get Involved (students, mentors, sponsors)
├── xrp.html, lego.html ← Old fundraiser pages (not in the menu; flyer QR codes point here, don't delete)
├── 404.html            ← "Page not found" page (links must start with /)
├── sitemap.xml         ← Page list for Google — add new pages here too
├── robots.txt          ← Rules for search engine crawlers
├── partials/
│   ├── header.html     ← THE header + menu for every page
│   └── footer.html     ← THE footer for every page
└── assets/
    ├── style.css       ← Site-wide styles (colors, fonts, header, footer, buttons)
    ├── fonts/          ← Norwester title font (stored here so it can't disappear)
    └── images/         ← Photos and logos, sorted into folders
```

Every page starts with a comment explaining what's on it and how to change common things. Read it first!

---

### The Header and Footer (shared by every page)

The header (logo + menu) and footer are each in **one file**:

- `html/partials/header.html`
- `html/partials/footer.html`

Each page has an include line where the header/footer goes, e.g. `<!--#include virtual="/partials/header.html" -->`. The web server replaces that line with the file's contents before sending the page. **Change the partial once and every page updates.** Don't delete or edit the include lines.

- **Header/footer look** (colors, sizes): `assets/style.css`, sections **HEADER / NAV** and **FOOTER**
- **Current-page highlight** in the menu happens automatically — you don't need to do anything
- **Links in the partials start with `/`** (e.g. `/team`) so they work from every page, including blog posts

---

### Adding a New Page

1. Copy an existing simple page (e.g. `calendar.html`) and rename it, e.g. `awards.html`
2. Change the `<title>`, the description/`og:` lines, the page hero, and the content. Keep the two include lines
3. Add a menu link in `partials/header.html` and a footer link in `partials/footer.html` (`href="/awards"` — no `.html`)
4. Add the page to `html/sitemap.xml` so Google finds it
5. Preview it, then commit and open a Pull Request as usual

---

### Photos

Resize photos to about **1600px wide** and remove location data before adding them. Phone photos are huge (5–10 MB) and often contain GPS coordinates of where they were taken. Ask a mentor if you're not sure how.

---

### Brand Guidelines (Quick Reference)

| Element | Value |
|---|---|
| Primary color | Urbana Blue `#04003b` |
| Background | White `#ffffff` |
| Accent gray | `#9e9d9d` |
| Title font | Norwester |
| Body font | Exo |
| Team name | Always spelled **CryptoHawks** (capital C and H, one word) |

Full brand kit is available from the marketing sub-team lead.

---

### How the Deployment Works

For the curious — here's what happens when Coach Holmes merges a PR:

1. GitHub detects a push to `main`
2. GitHub Actions automatically runs the deploy workflow (`.github/workflows/deploy.yml`)
3. The workflow sends a **signed** request to a webhook on the team's home server (pimedia)
4. The server checks the signature, then pulls the latest code from GitHub
5. Nginx (the web server) serves the new files immediately — no restart, no downtime
6. The live site updates — usually within 30 seconds of merging

The server runs at home and is accessible worldwide via Cloudflare Tunnel at `frc8726.org`.

#### Deploy security (for admins)

- The webhook only deploys when the request is signed with a shared secret (HMAC-SHA256). Requests without a valid signature are rejected, so nobody else can trigger deploys.
- The secret lives in two places: the repo's **Settings → Secrets and variables → Actions** as `DEPLOY_WEBHOOK_SECRET`, and in the webhook config on the server. If you rotate it, update both.
- The deploy script lives on the server, **not in this repo**, on purpose: the webhook runs with admin rights, so merging a PR must never be able to change what it runs.
- If a deploy fails, check the **Actions** tab on GitHub — a red ❌ on "Deploy to pimedia" usually means the secret is missing or doesn't match.

---

*Built and maintained by the CryptoHawks Partner Relations Sub-Team*  
*FRC Team 8726 · Urbana High School · Ijamsville, MD*
