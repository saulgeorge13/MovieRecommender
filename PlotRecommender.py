# Setup
import pandas as pd
metadata = pd.read_csv('Large Dataset.csv')
#print(metadata.head(3))

# Tfidf setup
from sklearn.feature_extraction.text import TfidfVectorizer
# Remove all 'english' words such as 'the', 'as', etc
tfidf = TfidfVectorizer(stop_words='english')

tfidf_matrix = tfidf.fit_transform(metadata['Plot'])
#print(tfidf_matrix.shape) # (num movies: num words)
#print(tfidf.get_feature_names()[2000:2010])

# We use the consine similarity score to compute similarity between movies, as tfidf gives us a vector score allowing easy comparison
# Returns a (num_moviesXnum_movies) matrix where each movie is a (1Xnum_movies) column vectore,
# where each column is a similarity score with a movie
from sklearn.metrics.pairwise import cosine_similarity

# Compute cosine similarity matrix
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
#print(cosine_sim.shape)

# Series of indices and movie titles
idx = pd.Series(metadata.index, index=metadata['Title']).drop_duplicates()
#print(indices[:10])

def get_recommendations(title, cosine_sim=cosine_sim):
    id = idx[title]
    sim_scores = list(enumerate(cosine_sim[id]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]
    movie_indices = []
    movie_indices = [i[0] for i in sim_scores]
    return metadata['Title'].iloc[movie_indices]

#print(get_recommendations('The Dark Knight'))
    