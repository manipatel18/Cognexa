import streamlit as st 
from utils.explainer import generateConcept
from utils.ui import apply_common_css


st.set_page_config(
    page_title="Concept Explainer",
    page_icon="💡",
    layout="wide",
)

apply_common_css()


st.title("💡 Concept Explainer")

st.markdown(" *Paste your notes below and lets AI Explains .*")

level = st.sidebar.selectbox(
    "Output Tone / Level",
    ["Simple / Beginner-Friendly",
     "Standard Academic",
     "Advanced / Expert"],
    index=1,
)
# text or paste here
notes = st.text_area(
    " ",
    height= 250,
    placeholder="paste your notes here...")

# generate bottom
if st.button(" Explain ", use_container_width=True):

    # validation
    if notes.strip()=="":
        st.warning("⚠️ Please enter notes before clicking Explain Notes button.")

    else:
        with st.spinner("Generating summary...."):

            try:
                explanation = generateConcept(notes, level)

                st.session_state["concept_explanation"] = explanation

                st.success(" ✅ Concept explained Successfully!")


            except Exception as e:
                st.error(f"Unable to explain concept: {e}")

# Display saved result
if "concept_explanation" in st.session_state:

    st.subheader("💡 Explanation")
    st.info(
        st.session_state["concept_explanation"]
    )