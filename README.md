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

### File Structure

```
html/
├── index.html          ← Home page
├── calendar.html       ← Team calendar
├── contact.html        ← Contact / Join Us
└── assets/
    ├── style.css       ← All styles (colors, fonts, layout)
    └── images/
        └── hawk-logo.png
```

**Important:** If you add a new page, make sure to add it to the navigation in `style.css` and link it from every other page's `<nav>` section.

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
3. The workflow calls a webhook on the team's OrangePi5 home server
4. The Pi pulls the latest code from GitHub
5. Nginx (the web server) restarts with the new files
6. The live site updates — usually within 30 seconds of merging

The server runs at home on an OrangePi5 and is accessible worldwide via Cloudflare Tunnel at `frc8726.org`.

---

### Getting Help

- **Discord** — post in the appropriate channel if you're stuck
- **Coach Holmes** — [joshua.holmes@fcps.org](mailto:joshua.holmes@fcps.org)
- **Team email** — [urbanahsrobotics@gmail.com](mailto:urbanahsrobotics@gmail.com)
- **GitHub Docs** — [docs.github.com](https://docs.github.com) is actually really good

If you break something, don't panic. That's what branches and Pull Requests are for — nothing gets to the live site without approval.

---

*Built and maintained by the CryptoHawks Partner Relations Sub-Team*  
*FRC Team 8726 · Urbana High School · Ijamsville, MD*
