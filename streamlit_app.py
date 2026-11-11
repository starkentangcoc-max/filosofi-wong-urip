from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components


st.set_page_config(
    page_title="Ruang Makna — Kenali filosofi hidupmu",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
      #MainMenu, header, footer { visibility: hidden; }
      .block-container { max-width: 100%; padding: 0; }
      [data-testid="stAppViewContainer"] { background: #f5f2e9; }
      iframe { display: block; border: 0; }
    </style>
    """,
    unsafe_allow_html=True,
)

html_path = Path(__file__).with_name("index.html")
html = html_path.read_text(encoding="utf-8")

components.html(html, height=6000, scrolling=True)
