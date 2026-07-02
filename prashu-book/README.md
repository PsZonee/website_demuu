# For Prashu 💌

A small notebook-themed website — twenty chapters of notes, poems, and letters, written by Sammu for Prashu.

## How to host this on GitHub (free, takes ~5 minutes)

1. **Create a new repository** on GitHub (e.g. `for-prashu`). Keep it Public (Pages requires a public repo on the free plan, unless you have GitHub Pro).
2. **Upload these files** to the repo, keeping the folder structure exactly as-is:
   ```
   index.html
   contents.html
   closing.html
   README.md
   assets/style.css
   chapters/01.html ... 20.html
   ```
   Easiest way: on the repo page, click **Add file → Upload files**, drag the whole `prashu-book` folder contents in, and commit.
3. Go to the repo's **Settings → Pages**.
4. Under **Build and deployment → Source**, choose **Deploy from a branch**.
5. Under **Branch**, choose `main` and folder `/ (root)`, then **Save**.
6. Wait ~1 minute, refresh the page — GitHub will show you a live link like:
   ```
   https://your-username.github.io/for-prashu/
   ```
7. Send her that link. That's it — the whole book lives there.

## Editing later

- All the writing lives in `build.py` inside the `CHAPTERS` list — edit the text there and re-run `python3 build.py` to regenerate the chapter pages, or just edit the files in `/chapters` directly (they're plain HTML).
- Colors, fonts, and spacing all live in `assets/style.css`.
- Want to add real photos later? Drop image files into a new `assets/photos/` folder and add `<img src="../assets/photos/yourfile.jpg" alt="...">` inside any chapter's `<article class="prose">` block.

## Structure

- `index.html` — the cover
- `contents.html` — table of contents
- `chapters/01.html` – `20.html` — the chapters
- `closing.html` — the final page
- `assets/style.css` — the whole design system (pink/blush notebook theme)
