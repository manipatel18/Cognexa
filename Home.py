import streamlit as st 

st.set_page_config(
    page_title="Cognexa",
    page_icon="1",
    layout="wide"
)

st.title("Cognexa")

st.write("Welcome! This is the first version of the project.")

st.markdown("----")

st.header("Features")

col1, col2 = st.columns(2)

with col1:
    st.info(" 📄 notes summarizer")
    st.info(" ❓ AI Doubt solver")
    st.info(" 📝 Quiz Generator")

with col2:
    st.info("📅 Study Planner")
    st.info ("⏰ TImetable")
    st.info("📚 Assignment Helper")



