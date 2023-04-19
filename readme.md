# Flask Movie Database App

## Table of Contents
* [General Info](#general-information)
* [Technologies Used](#technologies-used)
* [Features](#features)
* [Screenshots](#screenshots)
* [Setup](#setup)
* [Project Status](#project-status)
* [Acknowledgements](#acknowledgements)
* [License](#license)


## General Information
This Flask web application allows users to browse and discover movies from the popular TMDb (The Movie Database) API.

Users can view popular, now playing, top-rated, and upcoming movies, as well as individual movie details and cast information.


## Technologies Used

   -Flask - A lightweight Python web framework

   -Bootstrap - A popular CSS framework for responsive web design

   -TMDb API - A community-driven movie and TV information database


## Features

   -Browse movies by category: Popular, Now Playing, Top Rated, and Upcoming
   
   -View movie details, including tagline, overview, budget, and genres
   
   -See cast information with actor images and character names
   
   -Responsive design for optimal viewing on various screen sizes


## Screenshots
![Example screenshot](https://raw.githubusercontent.com/deciever5/movies_catalogue/master/app_view.JPG)
<!-- If you have screenshots you'd like to share, include them here. -->


## Setup
1.Clone the repository:

      git clone https://github.com/yourusername/flask-movie-database-app.git
      cd flask-movie-database-app

2.Create a virtual environment and install dependencies:

      python3 -m venv venv
      source venv/bin/activate
      pip install -r requirements.txt

3.Set up your TMDb API key:

  -Register for a free account at TMDb and request an API key from your account settings.
  
  -Replace the Api_token variable in the tmdb_client.py file with your own API key.

4.Run the application:

      export FLASK_APP=main.py
      flask run

5.Open your browser and visit http://localhost:5000 to view the app.


## Project Status

Project is: _in progress_


## Acknowledgements

   -TMDb for providing the movie data and images
   
   -Bootstrap for the responsive design templates and components
   
   -OpenAI for providing guidance and suggestions through ChatGPT


<!-- Optional -->
## License
This project is licensed under the MIT License.

<!-- You don't have to include all sections - just the one's relevant to your project -->
