import requests
import streamlit as st
import pickle
import pandas as pd

# ------------------- Poster from OMDb -------------------
def fetch_poster_omdb(movie_title):
    api_key = "980f4407"
    url = f"http://www.omdbapi.com/?t={movie_title}&apikey={api_key}"
    try:
        response = requests.get(url, timeout=5)
        data = response.json()
        if data['Response'] == 'True' and data['Poster'] != "N/A":
            return data['Poster']
        else:
            return "https://via.placeholder.com/500x750.png?text=Not+Found"
    except Exception as e:
        st.error(f"OMDb API error: {e}")
        return "https://via.placeholder.com/500x750.png?text=Error"

# ------------------- Recommendation Function -------------------
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []

    for i in movies_list:
        title = movies.iloc[i[0]].title
        recommended_movies.append(title)
        recommended_movies_posters.append(fetch_poster_omdb(title))

    return recommended_movies, recommended_movies_posters

# ------------------- Load Data -------------------
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

# ------------------- UI Starts Here -------------------
st.set_page_config(layout="wide")
st.markdown("<h1 style='text-align: center; color: #FF4B4B;'>🎬 Movie Recommendation System 🍿</h1>", unsafe_allow_html=True)
st.markdown("---")

selected_movie_name = st.selectbox('Select your favourite movie:', movies['title'].values)

if st.button('🎯 Recommend'):
    names, posters = recommend(selected_movie_name)

    st.markdown("### 🔥 Top 5 Recommendations:")

    cols = st.columns(5)
    for i in range(5):
        with cols[i]:
            st.image(posters[i], use_container_width=True, caption=f"🎞️ {names[i]}")
            st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("""
    <div style="text-align: center;">
        <a href="https://forms.gle/BzMJgVgXNhoE5qJc9" target="_blank" style="text-decoration: none;">
            <button style="background-color: #4CAF50; color: white; padding: 10px 20px; font-size: 16px; border: none; border-radius: 5px;">
                ✍️ Submit Feedback
            </button>
        </a>
    </div>
    """, unsafe_allow_html=True)
