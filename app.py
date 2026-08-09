import streamlit as st

st.set_page_config(
    page_title="Cognexa",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)


home = st.Page(
    "Home.py",
    title="Home",
    icon=":material/home:",
    default=True
)

answer = st.Page(
    "pages/Answer_Improvement.py",
    title="Answer Improvement",
    icon=":material/edit:"
)

concept = st.Page(
    "pages/Concept_Explainer.py",
    title="Concept Explainer",
    icon=":material/lightbulb:"
)

summary = st.Page(
    "pages/Notes_Summarizer.py",
    title="Notes Summarizer",
    icon=":material/summarize:"
)

quiz = st.Page(
    "pages/Quiz_Generator.py",
    title="Quiz Generator",
    icon=":material/quiz:"
)


pg = st.navigation([
    home,
    answer,
    concept,
    summary,
    quiz
])

pg.run()