"""Data loading and shared session-state helpers for Local Tourism Explorer."""

import json
from pathlib import Path

import streamlit as st

DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "experiences.json"

CATEGORIES = [
    "Food & Culture",
    "Hidden Gems",
    "Adventure",
    "Art & Crafts",
    "Nature",
    "Nightlife",
    "Local Markets",
    "History",
]

CROWD_COLORS = {
    "green": "#4C7A51",
    "yellow": "#C9A227",
    "red": "#B5533C",
}

CROWD_LABELS = {
    "green": "Quiet",
    "yellow": "Moderate",
    "red": "Crowded",
}


@st.cache_data
def load_experiences():
    """Load the experience dataset once and cache it for the session."""
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def get_experience_by_id(exp_id: str):
    for exp in load_experiences():
        if exp["id"] == exp_id:
            return exp
    return None


def init_session_state():
    """Set up session-state containers used across pages. Call once per page."""
    if "saved" not in st.session_state:
        # folder name -> list of experience ids
        st.session_state.saved = {"My Hyderabad": []}
    if "profile" not in st.session_state:
        st.session_state.profile = {
            "name": "",
            "email": "",
            "age": None,
            "traveller_types": [],
            "trip_feel": [],
            "onboarded": False,
        }
    if "selected_experience_id" not in st.session_state:
        st.session_state.selected_experience_id = None


def save_experience(exp_id: str, folder: str = "My Hyderabad"):
    init_session_state()
    if folder not in st.session_state.saved:
        st.session_state.saved[folder] = []
    if exp_id not in st.session_state.saved[folder]:
        st.session_state.saved[folder].append(exp_id)


def unsave_experience(exp_id: str, folder: str = "My Hyderabad"):
    init_session_state()
    if folder in st.session_state.saved and exp_id in st.session_state.saved[folder]:
        st.session_state.saved[folder].remove(exp_id)


def is_saved(exp_id: str) -> bool:
    init_session_state()
    return any(exp_id in ids for ids in st.session_state.saved.values())


def personalization_reason():
    """Return a human-readable reason string based on the stored profile, or None."""
    profile = st.session_state.get("profile", {})
    types = profile.get("traveller_types", [])
    if not types:
        return None
    if len(types) == 1:
        return f"Because you told us you're a {types[0]}"
    return f"Because you told us you're a {types[0]} and a {types[1]}"
