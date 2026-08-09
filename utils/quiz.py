import os
import streamlit as st
from google import genai
from dotenv import load_dotenv
import json

load_dotenv()


@st.cache_resource
def loading():
    return genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

client = loading()

@st.cache_data(show_spinner=False)
def generateQuiz(notes,level):
    prompt = f"""

            You are an expert educator. Create a comprehensive practice quiz based on the following text. Include multiple-choice questions with correct answers and brief explanations.
            you are an AI quiz generator.

            Generate 5 multiple - choice questions from the notes below.

            Return ONLY valid JSON.

            Example:

                [
                {{
                    "question":"What is Python?",
                    "options":[
                    "Programming Language",
                    "Database",
                    "Browser",
                    "Operating System"
                    ],
                    "answer":"Programming Language"
                }}
                ]


                Notes:
                {notes}

    """

    response =client.models.generate_content(model="gemini-3.1-flash-lite", contents= prompt)

    return json.loads(response.text)