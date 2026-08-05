import streamlit as st
from utils.quiz import generateQuiz


st.set_page_config(
    page_title="Quiz",
    page_icon="🤔"
)

st.title("Quiz Generator")
st.write("Quiz generate by Ai ")

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
            quiz = generateQuiz(notes)

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







