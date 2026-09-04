import streamlit as st

from utils.data import init_session_state
from utils.styling import inject_css, eyebrow, divider

st.set_page_config(page_title="Onboarding · Local Tourism Explorer", page_icon="👤", layout="centered")
inject_css()
init_session_state()

eyebrow("BUILD YOUR EXPLORER PROFILE")
st.markdown("## What kind of traveller are you?")

traveller_types = st.multiselect(
    "Select all that apply",
    ["Foodie", "Explorer", "Culture Lover", "Nature Seeker", "Adventure Junkie",
     "Art & Craft Lover", "History Buff", "Night Owl"],
    default=st.session_state.profile.get("traveller_types", []),
    label_visibility="collapsed",
)

divider()
st.markdown("## What do you want your trip to feel like?")
trip_feel = st.multiselect(
    "Select all that apply",
    ["Relaxed", "Adventurous", "Social", "Cultural", "Unexpected", "Authentic"],
    default=st.session_state.profile.get("trip_feel", []),
    label_visibility="collapsed",
)

divider()
st.markdown("## A bit about you")
c1, c2 = st.columns(2)
with c1:
    name = st.text_input("Name", value=st.session_state.profile.get("name", ""))
    age = st.number_input(
        "Age", min_value=13, max_value=100,
        value=st.session_state.profile.get("age") or 25,
    )
with c2:
    email = st.text_input("Email", value=st.session_state.profile.get("email", ""))
    home_city = st.text_input("Home city (optional)")

if st.button("Build My Explorer Profile", use_container_width=True):
    st.session_state.profile = {
        "name": name,
        "email": email,
        "age": age,
        "home_city": home_city,
        "traveller_types": traveller_types,
        "trip_feel": trip_feel,
        "onboarded": True,
    }
    st.success(f"Welcome, {name or 'explorer'} — your recommendations are now personalised.")
    st.balloons()
