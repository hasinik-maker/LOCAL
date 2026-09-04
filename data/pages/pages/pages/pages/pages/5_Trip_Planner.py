import datetime as dt

import streamlit as st

from utils.data import init_session_state, load_experiences
from utils.styling import inject_css, eyebrow, divider

st.set_page_config(page_title="Trip Planner · Local Tourism Explorer", page_icon="🧳", layout="wide")
inject_css()
init_session_state()

experiences = load_experiences()

eyebrow("PLAN YOUR TRIP")
st.markdown("## Where and when are you going?")

c1, c2, c3 = st.columns(3)
with c1:
    destination = st.text_input("Destination", value="Hyderabad")
with c2:
    check_in = st.date_input("Check-in", value=dt.date.today())
with c3:
    check_out = st.date_input("Check-out", value=dt.date.today() + dt.timedelta(days=2))

travellers = st.number_input("Number of travellers", min_value=1, max_value=12, value=2)

trip_length = max((check_out - check_in).days, 0)
if trip_length <= 0:
    st.warning("Check-out should be after check-in.")
else:
    st.success(f"{trip_length}-day trip for {travellers} traveller(s) in {destination or 'your destination'}.")

    divider()
    eyebrow("RECOMMENDED FOR YOUR TRIP LENGTH")
    n_recommend = min(len(experiences), max(trip_length * 2, 2))
    recommended = experiences[:n_recommend]
    cols = st.columns(min(len(recommended), 4) or 1)
    for i, exp in enumerate(recommended):
        with cols[i % len(cols)]:
            st.image(exp["image"], use_container_width=True)
            st.markdown(f"**{exp['name']}**")
            st.caption(f"⏱ {exp['duration_minutes']} min · ⭐ {exp['rating']}")
            if st.button("View details", key=f"trip_view_{exp['id']}"):
                st.session_state.selected_experience_id = exp["id"]
                st.switch_page("pages/3_Experience_Detail.py")

    divider()
    eyebrow("NEARBY STAYS")
    stays = [
        {"name": "Falaknuma Heritage Homestay", "price": "₹4,200/night", "distance": "1.2 km from your experiences"},
        {"name": "Old City Boutique Inn", "price": "₹2,800/night", "distance": "0.6 km from your experiences"},
        {"name": "Banjara Hills Studio", "price": "₹3,500/night", "distance": "3.1 km from your experiences"},
    ]
    scols = st.columns(3)
    for col, stay in zip(scols, stays):
        with col:
            st.markdown(f"**{stay['name']}**")
            st.caption(f"{stay['price']} · {stay['distance']}")

    divider()
    eyebrow("NEARBY CAFÉS")
    cafes = ["Café Bahar (old-city classic)", "Blue Cup Coffee Roasters", "Nimrah Café & Bakery"]
    for cafe in cafes:
        st.markdown(f"- {cafe}")

    divider()
    if st.button("Confirm trip plan", use_container_width=False):
        st.balloons()
        st.success("Trip plan saved. (Demo only — no backend booking is wired up yet.)")
