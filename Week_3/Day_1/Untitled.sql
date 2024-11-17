-- CREATE TABLE actors (
-- 	actor_id SERIAL PRIMARY KEY,
-- 	first_name VARCHAR(50) NOT NULL,
-- 	last_name VARCHAR(50) NOT NULL,
-- 	age DATE NOT NULL,
-- 	number_oscars SMALLINT NOT NULL
-- )

-- SELECT * FROM actors

-- INSERT INTO actors(first_name, last_name, age, number_oscars)
-- VALUES ('Matt', 'Damon', '08/10/1970', 5),
-- ('Zendaya', 'Coleman', '08/10/1970', 1),
-- ('Scarlett', 'Johansonn', '11/22/1984', 0),
-- ('Leonardo', 'Decaprio', '11/11/1974', 1),
-- ('Angelina', 'Jolie', '04/06/1975',1)

-- 
------------ QUERYING THE TABLE
-- 
-- SELECT * FROM actors WHERE first_name = 'Zendaya'
-- SELECT first_name FROM actors WHERE number_oscars > 2
-- SELECT first_name FROM actors WHERE number_oscars > 2 AND last_name = 'Damon'
-- SELECT * FROM actors WHERE first_name = 'Matt' OR number_oscars = 5
-- SELECT * FROM actors WHERE first_name NOT = 'Matt'
-- SELECT * FROM actors WHERE last_name ILIKE '%amo%' LIMIT 2
-- SELECT * FROM actors OFFSET 2
-- SELECT * FROM actors ORDER BY number_oscars DESC

-- UPDATE actors
-- SET first_name = 'Tom',
-- last_name = 'Holland'
-- WHERE first_name = 'Matt'
SELECT * FROM actors

-- DELETE FROM actors
-- WHERE actor_id = 7