import requests
import streamlit as st
import pickle
import pandas as pd
import speech_recognition as sr

# Function to fetch movie poster using API
def fetch_poster(movie_id):
    response = requests.get(
        'https://api.themoviedb.org/3/movie/{}?api_key=01e5f1fa40a068be89fa790aba403e58'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

# Function to recommend movies
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        # fetch poster from API
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_posters

# Load movie data and similarity matrix
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Streamlit app layout
st.title('Movie Recommendation System')

# Initialize selected movie name
selected_movie_name = ""

# Voice input using microphone
if st.button('Voice'):
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        st.text("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        st.text("Processing...")
        speech_input = recognizer.recognize_google(audio)
        st.session_state['movie_title'] = speech_input
        # Check if the spoken movie title is in the movie titles
        if speech_input in movies['title'].values:
            selected_movie_name = speech_input

# Movie selection dropdown
if selected_movie_name:
    index = movies['title'].values.tolist().index(selected_movie_name)
else:
    index = None

selected_movie_name = st.selectbox('What is your favourite movie??', movies['title'].values, index=index)

# Recommendation button
if st.button('Recommend'):
    voice_movie = st.session_state.get('movie_title', "")
    if voice_movie != "":
        selected_movie_name = voice_movie
    names, posters = recommend(selected_movie_name)
    st.session_state['movie_title'] = ""
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(names[0])
        st.image(posters[0])

    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])

    with col4:
        st.text(names[3])
        st.image(posters[3])

    with col5:
        st.text(names[4])
        st.image(posters[4])

    st.write('Feedback Form : https://forms.gle/BzMJgVgXNhoE5qJc9')
