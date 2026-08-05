import streamlit as st 
from utils.llm import summarize_notes

st.set_page_config(
    page_title="Notes Summarizer",
    page_icon="📄"


)

st.title("Notes Summarizers")

st.write("**Paste your notes below and lets AI generate a concise summary. **")

st.markdown("""
<style>
/* background */
[data-testid="stAppViewContainer"]{
    background-color:black;
}

h1{
    color:#1F2937;
}
div.stButton > button{
    background : #2563EB;
    border-radius:12px;
    border:none;
}

div.stButton > button:hover{
    background:linear-gradient(90deg,#1D4ED8,#3730A3);

}


</style>
""", unsafe_allow_html=True)


# text or paste here

notes = st.text_area(
    " ",
    height= 250,
    placeholder="paste your notes here...")




# bottom

if st.button(" Summarize Notes", use_container_width=True):

    # validation
    if notes.strip()=="":
        st.warning("⚠️ Please enter notes before clicking Summarize Notes button.")

    else:
        with st.spinner("Generating summary...."):

            try:
                summary = summarize_notes (notes)

                st.success(" ✅ Summary Generated Successfully!")
                st.subheader("📋 summary")
                st.info(summary)

            except Exception as e:
                st.error(e)


st.divider()

st.caption("Developed using Streamlit + LLM API")