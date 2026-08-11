import os
import streamlit as st
from google import genai
from dotenv import load_dotenv

load_dotenv()


@st.cache_resource
def getclient():
    return genai.Client(
        api_key=os.getenv("GEMINI_API_KEY")
    )