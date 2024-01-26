movie_ratings = {
    'user1': {'movie1': 5, 'movie2': 4, 'movie3': 2, 'movie4': 3},
    'user2': {'movie1': 3, 'movie2': 5, 'movie3': 4, 'movie4': 2},
    'user3': {'movie1': 4, 'movie2': 3, 'movie3': 5, 'movie4': 4},
    'user4': {'movie1': 2, 'movie2': 4, 'movie3': 3, 'movie4': 5},
    'user5': {'movie1': 5, 'movie2': 2, 'movie3': 4, 'movie4': 3}
}

def calculate_similarity(user1, user2):
    """Calculate the similarity between two users based on movie ratings."""

    common_movies = [movie for movie in user1 if movie in user2]
    

    if not common_movies:
        return 0 
    
    sum1 = sum(user1[movie] for movie in common_movies)
    sum2 = sum(user2[movie] for movie in common_movies)
    sum1_sq = sum(pow(user1[movie], 2) for movie in common_movies)
    sum2_sq = sum(pow(user2[movie], 2) for movie in common_movies)
    product_sum = sum(user1[movie] * user2[movie] for movie in common_movies)
    
    num = product_sum - (sum1 * sum2 / len(common_movies))
    den = ((sum1_sq - pow(sum1, 2) / len(common_movies)) * (sum2_sq - pow(sum2, 2) / len(common_movies))) ** 0.5
    
    if den == 0:
        return 0  
    return num / den

def recommend_movies(user, all_ratings, num_recommendations=5):

    scores = {}
    total_similarities = {}
    
    for other_user in all_ratings:
        if other_user == user:
            continue
        
        similarity = calculate_similarity(all_ratings[user], all_ratings[other_user])
        
        if similarity <= 0:
            continue
        
        for movie in all_ratings[other_user]:

            if movie not in all_ratings[user] or all_ratings[user][movie] == 0:
              
                scores.setdefault(movie, 0)
                scores[movie] += all_ratings[other_user][movie] * similarity
                total_similarities.setdefault(movie, 0)
                total_similarities[movie] += similarity

   
    ranked_recommendations = [(score / total_similarities[movie], movie) for movie, score in scores.items()]
    ranked_recommendations.sort(reverse=True)
    
   
    return ranked_recommendations[:num_recommendations]


user = 'user1'

recommendations = recommend_movies(user, movie_ratings)


print("Recommendations for", user + ":")
if recommendations:
    for score, movie in recommendations:
        print("Movie:", movie, "- Score:", round(score, 2))
else:
    print("No recommendations available for", user)
