from pathlib import Path
import streamlit as st



def show_loader(message="Loading Cognexa..."):
    loader = st.empty()


    return loader


@st.cache_data
def load_css():
    css_path = Path(__file__).resolve().parent.parent / "styles" / "common.css"
    return css_path.read_text(encoding="utf-8")


def apply_common_css():
    st.markdown(
        f"<style>{load_css()}</style>",
        unsafe_allow_html=True
    )