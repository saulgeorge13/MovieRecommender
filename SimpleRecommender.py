#Setup
import pandas as pd
metadata = pd.read_csv('Full Dataset.csv')
print(metadata.head(3))

# The main issue with a simple recommender is the weightage of individual reviews. 
# For example; is a movie with 1 review that is 9/10 better than a movie with 100 reviews scoring it 8/10?
# As the number of reviews increase they end up being normally distributed but for now we need a way to fairly weigh the number of reviews

# In this simple recommeder we use IMDB's weighted rating formaula;
# weighted_rating = (vote_count/(vote_count + min_votes) * vote_avg) + (min_votes/(vote_count + min_votes) * avg)
# num_reviews = number of reviews (taken from dataset as vote_count)
# avg_review = average rating (taken from dataset as vote_average)
# min_votes = min reviews to be listed (we've gone with 90th percentile)
# avg = mean rating across entire dataset

min_votes = metadata['vote_count'].quantile(0.9)
#print(min_votes)
avg =  metadata['vote_average'].mean()
#print(avg)

# Filter out movies which don't have min reviews
filter_movies = metadata.copy().loc[metadata['vote_count'] >= min_votes]
#print(filter_movies.shape)
#print(metadata.shape())

# Computes weighted rating of a movie
def compute_rating(movie, min_votes=min_votes, avg=avg):
    num_reviews = movie['vote_count']
    avg_review = movie['vote_average']
    return((num_reviews/(num_reviews + min_votes) * avg_review) + (min_votes/(num_reviews + min_votes) * avg))

# Apply the function to the entire dataset
filter_movies['score'] = filter_movies.apply(compute_rating, axis=1)

# Sort by descending order and print top 20 movies
filter_movies = filter_movies.sort_values('score', ascending=False)
print(filter_movies[['title', 'score']].head(20))