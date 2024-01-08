class MovieRecommendationSystem:
    def __init__(self):
        self.movies_data = {
            'Movie1': {'Action': 5, 'Comedy': 3, 'Drama': 2, 'Romance': 1},
            'Movie2': {'Action': 4, 'Comedy': 2, 'Drama': 3, 'Romance': 1},
            'Movie3': {'Action': 1, 'Comedy': 5, 'Drama': 2, 'Romance': 4},
            'Movie4': {'Action': 3, 'Comedy': 2, 'Drama': 4, 'Romance': 5},
            'Movie5': {'Action': 2, 'Comedy': 4, 'Drama': 3, 'Romance': 5}
        }

    def recommend_movies(self, user_preferences):
        scores = {}
        for movie, genres in self.movies_data.items():
            similarity_score = sum(user_preferences[genre] * genres[genre] for genre in user_preferences)
            scores[movie] = similarity_score

        recommended_movies = sorted(scores, key=scores.get, reverse=True)
        return recommended_movies

# Example usage
user_preferences = {'Action': 4, 'Comedy': 3, 'Drama': 2, 'Romance': 5}
recommendation_system = MovieRecommendationSystem()
recommendations = recommendation_system.recommend_movies(user_preferences)

print("Recommended Movies:")
for movie in recommendations:
    print(movie)
