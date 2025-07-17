import pandas as pd
from sentence_transformers import SentenceTransformer
import numpy as np
import pickle

# Load your dataset
df = pd.read_csv("movies_dataset.csv")

# Drop missing summaries
df = df.dropna(subset=["summary"])

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Generate embeddings from summaries
df["embedding"] = df["summary"].apply(lambda x: model.encode(x, convert_to_numpy=True))

# Save for Streamlit app
with open("movies_with_embeddings.pkl", "wb") as f:
    pickle.dump(df, f)
