-- -- FOREIGN KEY: PARENT AND CHILD TABLES

-- -- Creating a child table to the actors table
-- CREATE TABLE movies(
-- 	movie_id SERIAL,
-- 	movie_title VARCHAR(100) NOT NULL,
-- 	movie_story TEXT,
-- 	actor_playing_id INTEGER,
-- 	-- Now i've defined the fields, I can specify the keys
-- 	PRIMARY KEY (movie_id),
-- 	FOREIGN KEY (actor_playing_id) REFERENCES actors(actor_id)
-- )

-- INSERT INTO movies (movie_title, movie_story, actor_playing_id)
-- VALUES ('Dune', 'Multiplanetary sci-fi movie.',
-- 	(SELECT actor_id FROM actors WHERE first_name = 'Zendaya' AND last_name = 'Coleman')
-- );

SELECT * FROM movies