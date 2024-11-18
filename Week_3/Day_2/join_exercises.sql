CREATE TABLE countries(
	country_id SERIAL,
	country_name TEXT,
	actor_id INTEGER,

	PRIMARY KEY(country_id),
	FOREIGN KEY(actor_id) REFERENCES actors(actor_id)
)