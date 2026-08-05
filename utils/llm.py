import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def summarize_notes(notes):
    prompt = f"""Summarize the following notes:
    \n{notes}\n
    \nSummary:"""
    response = client.models.generate_content(model="gemini-flash-latest",contents=f"Summarize these notes:\n\n{notes}")

    return response.text             


