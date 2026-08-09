import os
import streamlit as st
from google import genai
from dotenv import load_dotenv
from utils.gemini_client import getclient


load_dotenv()


client = getclient()

def answer_improvement(notes,level):
    prompt = f"""
    You are Cognexa, an AI-powered academic learning assistant.

    answer improvement: {level}

   Requirements:
    Improve grammar.
    Improve clarity.
    Improve structure.
    Keep the original meaning.
    Do not add unrelated information.
    Make the answer suitable for academic use.

    Student notes:
    {notes}
    
    """
    response = client.models.generate_content(model="gemini-3.1-flash-lite",contents= prompt)
    return response.text

