import streamlit as st 
from utils.ui import apply_common_css

st.set_page_config(
    page_title="Cognexa",
    page_icon="1",
    layout="wide",
    initial_sidebar_state="expanded"

)

apply_common_css()

st.markdown("""
<style>

/* columns background */
div[data-testid="stAlert"] *{
    background-color: white;
    color: black !important;
    border-radius: 13px;   
}

/* arrow container*/
div[data-testid="stElementContainer"] p{
    background-color: white !important;
    color:grey !important;
    border: 1px solid #d9d9d9;
    border-radius: 12px;
    margin-top: 10px;
    padding:15px;
    
}
span[data-testid="stIconEmoji"] {
    margin-top: 100rem;
}
div[data-testid="stPageLink"] p{
    color:#18a4d6 !important;
    padding:3px;
    border: 1px solid #88c8df !important;
    text-align:bold;
    font-style: italic

}
div[data-testid="stPageLink"] :hover{
    color: black !important;
    
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
            label=" OPEN "
        )

    

with st.expander("💡Concept Explainer",expanded=False):
    with st.container(border=True):
        st.write("""
        The *Concept Explainer* feature uses AI to simplify complex topics and explain them in a clear, structured, and easy-to-understand manner. It adapts explanations to the user's level of understanding and can provide examples, key points, and step-by-step explanations to support effective learning.
        """)
        st.page_link(
            "pages/Concept_Explainer.py",
            label=" OPEN "
        )



with st.expander("📝Notes Summarizer",expanded=False):
    with st.container(border=True):
        st.write("""
        The *Notes Summarizer* feature uses AI to analyze lengthy study materials and generate concise, well-structured summaries. It extracts important concepts, key points, definitions, and essential information, helping users save time and revise their study material more efficiently.
        """)
        st.page_link(
            "pages/Notes_SummarizerS.py",
            label=" OPEN "
        )            
      

with st.expander("🧠 Quiz Generator",expanded=False):
    with st.container(border=True):
        st.write("""
            The *Quiz Generator* feature uses AI to automatically create quizzes from provided study material. It generates relevant questions based on the content and can include multiple-choice questions, answers, and explanations to help users test their knowledge and identify areas for improvement.
            """)
        st.page_link(
            "pages/Quiz_Generator.py",
            label=" OPEN "
        )