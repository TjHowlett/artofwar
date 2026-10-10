# Art of War Daily

A daily reading page for Sun Tzu's *The Art of War* (Lionel Giles, 1910). One theme a day, discussed with modern corporate and personal applications, with follow-up questions by typing or speaking. Built phone-first for Chrome on Android.

- `index.html` is the whole app. Open it from a web server (or GitHub Pages). The book data is embedded in it.
- `aow-points.json`, `aow-themes.json`, `aow-links.json`, `aow-sources.json` are the source data.
- After editing any `aow-*.json`, run `python embed-data.py` to copy the data into `index.html`.
- The AI model name is the `MODEL` constant at the top of `index.html`.

Your Anthropic API key is typed into the page and kept only in that browser's local storage. It is never stored in this repository and never included in the page's backup file.

## Personal use only

This is a private reading tool for personal use. It is not for commercial use, resale or redistribution. It includes Lionel Giles's 1910 translation for personal study only; please don't copy or republish that text.
