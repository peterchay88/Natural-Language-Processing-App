import streamlit as st
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import os

# Download the vader_lexicon resource if not already present & assign the analyzer object
nltk.download('vader_lexicon')
analyzer = SentimentIntensityAnalyzer()


# Reading all the text files at once
def read_text_file(file_path):
    with open(file_path, 'r') as f:
        slash_index = file_path.find("/")
        txt_name = file_path[slash_index +1:]
        read_text = f"{txt_name}\n{f.read()}"
    return read_text


diary_text = ""
for file in os.listdir("diary/"):
    try:
        if file.endswith(".txt"):
            file_path = f"diary/{file}"
            diary_text += read_text_file(file_path)
    except FileNotFoundError:
        print("could not read")


st.title("Diary Tone")
st.text(diary_text)