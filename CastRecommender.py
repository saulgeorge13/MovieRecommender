# Setup
import pandas as pd
import numpy as np
metadata = pd.read_csv('Large Dataset.csv')
#print(metadata.head(3))

# Convert all keyword strings to lowecase and remove spaces
# This ensures the vectorizer recognises actors/directors with same first or last names are distinct
def clean_data(element):
    if isinstance(element, list):
        return [str.lower(i.replace(" ", "")) for i in element]
    else:
        if isinstance(element, str):
            return str.lower(element.replace(" ", ""))
        else:
            return ' '

# Apply data cleaning to our dataset
features = ['Director', 'Star1', 'Star2', 'Star3', 'Star4']
for feature in features:
    metadata[feature] = metadata[feature].apply(clean_data)
#print(metadata[['Director', 'Star1', 'Star2', 'Star3', 'Star4']].head(3))

def create_soup(x):
    return (x['Director']) + ' ' + (x['Star1']) + ' ' + (x['Star2']) + ' ' + (x['Star3']) + ' ' + (x['Star4'])

metadata['soup'] = metadata.apply(create_soup, axis=1)
#print(metadata[['soup']].head(3))

from sklearn.feature_extraction.text import CountVectorizer
count = CountVectorizer(stop_words='english')
count_matrix = count.fit_transform(metadata['soup'])
#print(count_matrix.shape)

from sklearn.metrics.pairwise import cosine_similarity
cosine_sim2 = cosine_similarity(count_matrix, count_matrix)

metadata = metadata.reset_index()
idx = pd.Series(metadata.index, index=metadata['Title'])

def get_recommendations(title, cosine_sim=cosine_sim2):
    id = idx[title]
    sim_scores = list(enumerate(cosine_sim[id]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]
    movie_indices = []
    movie_indices = [i[0] for i in sim_scores]
    return metadata['Title'].iloc[movie_indices]

print(get_recommendations('The Dark Knight'))
