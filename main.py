from random import random, choice
from flask import Flask, render_template

import tmdb_client

app = Flask(__name__)


@app.route('/')
def homepage():
    movies = tmdb_client.get_movies(how_many=12)
    return render_template("homepage.html", movies=movies)


@app.route("/movie/<movie_id>")
def movie_details(movie_id):
    details = tmdb_client.get_single_movie(movie_id)
    cast = tmdb_client.get_movie_credits(movie_id)
    movie_images = tmdb_client.get_movie_images(movie_id)
    selected_backdrop = choice(movie_images['backdrops'])
    return render_template("movie_details.html", movie=details, cast=cast, selected_backdrop=selected_backdrop)


@app.context_processor
def utility_processor():
    def tmdb_image_url(path, size):
        return tmdb_client.get_image_url(path, size)

    return {"tmdb_image_url": tmdb_image_url}


if __name__ == '__main__':
    app.run(debug=True)
