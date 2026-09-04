Local Tourism Explorer
A Streamlit prototype of a luxury local-experience discovery platform — search, personalised picks,
hidden gems, an interactive map, deep trust signals per experience (verified visits, local take,
crowd level, "before you go" practicals), a trip planner, saved collections, and onboarding.
This is a functioning MVP scaffold, not a finished production product — it uses in-memory
session state (saved items, profile) that resets when the app restarts, and the sample data covers
4 experiences in Hyderabad so you can see every feature working end-to-end. Swap in your own data
and add a real database once you're ready to go further than a prototype.
What's inside
```
local-tourism-explorer/
├── app.py                        # Home page (entry point)
├── pages/
│   ├── 1_Explore.py              # Filterable listing of all experiences
│   ├── 2_Map.py                  # Interactive map + synced list, every pin clickable
│   ├── 3_Experience_Detail.py    # Full detail page: trust signals, local take, crowd level, etc.
│   ├── 4_Saved.py                # Folder-based saved collections
│   ├── 5_Trip_Planner.py         # Dates, traveller count, recommendations, stays, cafés
│   └── 6_Onboarding.py           # Traveller type + trip feel + account
├── utils/
│   ├── data.py                   # Data loading + session-state helpers
│   └── styling.py                # Custom luxury CSS + shared UI helpers
├── data/
│   └── experiences.json          # Sample dataset (edit or replace this to add real content)
├── .streamlit/
│   └── config.toml               # Theme (colors, font)
├── requirements.txt
└── .gitignore
```
---
A–Z: Get this running and live on the internet
Part 1 — Get the code
A. Install prerequisites (once, on your computer)
Install Python 3.10+ if you don't have it.
Install Git if you don't have it.
Create a free GitHub account if you don't have one.
B. Download this project to your computer
If you received it as a folder/zip: unzip it anywhere, e.g. `Documents/local-tourism-explorer`.
Part 2 — Run it locally first (confirm it works before publishing)
C. Open a terminal in the project folder
```bash
cd path/to/local-tourism-explorer
```
D. Create a virtual environment (keeps this project's packages separate from everything else on your machine)
```bash
python3 -m venv venv
```
E. Activate the virtual environment
macOS/Linux:
```bash
  source venv/bin/activate
  ```
Windows (PowerShell):
```powershell
  venv\Scripts\Activate.ps1
  ```
F. Install the dependencies
```bash
pip install -r requirements.txt
```
G. Run the app
```bash
streamlit run app.py
```
H. View it
Streamlit will open your browser automatically at `http://localhost:8501`. If it doesn't, open that URL manually.
Click through Explore, the Map, an experience's detail page, Saved, Trip Planner, and Onboarding to confirm everything works.
I. Stop the app
Press `Ctrl+C` in the terminal when you're done testing.
Part 3 — Put the code on GitHub
J. Create a new, empty repository on GitHub
Go to github.com/new.
Name it `local-tourism-explorer` (or anything you like).
Leave it empty — do not check "Add a README" (you already have one).
Click Create repository.
Keep the page open — you'll need the repository URL it shows you (something like
`https://github.com/your-username/local-tourism-explorer.git`).
K. Turn your local folder into a Git repository
```bash
git init
```
L. Tell Git who you are (only needed once per computer)
```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```
M. Stage and commit all the files
```bash
git add .
git commit -m "Initial commit: Local Tourism Explorer Streamlit app"
```
N. Point your local repo at the GitHub repo you created
```bash
git remote add origin https://github.com/your-username/local-tourism-explorer.git
```
(Replace the URL with the one from step J.)
O. Push your code up to GitHub
```bash
git branch -M main
git push -u origin main
```
P. Confirm it worked
Refresh the GitHub repository page in your browser — you should see all your files there.
Part 4 — Deploy it live with Streamlit Community Cloud (free)
Q. Go to Streamlit Community Cloud
Visit share.streamlit.io and sign in with your GitHub account.
R. Start a new app
Click Create app (or New app).
S. Connect your repository
Choose the `local-tourism-explorer` repository you just pushed.
Branch: `main`
Main file path: `app.py`
T. Deploy
Click Deploy. Streamlit Cloud will install your `requirements.txt` and start the app —
this usually takes 1–3 minutes the first time.
U. Get your live link
Once deployed, you'll get a public URL like `https://your-app-name.streamlit.app` — this is
the link you can share with anyone.
V. Redeploying after changes
Any time you want to update the live site: make your edits locally, then:
```bash
  git add .
  git commit -m "Describe what you changed"
  git push
  ```
Streamlit Cloud automatically redeploys within a minute or two of every push to `main`.
Part 5 — Next steps to take this from prototype to real product
W. Replace the sample data
Edit `data/experiences.json` to add your real experiences, or connect the app to a real database
(e.g. Supabase, Firebase, or Postgres) instead of a local JSON file.
X. Add persistence
Right now, Saved items and Profile data live in `st.session_state`, which resets whenever someone
reloads the app or a new session starts. For real users, connect these to a database keyed by a
logged-in user account.
Y. Add real authentication
The onboarding page collects name/email/age but doesn't actually create accounts. Add a proper
auth flow (e.g. `streamlit-authenticator`, or a hosted auth provider) if you want real logins.
Z. Add real photography, host messaging, and booking
Swap the sample Unsplash image URLs for your own licensed photography.
Replace the "Message host" placeholder with a real chat backend (e.g. Firebase, Supabase Realtime,
or a simple messages table + polling).
Replace the "Confirm trip plan" placeholder with a real booking/payment flow.
---
Notes
This uses pydeck for the interactive map — no API key required.
All images currently load from Unsplash URLs; swap these for your own hosted images before going live for real, since hotlinking isn't reliable long-term.
The custom "luxury" styling lives in `utils/styling.py` as injected CSS — Streamlit's own component
styling is limited, so this is the main lever for visual polish. Tweak colors/fonts there.
