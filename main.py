from random import choice

from flask import Flask, render_template, request, url_for

import tmdb_client

app = Flask(__name__)

VALID_LIST_NAMES = ['popular', 'top_rated', 'upcoming', 'now_playing']

@app.route('/')
def homepage():
    """
    Render the homepage with a list of movies based on the selected filter.
    """
    selected_list = request.args.get('list_name', 'popular')
    if selected_list not in VALID_LIST_NAMES:
        selected_list = 'popular'
    movies = tmdb_client.get_movies(how_many=12, list_name=selected_list)
    return render_template("homepage.html", movies=movies, current_list=selected_list)


@app.route("/movie/<movie_id>")
def movie_details(movie_id):
    """
    Render the movie details page with information about the selected movie.
    """
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
