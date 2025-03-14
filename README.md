# movie_db
A Movie Database for CS 586 Intro to DBMS
The database consists of 7 tables:
1. Movies (id, title, release_year, certificate, runtime, imdb_rating, number_of_votes, gross)
2. Actors (id, first_name, last_name)
3. Directors (id, first_name, last_name)
4. Genres (id, name)
5. Movie_Director_Rel(movie_id, director_id)
- movie_id is a foreign key referencing Movies(id)
- director_id is a foreign key referencing Directors(id)
6. Movie_Actor_Rel (movie_id, actor_id)
- movie_id is a foreign key referencing Movies(id)
- actor_id is a foreign key referencing Actors(id)
7. Movie_Genre_Rel (movie_id, genre_id)
- movie_id is a foreign key referencing Movies(id)
- genre_id is a foreign key referencing Genres(id)
