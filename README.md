# Movie Analysis & Recommendation

This repository contains two Jupyter notebooks analyzing the TMDB 5000 dataset, plus a Streamlit app for interactive movie recommendations:

1. **Movie_Data_Analysis.ipynb**: Predicts movie success (vote average ≥ 7) using Logistic Regression and Naive Bayes.
2. **Movie_Recommendation_System.ipynb**: Recommends similar movies using cosine similarity.
3. **Streamlit App**: A user-friendly UI hosted on Streamlit to explore movie recommendations.

## Projects

### Movie Success Prediction
- **Goal**: Classify movies as "good" (vote average ≥ 7) or not.
- **Methods**: Logistic Regression (84.12% accuracy), Naive Bayes (78.58% accuracy).
- **Features**: Budget, popularity, revenue, runtime, genres, cast, crew.

### Movie Recommendation System
- **Goal**: Suggest 5 similar movies based on a given title.
- **Methods**: Bag-of-words with CountVectorizer, cosine similarity.
- **Features**: Overview, genres, keywords, top 3 cast, director.

### Streamlit App
- **Description**: Interactive web app for movie recommendations with a sleek UI.
- **Access**: Hosted at [https://movierecommendationsystem-28012005.streamlit.app/].
- **Usage**: Select a movie to get instant recommendations.

## Dataset
- **TMDB 5000**: `tmdb_5000_movies.csv` and `tmdb_5000_credits.csv`.
- Download from [Kaggle](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata) and place in the project directory.

## Pickle Files Google Drive Link:
- [Drive](https://drive.google.com/drive/folders/1-28gSzrbDnaiIQl2fodtGsToXCs4SdR2?usp=sharing)

## Requirements

- Requires: `numpy`, `pandas`, `scikit-learn`, `statsmodels`, `nltk`, `pickle`, `streamlit`, `gdown`.


## Usage
- **Project 1**: Run `Movie_Data_Analysis.ipynb` to train and evaluate models.
- **Project 2**: Run `Movie_Recommendation_System.ipynb`. Use `recommend('Batman')` for suggestions.
- **Streamlit**: Visit [https://movierecommendationsystem-28012005.streamlit.app/] or run `streamlit run app.py` locally to use the UI.

## Results
- **Project 1**: Logistic Regression outperforms Naive Bayes (MSE: 0.1725 vs. 0.2185).
- **Project 2**: Recommends relevant movies (e.g., "Batman" suggests "Batman Begins").
- **Streamlit**: Provides an intuitive interface for movie recommendations.

