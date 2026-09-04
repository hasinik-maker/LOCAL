import streamlit as st

from utils.data import (
    CROWD_COLORS,
    CROWD_LABELS,
    get_experience_by_id,
    init_session_state,
    is_saved,
    load_experiences,
    save_experience,
    unsave_experience,
)
from utils.styling import inject_css, eyebrow, divider, crowd_dot

st.set_page_config(page_title="Experience · Local Tourism Explorer", page_icon="📖", layout="wide")
inject_css()
init_session_state()

exp_id = st.session_state.get("selected_experience_id")
experiences = load_experiences()

if not exp_id:
    st.info("Pick an experience from Explore, the Map, or Home first.")
    st.stop()

exp = get_experience_by_id(exp_id)
if not exp:
    st.error("That experience could not be found.")
    st.stop()

# ---------- GALLERY ----------
gallery = exp.get("gallery") or [exp["image"]]
gcols = st.columns(len(gallery))
for col, img in zip(gcols, gallery):
    with col:
        st.image(img, use_container_width=True)

# ---------- HEADER ----------
c1, c2 = st.columns([3, 1])
with c1:
    eyebrow(exp["category"])
    st.markdown(f"# {exp['name']}")
    st.caption(f"📍 {exp['location']}")
    price_str = "Free" if exp["price"] == 0 else f"₹{exp['price']}"
    st.markdown(
        f"⭐ {exp['rating']} · {exp['review_count']} reviews &nbsp;·&nbsp; "
        f"⏱ {exp['duration_minutes']} min &nbsp;·&nbsp; {price_str}"
    )
with c2:
    saved_now = is_saved(exp["id"])
    if st.button("♥ Saved" if saved_now else "♡ Save this experience", use_container_width=True):
        if saved_now:
            unsave_experience(exp["id"])
        else:
            save_experience(exp["id"])
        st.rerun()
    if st.button("Book Experience", use_container_width=True):
        st.session_state.selected_experience_id = exp["id"]
        st.switch_page("pages/5_Trip_Planner.py")

if exp.get("hidden_gem"):
    st.markdown(f'<span class="lux-quote">{exp["why_hidden"]}</span>', unsafe_allow_html=True)

divider()

# ---------- WHY LOCALS GO HERE ----------
eyebrow("WHY LOCALS GO HERE")
st.markdown(f'<div class="lux-quote">{exp["why_locals_go"]}</div>', unsafe_allow_html=True)

divider()

# ---------- EXPECTATION -> REALITY ----------
eyebrow("WHAT IT'S ACTUALLY LIKE")
er = exp["expectation_reality"]
er_cols = st.columns(4)
er_items = [
    ("🕐 Best time", er["best_time"]),
    ("👥 Crowd then", er["typical_crowd_at_best_time"]),
    ("💰 Cost", er["cost_range"]),
    ("🚶 Duration", er["duration"]),
    ("👗 Wear", er["dress_code"]),
    ("📸 Photo-worthy", "Yes" if er["photo_worthy"] else "Not especially"),
    ("⚠️ Note", er["notes"]),
    ("🏠 Crowd type", er["crowd_type"]),
]
for i, (label, value) in enumerate(er_items):
    with er_cols[i % 4]:
        st.markdown(f"**{label}**")
        st.caption(value)

st.markdown(f"**What you'll do:** {er['what_you_do']}")

divider()

# ---------- TRUST SIGNALS ----------
eyebrow("TRUST SIGNALS")
ts = exp["trust_signals"]
t1, t2, t3, t4, t5 = st.columns(5)
t1.metric("Verified visits", ts["verified_visits"])
t2.metric("Reviews (30d)", ts["reviews_last_30_days"])
t3.metric("With real photos", f"{ts['pct_reviews_with_photos']}%")
t4.metric("Local contributors", ts["local_contributors"])
t5.metric("Most recent review", f"{ts['most_recent_review_days_ago']}d ago")

divider()

# ---------- LOCAL TAKE ----------
lt = exp.get("local_take")
if lt:
    eyebrow("LOCAL TAKE")
    verdict = "❤️ Yes, worth it" if lt["recommend"] else "Mixed feelings"
    st.markdown(f"**Would a local recommend this? {verdict}**")
    st.markdown(f'<div class="lux-quote">"{lt["reason"]}" — {lt["reviewer_name"]}</div>', unsafe_allow_html=True)
    divider()

# ---------- CROWD LEVEL ----------
eyebrow("CURRENT CROWD LEVEL")
cl = exp["crowd_level"]
current_color = CROWD_COLORS[cl["current"]]
st.markdown(
    f"{crowd_dot(current_color)} **{CROWD_LABELS[cl['current']]} right now**",
    unsafe_allow_html=True,
)
for slot in cl["by_hour"]:
    color = CROWD_COLORS[slot["level"]]
    st.markdown(
        f"{crowd_dot(color)} {slot['range']} — {CROWD_LABELS[slot['level']]}",
        unsafe_allow_html=True,
    )

divider()

# ---------- BEFORE YOU GO ----------
eyebrow("BEFORE YOU GO")
byg = exp["before_you_go"]
b1, b2, b3, b4 = st.columns(4)
byg_items = [
    ("♿ Accessibility", "⭐" * byg["accessibility"] + "☆" * (5 - byg["accessibility"])),
    ("🚶 Walking", f"{byg['walking_time_minutes']} min"),
    ("🚻 Toilets", "Yes" if byg["toilets"] else "No"),
    ("🅿️ Parking", byg["parking"]),
    ("💳 Payment", byg["payment"]),
    ("🗣 Language", byg["language"]),
    ("🛡 Safety", byg["safety"]),
    ("🗓 Best season", byg["best_season"]),
]
for i, (label, value) in enumerate(byg_items):
    with [b1, b2, b3, b4][i % 4]:
        st.markdown(f"**{label}**")
        st.caption(value)

fam = "Family-friendly" if byg["family_friendly"] else "Not ideal for families"
solo = "Solo-friendly" if byg["solo_friendly"] else "Better with company"
st.caption(f"{fam} · {solo}")

divider()

# ---------- HOST ----------
host = exp.get("host")
if host:
    eyebrow("MEET YOUR LOCAL HOST")
    hc1, hc2 = st.columns([1, 3])
    with hc1:
        st.image(host["photo"], width=140)
    with hc2:
        badge = " ✓ Verified host" if host.get("verified") else ""
        st.markdown(f"**{host['name']}**{badge}")
        st.caption(host["bio"])
        st.caption(f"Speaks: {', '.join(host['languages'])}")
        st.caption(host["response_time"])
        if st.button("Message host"):
            st.session_state["chat_open_for"] = exp["id"]
            st.info("Chat opened — say hello! (Demo only: no message backend is wired up yet.)")
    divider()

# ---------- REVIEWS ----------
eyebrow("STORIES FROM FELLOW EXPLORERS")
st.markdown(f"### Reviews ({exp['review_count']})")
for r in exp["reviews"]:
    st.markdown(f"**{r['name']}** · ⭐ {r['rating']} · {r['days_ago']}d ago")
    st.write(r["text"])
    if r["photo_count"]:
        st.caption(f"📷 {r['photo_count']} photos attached")
    divider()
