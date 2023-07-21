import streamlit as st
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Download the vader_lexicon resource if not already present & assign the analyzer object
nltk.download('vader_lexicon')
analyzer = SentimentIntensityAnalyzer()

st.title("Diary Tone")

