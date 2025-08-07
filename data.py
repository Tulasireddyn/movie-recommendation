import pandas as pd
import requests
import time

API_KEY = "api key here"
BASE_URL = "https://api.themoviedb.org/3"

def get_additional_movie_info(title):
    search_url = f"{BASE_URL}/search/movie"
    params = {
        "api_key": API_KEY,
        "query": title
    }
    response = requests.get(search_url, params=params)
    data = response.json()
    if not data['results']:
        return None, None
    movie = data['results'][0]
    return movie.get('release_date', ''), movie.get('original_language', '')

# Load existing dataset
df = pd.read_csv("movies_dataset.csv")
# Add new columns
df['release_date'] = ""
df['release_year'] = ""
df['original_language'] = ""

# filepath: c:\Users\tulas\OneDrive\Desktop\project\data.py
for index, row in df.iterrows():
    try:
        release_date, lang = get_additional_movie_info(row['title'])
        df.at[index, 'release_date'] = release_date
        df.at[index, 'release_year'] = release_date[:4] if release_date else ""
        df.at[index, 'original_language'] = lang
        print(f"Processed: {row['title']}")
        df.to_csv("movies_dataset.csv", index=False)  # Save after each row
        time.sleep(0.2)  # Avoid rate limit
    except Exception as e:
        print(f"Error processing {row['title']}: {e}")
        continue

print("Updated file saved as movie_dataset.csv")
df.to_csv("movies_dataset.csv", index=False)
print("Updated file saved as movie_dataset.csv")
