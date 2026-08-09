import streamlit as st 
from utils.llm import summarize_notes
from utils.ui import apply_common_css


st.set_page_config(
    page_title="Notes Summarizer",
    page_icon="📄",
    layout="wide",
)

apply_common_css()

st.title("📝 Notes Summarizers")

st.markdown("*Paste your notes below and lets AI generate a concise summary.*")

level = st.sidebar.selectbox(
    "Output Tone / Level",
    ["Simple / Beginner-Friendly",
     "Standard Academic",
     "Advanced / Expert"],
    index=1
)

# text or paste here
notes = st.text_area(
    " ",
    height= 250,
    placeholder="paste your notes here...")

# bottom
if st.button(" Summarize Notes", use_container_width=True):

    # validation
    if not notes.strip():
        st.warning("⚠️ Please enter notes before clicking Summarize Notes button.")

    else:
        with st.spinner("Generating summary...."):

            try:
                summary = summarize_notes(notes, level)

                st.session_state[
                    "notes_summary"
                ] = summary

                st.success(" ✅ Summary Generated Successfully!")


            except Exception as e:
                st.error(f"Unable to summarize notes: {e}")
                
# Display saved result
if "notes_summary" in st.session_state:

    st.subheader("📋 Summary")

    st.info(
        st.session_state["notes_summary"]
    )





