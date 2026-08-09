import os
import streamlit as st
from google import genai
from dotenv import load_dotenv
from utils.gemini_client import getclient


load_dotenv()


client = getclient()

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

