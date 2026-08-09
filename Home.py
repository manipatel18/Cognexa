import streamlit as st 

st.set_page_config(
    page_title="Cognexa",
    page_icon="1",
    layout="wide",
    initial_sidebar_state="expanded"

)

st.markdown("""
<style>
.stApp {
    background-color: #FFF5EE;
}
h1, h2, h3, p {
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


/* columns background */
div[data-testid="stAlert"] *{
    background-color: white;
    color: black !important;
    border-radius: 13px;

    
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
        background:white;
        border-radius:12px;
        padding:20px;

}

/* arrow container*/
div[data-testid="stElementContainer"] p{
    background-color: white !important;
    color:grey !important;
    border: 1px solid #d9d9d9;
    border-radius: 12px;
    margin-top: 10px;
    width: 100%;
    box-sizing: border-box;
}
span[data-testid="stIconEmoji] {
    margin-top: 100rem;
}
""", unsafe_allow_html=True
)


st.image("images/logo111.png",width=350)

st.subheader("Welcome! This is the first version of the project.")



st.header("Features")

with st.expander("✏️Answer Improvement", expanded=False):


    with st.container(border=True):
        st.write("""
            The*Answer Improvement*feature uses AI to analyze and enhance user-provided answers. It improves clarity, grammar, structure, and overall presentation while preserving the original meaning. This helps users create more accurate, concise, and professional responses suitable for academic, professional, and general communication.
            """)
        st.page_link(
            "pages/Answer_Improvement.py",
            label="✏️"
        )

    

with st.expander("💡Concept Explainer",expanded=False):
    with st.container(border=True):
        st.write("""
        The *Concept Explainer* feature uses AI to simplify complex topics and explain them in a clear, structured, and easy-to-understand manner. It adapts explanations to the user's level of understanding and can provide examples, key points, and step-by-step explanations to support effective learning.
        """)




with st.expander("📝Notes Summarizer",expanded=False):
    with st.container(border=True):
        st.write("""
        The *Notes Summarizer* feature uses AI to analyze lengthy study materials and generate concise, well-structured summaries. It extracts important concepts, key points, definitions, and essential information, helping users save time and revise their study material more efficiently.
        """)
            
      

with st.expander("🧠 Quiz Generator",expanded=False):
    with st.container(border=True):
        st.write("""
            The *Quiz Generator* feature uses AI to automatically create quizzes from provided study material. It generates relevant questions based on the content and can include multiple-choice questions, answers, and explanations to help users test their knowledge and identify areas for improvement.
            """)

pages = [
    st.Page("Home.py", title="Home", icon=":material/home:")]