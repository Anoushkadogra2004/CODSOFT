import pandas as pd 
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Movies data
movies = {
    'movie_id': [1, 2, 3, 4, 5],
    'title': ['The Matrix', 'Inception', 'Interstellar', 'The Dark Knight', 'The Lion King'],
    'genre': ['Action Sci-Fi', 'Action Sci-Fi', 'Sci-Fi Drama', 'Action Crime', 'Animation Drama']
}
movies_df = pd.DataFrame(movies)

# Content-based filtering
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(movies_df['genre'])
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

def recommend_content(movie_title, n=2):
    if movie_title not in movies_df['title'].values:
        return ["Movie not found!"]
    
    idx = movies_df[movies_df['title'] == movie_title].index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:n+1]
    movie_indices = [i[0] for i in sim_scores]
    return movies_df['title'].iloc[movie_indices].tolist()

# Ratings data
ratings = {
    'user_id': [1, 1, 1, 2, 2, 3, 3, 3, 4],
    'movie_id': [1, 2, 3, 2, 4, 3, 4, 5, 5],
    'rating': [5, 4, 4, 5, 4, 5, 3, 4, 5]
}
ratings_df = pd.DataFrame(ratings)

# Collaborative filtering (user-based)
user_item_matrix = ratings_df.pivot_table(
    index='user_id', columns='movie_id', values='rating'
).fillna(0)

user_similarity = cosine_similarity(user_item_matrix)
user_similarity_df = pd.DataFrame(
    user_similarity, index=user_item_matrix.index, columns=user_item_matrix.index
)

def recommend_collaborative(user_id, n=2):
    if user_id not in user_similarity_df.index:
        return ["User not found!"]
    
    similar_users = user_similarity_df[user_id].sort_values(ascending=False).index[1:]
    watched_movies = set(ratings_df[ratings_df['user_id'] == user_id]['movie_id'])
    
    recommendations = []
    for other_user in similar_users:
        other_movies = ratings_df[ratings_df['user_id'] == other_user] \
            .sort_values(by='rating', ascending=False)
        for movie in other_movies['movie_id']:
            if movie not in watched_movies and movie not in recommendations:
                recommendations.append(movie)
            if len(recommendations) >= n:
                break
        if len(recommendations) >= n:
            break
    
    return movies_df[movies_df['movie_id'].isin(recommendations)]['title'].tolist()

# Test
print("Content-Based Recommendation for 'Inception':", recommend_content("Inception"))
print("Collaborative Recommendation for User 1:", recommend_collaborative(1))
