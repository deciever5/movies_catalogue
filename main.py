from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template('index.html')


Api_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI0ODg4ZWYxN2I2MWRjZTgzMWZiNGEwYjdiMjA4YTliNCIsInN1YiI6IjYzODcwMzJjMjI5YWUyMTViNDYwNTc1YSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.OYs7rxZFJzRMpix6mv1Bos89sX42SekoUY36kZAkJ_A"

if __name__ == '__main__':
    app.run(debug=True)