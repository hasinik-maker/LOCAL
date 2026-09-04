import streamlit as st

from utils.data import (
    CATEGORIES,
    init_session_state,
    load_experiences,
    personalization_reason,
    save_experience,
    unsave_experience,
    is_saved,
)
from utils.styling import inject_css, eyebrow, divider, tag

st.set_page_config(
    page_title="Local Tourism Explorer",
    page_icon="🧭",
    layout="wide",
    initial_sidebar_state="collapsed",
)

inject_css()
init_session_state()

experiences = load_experiences()

# ---------- HERO ----------
st.markdown(
    """
    <div style="padding: 60px 0 20px 0;">
        <div class="lux-eyebrow">LOCAL TOURISM EXPLORER</div>
        <h1 style="font-size: 3.2rem; margin-bottom: 6px;">Travel beyond the tourist trail.</h1>
        <p style="font-size: 1.15rem; color: #4a4640; max-width: 620px;">
            Discover authentic local experiences, hidden gems, and stories worth exploring —
            chosen and verified by the people who actually live there.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

with st.container():
    eyebrow("WHERE ARE YOU GOING?")
    c1, c2, c3, c4 = st.columns([2, 2, 2, 1])
    with c1:
        destination = st.text_input("Destination", placeholder="e.g. Hyderabad", label_visibility="collapsed")
    with c2:
        exp_type = st.selectbox("Experience", ["Any experience"] + CATEGORIES, label_visibility="collapsed")
    with c3:
        date = st.date_input("Date", label_visibility="collapsed")
    with c4:
        search_clicked = st.button("Explore", use_container_width=True)

    if search_clicked:
        st.switch_page("pages/1_Explore.py")

st.markdown(
    f"{tag('Local experiences')} {tag('Verified hosts')} {tag('Personalised recommendations')}",
    unsafe_allow_html=True,
)

divider()

# ---------- PICKED FOR YOU ----------
eyebrow("PICKED FOR YOU")
reason = personalization_reason()
if reason:
    st.caption(reason)
else:
    st.caption("Tell us what you're into to personalise this list — visit Onboarding in the sidebar.")

cols = st.columns(len(experiences))
for col, exp in zip(cols, experiences):
    with col:
        st.image(exp["image"], use_container_width=True)
        st.markdown(f"**{exp['name']}**")
        st.caption(f"📍 {exp['location']}")
        price_str = "Free" if exp["price"] == 0 else f"₹{exp['price']}"
        st.markdown(
            f"⭐ {exp['rating']} · {exp['review_count']} reviews &nbsp;·&nbsp; {price_str}",
        )
        saved_now = is_saved(exp["id"])
        btn_label = "♥ Saved" if saved_now else "♡ Save"
        if st.button(btn_label, key=f"home_save_{exp['id']}"):
            if saved_now:
                unsave_experience(exp["id"])
            else:
                save_experience(exp["id"])
            st.rerun()
        if st.button("View details", key=f"home_view_{exp['id']}", use_container_width=True):
            st.session_state.selected_experience_id = exp["id"]
            st.switch_page("pages/3_Experience_Detail.py")

divider()

# ---------- EXPLORE BY INTEREST ----------
eyebrow("EXPLORE BY INTEREST")
st.markdown("### What moves you?")

interest_lines = {
    "Food & Culture": "Street food walks, home-cooked dinners, market tastings",
    "Hidden Gems": "Places most travellers never find",
    "Adventure": "Trails, water, and things that get your heart rate up",
    "Art & Crafts": "Learn from artisans working the way their families always have",
    "Nature": "Sunrise viewpoints, quiet trails, open air",
    "Nightlife": "Where the city actually goes after dark",
    "Local Markets": "Real prices, real produce, real neighbourhood life",
    "History": "The story behind the street, not just the monument",
}

grid_cols = st.columns(4)
for i, cat in enumerate(CATEGORIES):
    with grid_cols[i % 4]:
        st.markdown(
            f"""
            <div class="lux-card" style="text-align:left; min-height: 110px;">
                <strong>{cat}</strong><br>
                <span class="lux-caption">{interest_lines[cat]}</span>
            </div>
            """,
            unsafe_allow_html=True,
        )

divider()

# ---------- HIDDEN GEMS ----------
eyebrow("PLACES TOURISTS USUALLY MISS")
st.markdown("### Hidden gems")

gems = [e for e in experiences if e.get("hidden_gem")]
gcols = st.columns(len(gems)) if gems else []
for col, exp in zip(gcols, gems):
    with col:
        st.image(exp["image"], use_container_width=True)
        st.markdown(f"**{exp['name']}**")
        st.caption(f"📍 {exp['location']}")
        st.markdown(f'<span class="lux-quote">{exp["why_hidden"]}</span>', unsafe_allow_html=True)
        if st.button("Explore", key=f"gem_{exp['id']}"):
            st.session_state.selected_experience_id = exp["id"]
            st.switch_page("pages/3_Experience_Detail.py")

st.markdown("<br><br>", unsafe_allow_html=True)
st.caption(
    "Use the sidebar to open Explore, the Map, your Saved collections, the Trip Planner, or Onboarding."
)
