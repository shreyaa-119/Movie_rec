Movie Recommendation System (Flask + MySQL)
This is a movie recommendation system built using Python Flask and MySQL.
It connects to a local MySQL database and allows users to browse movies, rate them, and view top-rated movies based on genre.

Overview
The project demonstrates how Flask can interact with a relational database to serve dynamic content on a web interface.
It uses data from a MySQL database containing movies, links, and user ratings.

Tech Stack
Frontend: HTML, CSS (Flask Templates)
Backend: Python Flask
Database: MySQL
Editor: VS Code
Version Control: Git and GitHub

Features
Fetches movies directly from the MySQL database
Displays top-rated movies by genre
Allows users to submit movie ratings
Lightweight Flask frontend with simple routing
Easy to extend for advanced recommendation models

Database Details
Database name: moviedb

Tables included:
movies – stores movie details (movie_id, title, genres)
links – stores imdb_id and tmdb_id for each movie

ratings – stores user ratings (user_id, movie_id, rating, timestamp)
