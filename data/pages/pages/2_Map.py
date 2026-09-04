import pandas as pd
import pydeck as pdk
import streamlit as st

from utils.data import init_session_state, load_experiences
from utils.styling import inject_css, eyebrow, divider

st.set_page_config(page_title="Map · Local Tourism Explorer", page_icon="🗺️", layout="wide")
inject_css()
init_session_state()

experiences = load_experiences()

eyebrow("NEARBY EXPERIENCES")
st.markdown(f"## {len(experiences)} experiences near you")

view_mode = st.radio("View", ["Map", "List"], horizontal=True, label_visibility="collapsed")

df = pd.DataFrame(
    [
        {
            "id": e["id"],
            "name": e["name"],
            "lat": e["lat"],
            "lon": e["lon"],
            "category": e["category"],
            "price": e["price"],
        }
        for e in experiences
    ]
)

if view_mode == "Map":
    col_map, col_list = st.columns([2, 1])

    with col_map:
        layer = pdk.Layer(
            "ScatterplotLayer",
            data=df,
            get_position="[lon, lat]",
            get_fill_color="[181, 83, 60, 200]",
            get_radius=90,
            pickable=True,
        )
        view_state = pdk.ViewState(
            latitude=df["lat"].mean(),
            longitude=df["lon"].mean(),
            zoom=11,
            pitch=0,
        )
        deck = pdk.Deck(
            layers=[layer],
            initial_view_state=view_state,
            tooltip={"text": "{name}\n{category}"},
            map_style="light",
        )
        st.pydeck_chart(deck, use_container_width=True)
        st.caption("Every pin here matches an experience in the list — click a name on the right for full details.")

    with col_list:
        st.markdown("#### All experiences")
        for i, exp in enumerate(experiences, start=1):
            st.markdown(f"**{i}. {exp['name']}**")
            st.caption(f"📍 {exp['location']} · {exp['category']}")
            if st.button("View details", key=f"map_view_{exp['id']}"):
                st.session_state.selected_experience_id = exp["id"]
                st.switch_page("pages/3_Experience_Detail.py")
            divider()

else:
    for exp in experiences:
        c1, c2 = st.columns([1, 3])
        with c1:
            st.image(exp["image"], use_container_width=True)
        with c2:
            st.markdown(f"### {exp['name']}")
            st.caption(f"📍 {exp['location']} · {exp['category']}")
            if st.button("View details", key=f"maplist_view_{exp['id']}"):
                st.session_state.selected_experience_id = exp["id"]
                st.switch_page("pages/3_Experience_Detail.py")
        divider()
