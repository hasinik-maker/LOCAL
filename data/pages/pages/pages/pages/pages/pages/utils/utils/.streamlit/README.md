# Local Tourism Explorer

A Streamlit prototype of a luxury local-experience discovery platform — search, personalised picks,
hidden gems, an interactive map, deep trust signals per experience (verified visits, local take,
crowd level, "before you go" practicals), a trip planner, saved collections, and onboarding.

This is a **functioning MVP scaffold**, not a finished production product — it uses in-memory
session state (saved items, profile) that resets when the app restarts, and the sample data covers
4 experiences in Hyderabad so you can see every feature working end-to-end. Swap in your own data
and add a real database once you're ready to go further than a prototype.

## What's inside

- `app.py` — Home page (entry point)
- `pages/1_Explore.py` — Filterable listing of all experiences
- `pages/2_Map.py` — Interactive map + synced list, every pin clickable
- `pages/3_Experience_Detail.py` — Full detail page: trust signals, local take, crowd level, etc.
- `pages/4_Saved.py` — Folder-based saved collections
- `pages/5_Trip_Planner.py` — Dates, traveller count, recommendations, stays, cafés
- `pages/6_Onboarding.py` — Traveller type + trip feel + account
- `utils/data.py` — Data loading + session-state helpers
- `utils/styling.py` — Custom luxury CSS + shared UI helpers
- `data/experiences.json` — Sample dataset (edit or replace this to add real content)
- `.streamlit/config.toml` — Theme (colors, font)
- `requirements.txt`

## Deploy on Streamlit Community Cloud

1. Push this repo to GitHub (done, if you're reading this from the repo).
2. Go to share.streamlit.io and sign in with GitHub.
3. Click "Create app", pick this repository, set branch to `main` and main file path to `app.py`.
4. Click Deploy. You'll get a live `streamlit.app` link in 1–3 minutes.
5. Any future commit to `main` redeploys automatically.

## Next steps to take this from prototype to real product

- Replace the sample data in `data/experiences.json` with real content or a real database.
- Add real persistence for Saved items and Profile (currently resets on reload).
- Add real authentication.
- Replace the "Message host" and "Confirm trip plan" placeholders with real backends.
- Swap sample Unsplash image URLs for your own hosted photography.
