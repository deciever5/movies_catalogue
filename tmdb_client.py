import requests


def get_popular_movies():
    Api_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI0ODg4ZWYxN2I2MWRjZTgzMWZiNGEwYjdiMjA4YTliNCIsInN1YiI6IjYzODcwMzJjMjI5YWUyMTViNDYwNTc1YSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.OYs7rxZFJzRMpix6mv1Bos89sX42SekoUY36kZAkJ_A"
    headers = {
        "Authorization": f"Bearer {Api_token}",
        "Content-Type": "application/json; charset=utf-8"
    }
    page = 'https://api.themoviedb.org/3/movie/popular'
    response = requests.get(page, headers=headers)
    return response.json()


def get_poster_url(poster_api_path,size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    print(base_url + size + poster_api_path)
    return base_url + size + poster_api_path

