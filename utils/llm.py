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
def summarize_notes(notes,level):
    prompt = f"""
You are Cognexa, an AI-powered academic learning assistant.

Your task is to summarize the students notes into high-quality academic study material.

Summary Level: {level}

Instructions based on the selected level:

- Beginner:
  • Use very simple English.
  • Explain concepts in an easy-to-understand way.
  • Avoid technical jargon where possible.
  • Suitable for first-time learners.

- Standard:
  • Use clear academic English.
  • Balance brevity and explanation.
  • Include essential concepts, definitions, and key points.
  • Suitable for university students and exam revision.

- Expert:
  • Use formal academic language.
  • Preserve technical terminology.
  • Include detailed explanations, relationships, formulas, and important insights.
  • Suitable for advanced learners and in-depth study.

General Guidelines:
• Maintain factual accuracy.
• Preserve the original meaning.
• Structure the response using:
  - Title
  - Overview
  - Key Concepts
  - Important Points
  - Definitions (if applicable)
  - Formulas (if applicable)
  - Examples (only if necessary)
  - Quick Revision Notes
• Remove redundant information.
• Do not add information not present in the notes.
• Format the response using Markdown.

Student Notes:
{notes}
"""
    response = client.models.generate_content(model="gemini-flash-latest",contents=f"Summarize these notes:\n\n{notes}")

    return response.text             


