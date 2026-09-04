import streamlit as st

from utils.data import (
    CATEGORIES,
    init_session_state,
    load_experiences,
    save_experience,
    unsave_experience,
    is_saved,
)
from utils.styling import inject_css, eyebrow, divider

st.set_page_config(page_title="Explore · Local Tourism Explorer", page_icon="🔎", layout="wide")
inject_css()
init_session_state()

experiences = load_experiences()

eyebrow("EXPLORE")
st.markdown("## All experiences")

with st.sidebar:
    st.markdown("### Filters")
    selected_categories = st.multiselect("Category", CATEGORIES)
    max_price = st.slider("Max price (₹)", 0, 1500, 1500, step=50)
    min_rating = st.slider("Minimum rating", 0.0, 5.0, 0.0, step=0.1)
    hidden_only = st.checkbox("Hidden gems only")

filtered = experiences
if selected_categories:
    filtered = [e for e in filtered if e["category"] in selected_categories]
filtered = [e for e in filtered if e["price"] <= max_price]
filtered = [e for e in filtered if e["rating"] >= min_rating]
if hidden_only:
    filtered = [e for e in filtered if e.get("hidden_gem")]

st.caption(f"{len(filtered)} experiences")
divider()

if not filtered:
    st.info("No experiences match these filters yet — try widening them.")

for exp in filtered:
    c1, c2 = st.columns([1, 2])
    with c1:
        st.image(exp["image"], use_container_width=True)
    with c2:
        st.markdown(f"### {exp['name']}")
        st.caption(f"📍 {exp['location']} · {exp['category']}")
        price_str = "Free" if exp["price"] == 0 else f"₹{exp['price']}"
        st.markdown(
            f"⭐ {exp['rating']} · {exp['review_count']} reviews &nbsp;·&nbsp; "
            f"{price_str} &nbsp;·&nbsp; {exp['duration_minutes']} min"
        )
        if exp.get("hidden_gem"):
            st.markdown(f'<span class="lux-quote">{exp["why_hidden"]}</span>', unsafe_allow_html=True)

        b1, b2, _ = st.columns([1, 1, 3])
        with b1:
            saved_now = is_saved(exp["id"])
            btn_label = "♥ Saved" if saved_now else "♡ Save"
            if st.button(btn_label, key=f"explore_save_{exp['id']}"):
                if saved_now:
                    unsave_experience(exp["id"])
                else:
                    save_experience(exp["id"])
                st.rerun()
        with b2:
            if st.button("View details", key=f"explore_view_{exp['id']}"):
                st.session_state.selected_experience_id = exp["id"]
                st.switch_page("pages/3_Experience_Detail.py")
    divider()
