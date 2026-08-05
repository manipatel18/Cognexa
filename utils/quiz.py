import os
from google import genai
from dotenv import load_dotenv
import json

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def generateQuiz(notes):
    prompt = f"""
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

    response =client.models.generate_content(model="gemini-3.5-flash-lite", contents= prompt)

    return json.loads(response.text)