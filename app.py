import pickleimport pickle
import requests
import streamlit as st

# 🔑 Your TMDb API key here
API_KEY = 'your_tmdb_api_key_here'

# 🔍 Function to fetch movie poster using TMDb API
def fetch_poster(movie_id):
    url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={0c6b7c1452ff64a1a71e76c2903ac85f}&language=en-US'
    response = requests.get(url)
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

# 🎬 Recommendation Function
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movies = []
    recommended_posters = []

    for i in distances[1:6]:  # Get top 5 recommendations
        movie_id = movies.iloc[i[0]].id  # 'id' column must match TMDb movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_posters.append(fetch_poster(movie_id))
    
    return recommended_movies, recommended_posters

# 🧠 Load data
movies = pickle.load(open('models/movie_db.df', 'rb'))          # DataFrame with 'title' and 'id' columns
similarity = pickle.load(open('models/cos_mat.mt', 'rb'))       # Cosine similarity matrix

# 🌐 Streamlit UI
st.title("🎬 Movie Recommendation System")

selected_movie = st.selectbox("Search or select a movie:", movies['title'].values)

if st.button("Recommend"):
    names, posters = recommend(selected_movie)
    cols = st.columns(5)

    for i in range(5):
        with cols[i]:
            st.text(names[i])
            st.image(posters[i])
