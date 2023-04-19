from random import shuffle
import requests
from config import API_TOKEN, HEADERS, BASE_URL, IMAGE_BASE_URL, NO_IMAGE_AVAILABLE


def get_movie_list(list_name):
    """
    Retrieve a list of movies based on the given list name.
    """
    url = f'{BASE_URL}/movie/{list_name}'
    params = {"api_key": API_TOKEN}
    try:
        response = requests.get(url, headers=HEADERS, params=params)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(e)
        return None

    return response.json()


def get_image_url(poster_api_path, size="w342"):
    """
    Generate the image URL from the poster API path.
    """
    if poster_api_path is None:
        return NO_IMAGE_AVAILABLE

    return IMAGE_BASE_URL + size + poster_api_path


def get_movies(how_many, list_name="popular"):
    """
    Retrieve and shuffle a list of movies, returning the specified number of them.
    """
    movie_data = get_movie_list(list_name)
    if movie_data is None:
        return []

    shuffle(movie_data["results"])
    return movie_data["results"][:how_many]


def get_single_movie(movie_id):
    """
    Retrieve details for a single movie.
    """
    url = f'{BASE_URL}/movie/{movie_id}'
    params = {"api_key": API_TOKEN}
    try:
        response = requests.get(url, headers=HEADERS, params=params)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(e)
        return None

    return response.json()


def get_movie_credits(movie_id):
    """
    Retrieve the cast credits for a movie.
    """
    url = f'{BASE_URL}/movie/{movie_id}/credits'
    params = {"api_key": API_TOKEN}
    try:
        response = requests.get(url, headers=HEADERS, params=params)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(e)
        return []

    return response.json()['cast']


def get_movie_images(movie_id):
    """
    Retrieve the images associated with a movie.
    """
    url = f"{BASE_URL}/movie/{movie_id}/images"
    params = {"api_key": API_TOKEN}
    try:
        response = requests.get(url, headers=HEADERS, params=params)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(e)
        return {}

    return response.json()
