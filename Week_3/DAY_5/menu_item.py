# # PART 1
import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

DB_HOST = os.getenv('HOSTNAME')
DB_USERNAME = os.getenv('USERNAME')
DB_PASSWORD = os.getenv('PASSWORD')
DB_DATABASE = os.getenv('DATABASE')
DB_PORT = os.getenv('PORT')

# Connecting to the database
connection = psycopg2.connect(
    host = DB_HOST,
    user = DB_USERNAME,
    password = DB_PASSWORD,
    dbname = DB_DATABASE,
    port = DB_PORT
)

cursor = connection.cursor()

# # Prevent table being created if already exists
# cursor.execute('DROP TABLE IF EXISTS menu_items')

# # SQL code to create table, stored in a variable for later execution
# create_table_query = f'''CREATE TABLE menu_items(
#                             item_id SERIAL PRIMARY KEY,
#                             item_name VARCHAR(30) NOT NULL,
#                             item_price SMALLINT DEFAULT 0
#                         )'''

# # Executing the sql code we saved to a variable
# cursor.execute(create_table_query)

# connection.commit()

class MenuItem:
    def __init__(self, name, price):
        self.name = name,
        self.price = price
    
    def save(self):
        sql_query = '''INSERT INTO menu_items (item_name, item_price)
                        VALUES (%s, %s)
                        '''%(self.name, self.price)
        # %s is a placeholder value we can specify in order after usage to avoid character errors
        cursor.execute(sql_query)
        connection.commit()

    def delete(self):
        sql_query = f'''DELETE FROM menu_items WHERE item_name = %s'''%(self.name)
        cursor.execute(sql_query)
        connection.commit()

    def update(self, new_name, new_price):
        sql_query = f'''UPDATE... '''


hamburger = MenuItem('Burger','60')
hamburger.save()