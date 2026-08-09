import os
import streamlit as st
from google import genai
from dotenv import load_dotenv

load_dotenv()


@st.cache_resource
def get_client():
    return genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

client = get_client()

@st.cache_data(show_spinner=False)
def generateConcept(notes,level):
    prompt = f"""
    You are Cognexa, an AI-powered academic learning assistant.

    Explain the following study material at the selected level:

    Level: {level}

    Notes:
    {notes}

    Requirements:
    - Explain the concept clearly.
    - Use simple language where appropriate.
    - Give important key points.
    - Give examples when useful.
    - Use headings and bullet points.
    - Do not change the meaning of the original content.
    """
    response = client.models.generate_content(model="gemini-flash-latest",contents= prompt)
    return response.text

