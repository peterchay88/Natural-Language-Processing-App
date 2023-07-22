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
list_of_dates = re.findall(pattern, diary_text)

# creating a list of scores from the text files
list_of_scores = []
for file in os.listdir("diary/"):
    if file.endswith(".txt"):
        file_path = f"diary/{file}"
        diary_text = read_text_file(file_path)
        list_of_scores.append(analyzer.polarity_scores(diary_text))

# Merge the list of scores and the list of dates into a list of tuples
merged_list = [(list_of_dates[i], list_of_scores[i]) for i in range(0, len(list_of_dates))]
merged_list = sorted(merged_list)

positive_list = []
for pair in merged_list:
    positive_list.append(pair[1]["pos"])

negative_list = []
for pair in merged_list:
    negative_list.append(pair[1]["neg"])

dates = []
for pair in merged_list:
    dates.append(pair[0])

# Start streamlit elements
st.title("Diary Tone")

positive_figure = px.line(x=dates, y=positive_list, labels={"x": "Date", "y": "Score"}, title="Positive Graph")
positive_graph = st.plotly_chart(positive_figure)

negative_figure = px.line(x=dates, y=negative_list, labels={"x": "Date", "y": "Score"}, title="Negative Graph")
negative_graph = st.plotly_chart(negative_figure)



