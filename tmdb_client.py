from random import shuffle

import requests

Api_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI0ODg4ZWYxN2I2MWRjZTgzMWZiNGEwYjdiMjA4YTliNCIsInN1YiI6IjYzODcwMzJjMjI5YWUyMTViNDYwNTc1YSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.OYs7rxZFJzRMpix6mv1Bos89sX42SekoUY36kZAkJ_A"
headers = {
    "Authorization": f"Bearer {Api_token}",
    "Content-Type": "application/json; charset=utf-8"
}


def get_popular_movies():
    page = 'https://api.themoviedb.org/3/movie/popular'
    response = requests.get(page, headers=headers)
    return response.json()


def get_poster_url(poster_api_path, size="w342"):
    if poster_api_path is None:
        return "https://upload.wikimedia.org/wikipedia/commons/a/ac/No_image_available.svg"
    base_url = "https://image.tmdb.org/t/p/"
    return base_url + size + poster_api_path


def get_movies(how_many):
    data = get_popular_movies()
    shuffle(data["results"])
    return data["results"][:how_many]


def get_single_movie(movie_id):
    page = f'https://api.themoviedb.org/3/movie/{movie_id}'
    response = requests.get(page, headers=headers)
    return response.json()


def get_movie_credits(movie_id):
    page = f'https://api.themoviedb.org/3/movie/{movie_id}/credits'
    response = requests.get(page, headers=headers)
    return response.json()['cast']
