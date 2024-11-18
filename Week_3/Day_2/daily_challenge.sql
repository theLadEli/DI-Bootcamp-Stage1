-- -- PART 1

-- -- PART 1.1

-- CREATE TABLE customer(
-- 	customer_id SERIAL UNIQUE,
-- 	first_name VARCHAR(50),
-- 	last_name VARCHAR(50) NOT NULL
-- );

-- CREATE TABLE customer_profile(
-- 	customer_p_id SERIAL,
-- 	isLoggedIn BOOLEAN DEFAULT FALSE,
-- 	customer_id INTEGER,
-- 	PRIMARY KEY (customer_p_id),
-- 	FOREIGN KEY (customer_id) REFERENCES customer(customer_id)
-- )

-- -- PART 1.2

-- INSERT INTO customer(first_name, last_name)
-- VALUES('John', 'Doe'),
-- ('Jerome','Lalu'),
-- ('Lea', 'Rive')

-- -- PART 1.3

-- INSERT INTO customer_profile(isLoggedIn, customer_id)
-- VALUES(TRUE,1),
-- (FALSE, 2)

-- -- PART 1.4

-- SELECT customer.first_name, customer_profile.isLoggedIn
-- FROM customer
-- INNER JOIN customer_profile
-- ON customer_profile.customer_id = customer.customer_id
-- WHERE customer_profile.isLoggedIn = True

-- SELECT customer.first_name, customer_profile.isLoggedIn
-- FROM customer
-- FULL JOIN customer_profile
-- ON customer_profile.customer_id = customer.customer_id

-- SELECT COUNT(isLoggedIn) as num_logged_in FROM customer_profile WHERE isLoggedIn = True

-- -- PART 2

-- -- PART 2.1

-- CREATE TABLE book(
-- 	book_id SERIAL PRIMARY KEY,
-- 	title TEXT NOT NULL,
-- 	author VARCHAR(50) NOT NULL
-- )

-- -- PART 2.2

-- INSERT INTO book(title, author)
-- VALUES('Alice In Wonderland', 'Lewis Carroll'),
-- ('Harry Potter', 'J.K Rowling'),
-- ('To Kill a Mockingbird', 'Harper Lee')

-- -- PART 2.3

-- CREATE TABLE student(
-- 	student_id SERIAL PRIMARY KEY,
-- 	name VARCHAR(100) NOT NULL UNIQUE,
-- 	age INTEGER CHECK(age<=15)
-- )

-- -- PART 2.4

-- INSERT INTO student(name, age)
-- VALUES('John',12),
-- ('Lera',11),
-- ('Patrick',10),
-- ('Bob',14)

-- -- PART 2.5

-- CREATE TABLE library(
-- 	book_fk_id INTEGER,
-- 	student_fk_id INTEGER,
-- 	borrowed_date DATE,

-- 	PRIMARY KEY (book_fk_id, student_fk_id),
-- 	FOREIGN KEY (book_fk_id) REFERENCES book(book_id) ON DELETE CASCADE ON UPDATE CASCADE,
-- 	FOREIGN KEY (student_fk_id) REFERENCES student(student_id) ON DELETE CASCADE ON UPDATE CASCADE
-- )

-- -- PART 2.6

-- INSERT INTO library(student_fk_id, book_fk_id, borrowed_date)
-- VALUES(1,1,'02/15/2022'),
-- (4,3,'03/03/2021'),
-- (2,1,'05/23/2021'),
-- (4,2,'08/12/2021')

-- -- PART 2.7

SELECT * FROM library, student.name, book.title
