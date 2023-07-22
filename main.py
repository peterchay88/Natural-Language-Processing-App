import streamlit as st
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import os
import re
import plotly.express as px

# Download the vader_lexicon resource if not already present & assign the analyzer object
nltk.download('vader_lexicon')
analyzer = SentimentIntensityAnalyzer()


# Reading all the text files at once
def read_text_file(file_path):
    with open(file_path, 'r') as f:
        slash_index = file_path.find("/")
        txt_name = file_path[slash_index +1:]
        read_text = f"{txt_name}\n{f.read()}\n"
    return read_text


diary_text = ""
for file in os.listdir("diary/"):
    if file.endswith(".txt"):
        file_path = f"diary/{file}"
        diary_text += read_text_file(file_path)

# Using Regular Expression to list dates from the title of the text files
pattern = re.compile("2023-10-[0-9]+")
dates = re.findall(pattern, diary_text)

# creating a list of scores from the text files
list_of_scores = []
for file in os.listdir("diary/"):
    if file.endswith(".txt"):
        file_path = f"diary/{file}"
        diary_text = read_text_file(file_path)
        list_of_scores.append(analyzer.polarity_scores(diary_text))

# Merge the list of scores and the list of dates into a list of tuples
merged_list = [(dates[i], list_of_scores[i]) for i in range(0, len(dates))]

# Create a list of the positive scores
positive_list = []
for score in list_of_scores:
    positive_list.append(score["pos"])

# Start streamlit elements
st.title("Diary Tone")
figure = px.line(x=dates, y=positive_list)
st.plotly_chart(figure)
st.text(positive_list)
st.text(dates)
