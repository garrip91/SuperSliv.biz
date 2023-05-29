import json


class MovieDAO:

    def __init__(self):
        pass

    def load_data(self):
        with open(file="data.json", mode="r", encoding="utf-8") as file:
            data = json.load(file)
        return data
    
    def get_by_id(self, movie_id):
        """Получает 1 запись (фильм) по id"""
        movies = self.load_data()
        for movie in movies:
            if movie.get("pk") == movie_id:
                return movie
            else:
                return None
    
    def get_by_period(self, period_from, period_to):
        """Получает записи (фильмы) по периодам включительно"""
        movies = self.load_data()
        movies_found = []
        for movie in movies:
            if period_from <= movie.get("year") <= period_to:
                movies_found.append(movie)
        return movies_found
