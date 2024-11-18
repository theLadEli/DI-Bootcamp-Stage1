-- CREATE TABLE producers(
-- 	producer_id SERIAL,
-- 	first_name VARCHAR(50),
-- 	last_name VARCHAR(50),
-- 	movie_id INTEGER,
-- 	PRIMARY KEY (producer_id),
-- 	FOREIGN KEY (movie_id) REFERENCES movies(movie_id)
-- )

-- INSERT INTO producers(first_name, last_name, movie_id)
-- VALUES('John', 'Doe',
-- 	(SELECT movie_id FROM movies WHERE movie_title = 'Spider Man')
-- ),('Sam', 'Someone',
-- 	(SELECT movie_id FROM movies WHERE movie_title = 'JoJo Rabbit')
-- )

SELECT producers.first_name, producers.last_name, movies.movie_title
FROM movies
INNER JOIN producers
ON producers.movie_id = movies.movie_id