import requests

Api_token = "eyJhbGciOiJIUzI1NiJ9eyJhdWQiOiI0ODg4ZWYxN2I2MWRjZTgzMWZiNGEwYjdiMjA4YTliNCIsInN1YiI6IjYzODcwMzJjMjI5YWUyMTViNDYwNTc1YSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.OYs7rxZFJzRMpix6mv1Bos89sX42SekoUY36kZAkJ_A"

headers = {
    "Authorization": f"Bearer {Api_token}",
    "Content-Type": "application/json; charset=utf-8"}


def get_popular_movies():
    page = 'https://api.themoviedb.org/3/movie/popular'
    response = requests.get(page, headers=headers)
    data = response.json()
    print(data)