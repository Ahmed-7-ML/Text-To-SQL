from dotenv import load_dotenv
import os
from google import genai
import streamlit as st

# Load all Environemnt Variables(.env File)
load_dotenv()

# Setup Gemini API Key
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("❌ GEMINI_API_KEY is missing! Please check your .env file or environment variables.")

client = genai.Client()
DB_PATH = "Faculty.db"

def initialize_session_state():
    """Setting up session variables if they don't exist"""
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
    
    if "username" not in st.session_state:
        st.session_state.username = ""
    
    if "role" not in st.session_state:
        st.session_state.role = ""

