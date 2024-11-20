import psycopg2

HOSTNAME = 'localhost'
USERNAME = 'postgres'
PASSWORD = '1290'
DATABASE = 'countries'
PORT = '5432'

# Connecting to the database
connection = psycopg2.connect(
    host=HOSTNAME,
    user=USERNAME,
    password=PASSWORD,
    dbname=DATABASE,
    port=PORT
)


cursor = connection.cursor()

# Prevent table being created if already exists
cursor.execute('DROP TABLE IF EXISTS random_countries')

# SQL code to create table, stored in a variable for later execution
create_table_query = f'''CREATE TABLE random_countries(
                        id SERIAL PRIMARY KEY,
                        name VARCHAR(100) NOT NULL,
                        capital VARCHAR(100) NOT NULL,
                        flag_code VARCHAR(100),
                        population INTEGER
                        )'''

# Executing the sql code we saved to a variable
cursor.execute(create_table_query)

connection.commit()

# results = cursor.fetchall()
# connection.close()

# for item in results:
#         print(item)