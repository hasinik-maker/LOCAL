import streamlit as st

from utils.data import get_experience_by_id, init_session_state
from utils.styling import inject_css, eyebrow, divider

st.set_page_config(page_title="Saved · Local Tourism Explorer", page_icon="❤️", layout="wide")
inject_css()
init_session_state()

eyebrow("YOUR EXPLORER LIST")
st.markdown("## Saved")

tab_saved, tab_folders = st.tabs(["All saved", "Create a folder"])

with tab_folders:
    new_folder = st.text_input("Folder name", placeholder="e.g. Food, Culture, Weekend")
    if st.button("Create folder") and new_folder:
        st.session_state.saved.setdefault(new_folder, [])
        st.success(f"Created '{new_folder}'")
        st.rerun()

with tab_saved:
    total_saved = sum(len(v) for v in st.session_state.saved.values())
    if total_saved == 0:
        st.info("Nothing saved yet — tap ♡ on any experience to add it here.")

    for folder, ids in st.session_state.saved.items():
        if not ids:
            continue
        st.markdown(f"### {folder}")
        st.caption(f"{len(ids)} saved")
        cols = st.columns(min(len(ids), 4) or 1)
        for i, exp_id in enumerate(ids):
            exp = get_experience_by_id(exp_id)
            if not exp:
                continue
            with cols[i % len(cols)]:
                st.image(exp["image"], use_container_width=True)
                st.markdown(f"**{exp['name']}**")
                st.caption(f"📍 {exp['location']}")
                if st.button("View details", key=f"saved_view_{exp_id}_{folder}"):
                    st.session_state.selected_experience_id = exp_id
                    st.switch_page("pages/3_Experience_Detail.py")
        if len(ids) >= 3:
            st.markdown(
                f"💡 You have **{len(ids)} saved places** in *{folder}* — "
                f"want to turn them into a mini-experience?"
            )
            if st.button("Create a mini-experience", key=f"mini_{folder}"):
                st.session_state.trip_prefill = ids
                st.switch_page("pages/5_Trip_Planner.py")
        divider()
