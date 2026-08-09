from pathlib import Path
import streamlit as st


@st.cache_data
def load_css():
    css_path = Path(__file__).resolve().parent.parent / "styles" / "common.css"
    return css_path.read_text(encoding="utf-8")


def apply_common_css():
    st.markdown(
        f"<style>{load_css()}</style>",
        unsafe_allow_html=True
    )