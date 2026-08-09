import streamlit as st
from utils.quiz import generateQuiz



st.markdown("""
 <style>
[data-testid="stAppViewContainer"] {
background-color:#FFF5EE;
}

h1, h2, h3, p {
    color: black !important;
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
        border-radius:15px;
        padding:1px;

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
div[data-testid="stFormSubmitButton"] *{
    color: white !important;
}
div[data-testid="stFormSubmitButton"] :hover{
    color: black !important;
}


</style>
""", unsafe_allow_html=True
)


st.set_page_config(
    page_title="Quiz",
    page_icon="🤔",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("🧠 Quiz Generator")
st.write("*Quiz generate by Ai* ")


level = st.sidebar.selectbox(
    "Output Tone / Level",["Simple / Beginner-Friendly", "Standard Academic", "Advanced / Expert"],
index = 1
)

notes = st.text_area(
    " ",
    height=250,
    placeholder="paste here your notes..."
)

if st.button("Generate Quiz",use_container_width= True):

    if not notes.strip():
        st.warning("Please paste notes here before clicking on Generate Quiz button")

    else:
        with st.spinner("Generating Quiz..."):
            quiz = generateQuiz(notes, level)

            st.session_state.quiz = quiz                                        

            

if "quiz" in st.session_state:

    quiz = st.session_state.quiz


    with st.form("quiz_form"):
        answers = []

        for i,q in enumerate(quiz):

            st.subheader(f"Q{i+1}. {q['question']}")

            choice = st.radio(
                "Select your answer:",
                q["options"],
                index = None,
                key=f"q{i}"
            )

            answers.append(choice)
        submit = st.form_submit_button("Submit Quiz")



    # calculate score 
    if submit:

        score = 0

        for user_answer, q in zip(answers, quiz):
            if user_answer == q["answer"]:
                score += 1 
        st.success(f"your score: {score}/{len(quiz)}")
        st.write("### Correct Answers")

        for i, q in enumerate(quiz):
            st.write(f"**Q{i+1}:** {q['answer']}")







