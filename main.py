from flask import Flask, render_template

from tmdb_client import get_popular_movies, get_poster_url

app = Flask(__name__)


@app.route('/')
def homepage():
    movies = [i for i in range(6)]
    get_poster_url("/pFlaoHTZeyNkG83vxsAJiGzfSsa.jpg")
    return render_template("homepage.html", movies=movies)


if __name__ == '__main__':
    app.run(debug=True)
