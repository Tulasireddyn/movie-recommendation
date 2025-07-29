# Movie Recommendation System

This project is a movie recommendation system that uses vector embeddings to suggest movies based on their plot summaries. It leverages natural language processing (NLP) techniques to convert movie summaries into numerical vectors, enabling similarity-based recommendations.

## Features

- Loads a movie dataset with plot summaries.
- Uses the `sentence-transformers` library to generate vector embeddings for each summary.
- Stores embeddings for efficient similarity search.
- Can be integrated with a Streamlit app for interactive recommendations.

## How It Works

1. **Preprocessing:**  
   The `preprocess.py` script reads the movie dataset, removes entries with missing summaries, and generates vector embeddings for each summary using a pre-trained transformer model.

2. **Embeddings:**  
   Each movie summary is converted into a high-dimensional vector. These vectors capture semantic meaning, allowing the system to find similar movies based on summary content.

3. **Recommendation:**  
   When a user provides a movie or a summary, the system computes its embedding and finds movies with the most similar embeddings.

## Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Tulasireddyn/movie-recommendation.git
   cd movie-recommendation
   ```

2. **Install dependencies:**
   ```bash
   pip install pandas sentence-transformers numpy streamlit
   ```

3. **Prepare the dataset:**
   - Place your `movies_dataset.csv` file in the project directory.

4. **Run preprocessing:**
   ```bash
   python preprocess.py
   ```

5. **Start the Streamlit app (if available):**
   ```bash
   streamlit run app.py
   ```

## Files

- `preprocess.py`: Generates and saves vector embeddings for movie summaries.
- `movies_dataset.csv`: Your source dataset (must contain a `summary` column).
- `movies_with_embeddings.pkl`: Pickle file with processed data and embeddings.
- `app.py`: (Optional) Streamlit app for interactive recommendations.

## Requirements

- Python 3.7+
- pandas
- sentence-transformers
- numpy
- streamlit (optional)

## Usage

After preprocessing, use the embeddings to recommend movies by comparing vector similarities. Integrate with a web app or use in scripts for personalized recommendations.

## License

This project is licensed under the MIT License.





