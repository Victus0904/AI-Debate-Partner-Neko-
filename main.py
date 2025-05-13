
from google import genai
import os
from dotenv import load_dotenv
import streamlit as st
from google.genai import types
import pyttsx3

load_dotenv()
engine = pyttsx3.init()

st.title("AI Debate Partner")
with st.container():
    message = st.chat_input("Hi")

# Load the model
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

response = client.models.generate_content(
    model="gemini-2.0-flash",
    config=types.GenerateContentConfig(
        system_instruction="You are a AI Debate Partner. Your name is Neko. Keep the replies short."),
    contents= f"You are a fierce debating partner + {message}",
)

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)   

st.write(response.text)
st.audio(engine.say(response.text))
engine.runAndWait() 


