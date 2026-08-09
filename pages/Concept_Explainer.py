import streamlit as st 
from utils.explainer import generateConcept

st.set_page_config(
    page_title="Concept Explainer",
    page_icon="💡"
)


st.markdown("""
<style>
/* background */
[data-testid="stAppViewContainer"]{
    background-color:#FFF5EE;
}

/* title, write, */
h1, h2, h3, p{
    color:black !important;
}
header[data-testid="stHeader"]{
    background: transparent !important;
}
span[data-testid="stIconMaterial"] {
    color: black !important;
}
/* Hide Deploy button */
[data-testid="stAppDeployButton"] {
    display: none !important;
}
[data-testid="stMainMenu"] {
    display: none !important;
}

div[data-testid="stToolbar"] {
    right: -2rem;
    margin-top: 6.5rem;
}


/*  sidebar background */
section[data-testid="stSidebar"] {
    background-color:#F5F7FA;
}
section[data-testid="stSidebar"] *{
    color:black;
    border-radius: 20px;
}

/* textarea background */
div[data-testid="stTextAreaRootElement"] {
    background-color:white;
    color:black !important;
}
div[data-testid="stTextAreaRootElement"] textarea::placeholder {
    color:black !important;
}

/* Sidebar background */
section[data-testid="stSidebar"] {
    background-color: white;
    border-radius: 20px;
    
}

/* Sidebar text */
section[data-testid="stSidebar"] *{
    color: black;
    border-radius: 20px
}
section[data-testid="stSidebar"] ul li a {
    font-size: 20px !important;
    font-weight: 600 !important;
    padding: 12px 16px !important;

}
div[data-testid="stSidebarNavLinkContainer"] :hover{
    background-color:#E3F2FD;
}

div[data-testid="stExpander"] {
    background-color:transparent !important;
    
}
div[data-testid="stExpander"] summary{
    background-color:transparent !important;
    border:2px solid #ddd;

}
div[data-testid="stExpander"] *{
    font-size: 20px !important;
    font-weight: 600 !important;
    padding: 1px 16px !important;

}
div[data-testid="stAlertContainer"] p{
        font-size: 15px !important;
        font-weight: 400 !important;
        width:100%;
        border-radius:12px;
        padding:20px;
}


/* output level */
div[role="group"]:has(input[aria-label="Output Tone / Level"]) {
    background-color: #FFF5EE !important;
    border: 1px solid #ff6b6b !important;
    border-radius: 25px !important;
    overflow: hidden !important;
}
/* Each option */
div[role="option"] {
    color: black !important;
    background-color: #FFF5EE !important;
}
/* Hover */
div[role="option"]:hover {
    background-color: #E3F2FD !important;
}

/* summarize button */
div.stButton > button{
    background : #87CEFA;
    border-radius:12px;
    border:none;
}
div.stButton > button:hover{
    background:linear-gradient(10deg,#1D4ED8,#3730A0);

}
</style>
""", unsafe_allow_html=True
)


st.title("💡 Concept Explainer")

st.markdown(" *Paste your notes below and lets AI Explains .*")

level = st.sidebar.selectbox(
    "Output Tone / Level",
    ["Simple / Beginner-Friendly",
     "Standard Academic",
     "Advanced / Expert"],
    index=1,
    key="output_level"
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
                summary = generateConcept(notes, level)

                st.success(" ✅ Concept explained Successfully!")
                st.subheader("💡Explaination")
                st.info(summary)

            except Exception as e:
                st.error(e)
    st.Page(
        "pages/Answer_Improvement.py",
        title="Answer Improvement",
        icon=":material/edit:"
    )