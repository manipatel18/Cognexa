import streamlit as st
from utils.quiz import generateQuiz
from utils.ui import apply_common_css


st.set_page_config(
    page_title="Quiz",
    page_icon="🤔",
    layout="wide",
    initial_sidebar_state="expanded"
)

apply_common_css()

st.markdown("""
 <style>

div[data-testid="stFormSubmitButton"] *{
    color: white !important;
}
div[data-testid="stFormSubmitButton"] :hover{
    color: black !important;
}


</style>
""", unsafe_allow_html=True
)


st.title("🧠 Quiz Generator")
st.write("*Quiz generate by Ai* ")


level = st.sidebar.selectbox(
    "Output Tone / Level",
    ["Simple / Beginner-Friendly", "Standard Academic", "Advanced / Expert"],
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
            try:
                 # Store result
                st.session_state.quiz = generateQuiz(notes, level)
                 # Reset submission state
                st.session_state.quiz_submitted = False
            except Exception as e:
                st.error(f"Unable to generate quiz: {e}")
                                        

            

if "quiz" in st.session_state:
    quiz = st.session_state.quiz


    with st.form("quiz_form"):
        answers = []

        for i,q in enumerate(quiz):

            st.subheader(f"Q{i + 1}. {q['question']}")

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
        st.session_state["quiz_score"] = score
        st.session_state["quiz_submitted"] = True   

# Show result
if st.session_state.get("quiz_submitted", False):

    quiz = st.session_state["quiz"]
    score = st.session_state["quiz_score"]     

    st.success(f"your score: {score}/{len(quiz)}")

    st.write("### Correct Answers")

    for i, q in enumerate(quiz):
        st.write(f"**Q{i+1}:** {q['answer']}")







