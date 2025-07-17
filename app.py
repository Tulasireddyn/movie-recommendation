import streamlit as st
import pickle
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Load data
with open("movies_with_embeddings.pkl", "rb") as f:
    df = pickle.load(f)

model = SentenceTransformer("all-MiniLM-L6-v2")

st.title("🎥 Smart Movie Recommender")
st.markdown("Type your favorite genres, movies, mood, or plot. We'll recommend the best matches!")

query = st.text_input("What kind of movie do you want to watch?")

if query:
    # Encode the query
    query_vec = model.encode(query, convert_to_numpy=True)
    
    # Compute similarity
    df["similarity"] = df["embedding"].apply(lambda x: cosine_similarity([query_vec], [x])[0][0])
    top_movies = df.sort_values(by="similarity", ascending=False).head(20)

    # Show results
    for index, row in top_movies.iterrows():
        st.markdown(f"### 🎞️ {row['title']}")
        st.markdown(f"**Year**: {row['release_year']}")
        st.image(row['poster_url'], width=150)
        st.markdown(f"**Rating**: ⭐ {row['rating']} | **Language**: {row['original_language']}")
        st.markdown(f"**Genres**: {row['genres']}")
        st.markdown(f"**Cast**: {row['cast']}")
        st.markdown(f"**Summary**: {row['summary']}")
        st.markdown("--")
