import pandas as pd
import numpy as np
import streamlit as st

df = pd.read_csv("characters.csv")
similarity = np.load("similarity.npy")

image_paths = {
    "TONY": "C:\\Users\\banda\\PycharmProjects\\PythonProject\\Machine Learning\\Project 1\\images\\Iron man.jpg",
    "STEVE": "C:\\Users\\banda\\PycharmProjects\\PythonProject\\Machine Learning\\Project 1\\images\\steve rogers.jpg",
    "THOR": "C:\\Users\\banda\\PycharmProjects\\PythonProject\\Machine Learning\\Project 1\\images\\Thor.jpg",
    "LOKI": "C:\\Users\\banda\\PycharmProjects\\PythonProject\\Machine Learning\\Project 1\\images\\LOKI.jpg",
    "BANNER": "C:\\Users\\banda\\PycharmProjects\\PythonProject\\Machine Learning\\Project 1\\images\\Hulk.jpg",
    "NATASHA": "C:\\Users\\banda\\PycharmProjects\\PythonProject\\Machine Learning\\Project 1\\images\\natasha.jpg",
    "FURY": "C:\\Users\\banda\\PycharmProjects\\PythonProject\\Machine Learning\\Project 1\\images\\Nick FURY.jpg",
    "BARTON": "C:\\Users\\banda\\PycharmProjects\\PythonProject\\Machine Learning\\Project 1\\images\\Hawkeye.jpg",
    "SELVIG":"C:\\Users\\banda\\PycharmProjects\\PythonProject\\Machine Learning\\Project 1\\images\\selvig.jpg",
    "MARIA HILL" :"C:\\Users\\banda\\PycharmProjects\\PythonProject\\Machine Learning\\Project 1\\images\\Maria Hill.jpg",
    "AGENT COULSON":"C:\\Users\\banda\\PycharmProjects\\PythonProject\\Machine Learning\\Project 1\\images\\Agent.jpg",
    "JARVIS":"C:\\Users\\banda\\PycharmProjects\\PythonProject\\Machine Learning\\Project 1\\images\\Jarvis.jpg"
}

st.markdown("<br>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 3, 1])

with col2:
    st.image("images/Marvel.jpg", width=250)

st.title("Marvel Character Finder")

st.write("Select a Marvel character to find similar characters.")

characters = df["character"].tolist()

selected_character = st.selectbox(
    "Select a character:",
    characters
)

index = df.index[df["character"] == selected_character][0]

scores = similarity[index]

similar_indices = scores.argsort()[::-1]

top_index = similar_indices[1]

st.write("You selected:", selected_character)

st.subheader("Most Similar Character")

matched_character = df.iloc[top_index]["character"]
score = scores[top_index] * 100

st.write(f"### Similarity: {score:.2f}%")

col1, col2 = st.columns(2)

with col1:
    st.subheader(selected_character)
    st.image(image_paths[selected_character], width=250)

with col2:
    st.subheader(matched_character)
    st.image(image_paths[matched_character], width=250)

