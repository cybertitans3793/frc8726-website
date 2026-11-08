# CryptoHawks Blog — How to Write and Publish Posts

The blog is managed through a simple admin panel that lives at a private URL. You don't need to know HTML or Git to publish a blog post — just fill out a form and hit Publish.

---

## Accessing the Admin Panel

Go to: **[https://frc8726.org/admin](https://frc8726.org/admin)**

**Password:** ask Coach Holmes. This repo is public, so the password is never written here — please don't post it in GitHub, group chats, or anywhere online.

Enter the password and click **Log in**. You'll stay logged in for about 8 hours on that device. When you're done, click **Log out** (top right), especially on a shared or school computer.

If you type the wrong password 5 times, the login locks for 15 minutes.

---

## Writing a Blog Post

Once you're on the admin page, fill out the form:

### Fields

**Title**
The headline of your post. Keep it clear and descriptive.
- Good: `Kickoff Day 2025 — What We're Building`
- Bad: `cool stuff`

**Author**
Your name, or your role if you prefer.
- Examples: `Jane Smith`, `Marketing Sub-Team`, `Drive Team`

**Date**
Defaults to today. You can backdate a post if you're writing about something that already happened.

**Content**
The body of your post. Write in plain text — paragraphs will be preserved. You can use basic HTML tags if you know them:
- `<b>bold text</b>` → **bold text**
- `<i>italic text</i>` → *italic text*
- `<br>` → line break
- `<p>...</p>` → paragraph
- `<a href="https://example.com">link text</a>` → clickable link

Any other HTML (scripts, images, embeds, styles) is removed automatically when you publish.

Keep posts between 150–500 words for readability. Shorter is usually better.

**Photo (optional)**
Upload one photo per post. JPG or PNG only.
- The photo will be automatically resized to 1200px wide
- Use a landscape (horizontal) photo when possible — it looks better on the page
- Max file size: ~10MB before resizing

Hit **Publish Post** when you're done.

---

## After Publishing

Your post will:
1. Appear immediately on the blog page at `frc8726.org/blog`
2. Show up in the post list at the bottom of the admin panel
3. Have its own page at `frc8726.org/blog/posts/YYYY-MM-DD-your-title.html`

No approval needed — posts go live instantly. Write responsibly.

---

## Deleting a Post

While logged in, scroll to the bottom of the admin page to see all existing posts. Click **Delete** next to a post and confirm to remove it permanently.

**Deletion cannot be undone.** The post file and photo are both removed.

---

## What Makes a Good Blog Post

The blog is public — sponsors, parents, judges, and potential new members read it. Keep that in mind.

**Good post ideas:**
- Competition recaps (what happened, what we learned)
- Build season updates (what we're working on this week)
- Outreach event summaries
- Student spotlights (with permission)
- Behind the scenes — what does the programming sub-team actually do?

**Things to avoid:**
- Inside jokes that outsiders won't understand
- Anything that could embarrass a student or the team
- Posting without proofreading (use Grammarly or ask someone to read it first)
- Huge walls of text with no paragraph breaks

**A good post structure:**
1. One sentence hook — what happened or what is this about?
2. Two or three paragraphs of detail
3. One sentence takeaway or what's coming next
4. A photo if you have one

---

## Tips for Photos

- Shoot **landscape (horizontal)** — portrait photos get cropped awkwardly
- Natural light or good workshop lighting — avoid dark or blurry shots
- Show the robot, the work, or the team in action — not posed group shots
- Save as JPG under 10MB before uploading

---

*Blog admin powered by a Flask app running on the CryptoHawks home server (pimedia).*
