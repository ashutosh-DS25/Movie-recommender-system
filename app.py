import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8a7eeb53af168895283c917b6a9fc720&language=en-US'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_lists = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1]) [1:6]

    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_lists:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_posters

movies_list = pickle.load(open('movies.pkl','rb'))
movies_list = movies_list['title'].values
movies_data = pickle.load(open('movies.pkl','rb'))
movies = pd.DataFrame(movies_data)
similarity = pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    'Select a movie',
    movies_list)
if st.button('Recommend'):
    names, poster = recommend(selected_movie_name)

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.header(names[0])
        st.image(poster[0])
    with col2:
        st.header(names[1])
        st.image(poster[1])
    with col3:
        st.header(names[2])
        st.image(poster[2])
    with col4:
        st.header(names[3])
        st.image(poster[3])
    with col5:
        st.header(names[4])
        st.image(poster[4])
