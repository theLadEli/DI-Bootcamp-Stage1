-- -- Aggregate Functions

SELECT * FROM actors

-- -- To get the average number of a column we use AVG()
-- SELECT AVG(number_oscars) FROM actors

-- -- Aliases: if we use a field multiple times we can give it an alias to refer back to it in the script later
-- SELECT AVG(number_oscars) AS avg_oscars FROM actors
-- SELECT COUNT(first_name) AS total_actors FROM actors
-- SELECT SUM(number_oscars) AS gm_oscars FROM actors WHERE first_name = 'Zendaya'
-- -- Unique names
-- SELECT DISTINCT first_name FROM actors ORDER BY first_name ASC

-- -- Multiple condition values can be done using 'in ()'
-- SELECT * FROM actors WHERE first_name in ('Tom', 'Zendaya')

-- -- Condition being between two values (for example date ranges)
-- SELECT * FROM actors WHERE age BETWEEN '1970-01-01' AND '1975-01-01'

-- -- If we use more then one field in an aggregate function, we have to use group by to define which field should be used to organise the output
-- SELECT first_name, last_name, MIN(number_oscars) FROM actors GROUP BY last_name, first_name;

-- -- Subqueries
-- -- Don't have to select *, can specify only few fields
-- SELECT *
-- FROM actors
-- WHERE number_oscars = (SELECT MAX (number_oscars) FROM actors)