"""Custom CSS and small reusable UI components for the luxury visual language."""

import streamlit as st

CUSTOM_CSS = """
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@500;600;700&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">

<style>
:root {
    --cream: #FAF7F1;
    --ivory: #F3EEE4;
    --olive: #3D4A34;
    --forest: #2F3D28;
    --terracotta: #B5533C;
    --charcoal: #262322;
    --hairline: #E4DDCE;
}

html, body, [class*="css"]  {
    font-family: 'Inter', sans-serif;
    color: var(--charcoal);
}

.stApp {
    background-color: var(--cream);
}

h1, h2, h3, .lux-serif {
    font-family: 'Playfair Display', serif !important;
    color: var(--charcoal);
    letter-spacing: 0.2px;
}

.lux-eyebrow {
    font-family: 'Inter', sans-serif;
    text-transform: uppercase;
    letter-spacing: 2px;
    font-size: 0.72rem;
    color: var(--olive);
    font-weight: 600;
    margin-bottom: 6px;
}

.lux-card {
    background-color: #FFFFFF;
    border: 1px solid var(--hairline);
    border-radius: 14px;
    padding: 18px;
    margin-bottom: 18px;
    transition: box-shadow 0.25s ease, transform 0.25s ease;
}

.lux-card:hover {
    box-shadow: 0 8px 24px rgba(38, 35, 34, 0.08);
    transform: translateY(-2px);
}

.lux-tag {
    display: inline-block;
    background-color: var(--ivory);
    color: var(--olive);
    border-radius: 999px;
    padding: 3px 12px;
    font-size: 0.72rem;
    font-weight: 600;
    letter-spacing: 0.5px;
    margin-right: 6px;
}

.lux-divider {
    border: none;
    border-top: 1px solid var(--hairline);
    margin: 22px 0;
}

.lux-quote {
    border-left: 3px solid var(--terracotta);
    padding-left: 16px;
    font-family: 'Playfair Display', serif;
    font-style: italic;
    font-size: 1.05rem;
    color: var(--charcoal);
    margin: 10px 0;
}

.lux-caption {
    color: #6B6560;
    font-size: 0.82rem;
}

.crowd-dot {
    height: 10px;
    width: 10px;
    border-radius: 50%;
    display: inline-block;
    margin-right: 6px;
}

.stButton>button {
    border-radius: 999px;
    border: 1px solid var(--charcoal);
    background-color: var(--charcoal);
    color: var(--cream);
    padding: 8px 22px;
    font-weight: 500;
    transition: opacity 0.2s ease;
}

.stButton>button:hover {
    opacity: 0.85;
    border: 1px solid var(--charcoal);
    color: var(--cream);
}

section[data-testid="stSidebar"] {
    background-color: var(--ivory);
}
</style>
"""


def inject_css():
    st.markdown(CUSTOM_CSS, unsafe_allow_html=True)


def eyebrow(text: str):
    st.markdown(f'<div class="lux-eyebrow">{text}</div>', unsafe_allow_html=True)


def divider():
    st.markdown('<hr class="lux-divider">', unsafe_allow_html=True)


def tag(text: str):
    return f'<span class="lux-tag">{text}</span>'


def crowd_dot(color_hex: str):
    return f'<span class="crowd-dot" style="background-color:{color_hex};"></span>'
