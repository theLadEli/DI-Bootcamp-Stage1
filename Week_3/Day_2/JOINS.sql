-- -- JOINS

-- -- INNER JOINS: Only shows if the data matches (if the second table has data to match with the first)
-- -- FULL JOINS: You get all the data even if some have values of Null

-- -- Start by defining the fields from each table you want, can do from multiple tables if you specify which table the field belongs to
-- SELECT actors.first_name, actors.last_name, movies.movie_title
-- -- The first table (doesn't matter if parent or child, either)
-- FROM actors
-- -- The second table
-- INNER JOIN movies
-- -- Now define how they are connected
-- ON actors.actor_id = movies.actor_playing_id