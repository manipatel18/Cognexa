import streamlit as st 
from utils.improve import answer_improvement
from utils.ui import apply_common_css

st.set_page_config(
    page_title="Answer Improvement",
    page_icon="✏️",
    layout="wide",
)

apply_common_css()


st.title("✏️ Answer Improvement")

st.markdown("*Paste your notes below and lets AI Enhancement .*")

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

# bottom
if st.button(" Enhance ", use_container_width=True):

    # validation
    if not notes.strip():
        st.warning("⚠️ Please enter notes before clicking Enhance Notes button.")

    else:
        with st.spinner("Improving answer...."):

            try:
                Improved = answer_improvement(notes, level)

                st.session_state["Improved_answer"] = improved

                st.success(" ✅ Notes Enhanced Successfully!")
               
        
            except Exception as e:
                st.error(f"Unable to improve answer: {e}")
# Display saved result
if "Improved_answer" in st.session_state:

    st.subheader("✨ Improved Answer")

    st.info(
        st.session_state["Improved"]
    )