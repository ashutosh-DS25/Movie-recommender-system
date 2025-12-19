# Movie Recommender System

This project is a content-based movie recommendation system built using movie metadata.
It recommends similar movies based on textual features such as genres, keywords, cast,
director, and movie overview.

The application is deployed using Streamlit and provides an interactive user interface
where users can select a movie and receive recommendations along with movie posters.

---

## Project Overview

The goal of this project is to demonstrate how content-based filtering can be used
to build a recommendation system without relying on user ratings or collaborative data.

Movie similarity is calculated using textual features extracted from movie metadata
and transformed into numerical vectors using Natural Language Processing techniques.

---

## Dataset

- TMDB 5000 Movies Dataset
- TMDB 5000 Credits Dataset

Key features used:
- Movie overview
- Genres
- Keywords
- Top 3 cast members
- Director

---

## Workflow

1. Data loading and merging of movie and credit datasets
2. Data cleaning and handling missing values
3. Feature engineering from text-based columns
4. Text preprocessing:
   - Tokenization
   - Lowercasing
   - Stemming
5. Vectorization using CountVectorizer
6. Similarity computation using cosine similarity
7. Recommendation logic based on similarity scores
8. Web app development using Streamlit
9. Deployment configuration for cloud hosting

---

## Recommendation Logic

For a selected movie:
- The similarity score is calculated against all other movies
- The top 5 most similar movies are returned
- Movie posters are fetched dynamically using the TMDB API

---

## Tech Stack

- Python
