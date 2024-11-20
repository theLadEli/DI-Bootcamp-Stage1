-- HAVING

-- SELECT actors.first_name, movies.movie_title
-- FROM actors
-- INNER JOIN movies
-- ON actors.actor_id = movies.actor_playing_id
-- GROUP BY actors.first_name, movies.movie_title
-- -- Having is used with Group By gives opt to specify the desired output (like WHERE)
-- HAVING actors.first_name ILIKE 'T%'

-- UNION
SELECT first_name, last_name FROM actors
UNION
SELECT movie_title, movie_story FROM movies
ORDER BY first_name