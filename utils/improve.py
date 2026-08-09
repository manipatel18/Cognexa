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
def answer_improvement(notes,level):
    prompt = f"""
    You are Cognexa, an AI-powered academic learning assistant.

    answer improvement: {level}


    Student notes:
    {notes}
    
    """
    response = client.models.generate_content(model="gemini-3.1-flash-lite",contents= prompt)
    return response.text

