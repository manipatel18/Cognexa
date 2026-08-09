import os
import json
import streamlit as st
from google import genai
from dotenv import load_dotenv
from utils.gemini_client import getclient


load_dotenv()

client = getclient()

def generateQuiz(notes,level):
    prompt = f"""

            You are an expert educator. Create a comprehensive practice quiz based on the following text. Include multiple-choice questions with correct answers and brief explanations.
            you are an AI quiz generator.

            Generate 5 multiple - choice questions from the notes below.

            Difficulty / Level:
            {level}

            Requirements:
            - Questions must be based only on the provided notes.
            - Each question must have exactly 4 options.
            - Include the correct answer.
            - Return ONLY valid JSON.
            - Do not include markdown.
            - Do not include ```json.

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