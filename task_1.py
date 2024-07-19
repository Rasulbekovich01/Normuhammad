import psycopg2

def connect_to_db( 


database = 'n48',
user = 'postgres',
host = 'localhost',
port = '5432',
password = '1305'):

    conn =  psycopg2.connect(database = 'n48', user= 'postgres', host = 'localhost', port = '5432', password = '1305')
    return conn 

def create_product_table(conn):
    with conn.cursor() as cur:
        create_table_query = """
            CREATE TABLE IF NOT EXISTS book (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                price int not null,
                color VARCHAR(50) NOT NULL,
                image varchar(500) not null
            );
        """
        cur.execute(create_table_query)
        conn.commit()
        print("Table created successfully.")

# ------------------2-misol--------------------------------

import psycopg2

def connect_to_db( 


database = 'n48',
user = 'postgres',
host = 'localhost',
port = '5432',
password = '1305'):

    conn =  psycopg2.connect(database = 'n48', user= 'postgres', host = 'localhost', port = '5432', password = '1305')
    return conn 

def create_product_table(conn):
    with conn.cursor() as cur:
        create_table_query = """
            CREATE TABLE IF NOT EXISTS book (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                price int not null,
                color VARCHAR(50) NOT NULL,
                image varchar(500) not null
            );
        """
        cur.execute(create_table_query)
        conn.commit()
        print("Table created successfully.")

def insert_product(conn, name, price, color, image):
    try:
        with conn.cursor() as cur:
            cur.execute("""
                INSERT INTO product (name, price, color, image)
                VALUES (%s, %s, %s, %s);
            """, (name, price, color, image))
            conn.commit()
            print("Product inserted successfully.")
    except Exception as e:
        print(f"Error inserting product: {e}")

def select_all_products(conn):
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM product;")
            products = cur.fetchall()
            for product in products:
                print(product)
    except Exception as e:
        print(f"Error selecting products: {e}")

def update_product(conn, product_id, name, price, color, image):
    try:
        with conn.cursor() as cur:
            cur.execute("""
                UPDATE product
                SET name = %s, price = %s, color = %s, image = %s
                WHERE id = %s;
            """, (name, price, color, image, product_id))
            conn.commit()
            print("Product updated successfully.")
    except Exception as e:
        print(f"Error updating product: {e}")

def delete_product(conn, product_id):
    try:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM product WHERE id = %s;", (product_id,))
            conn.commit()
            print("Product deleted successfully.")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    conn = connect_to_db()

    conn.close()

# ------------3-misol----------------------
class Alphabet:
    def __init__(self):
        self.letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.index = 0

    def __iter__(self):
        self.index = 0  
        return self

    def __next__(self):
        if self.index < len(self.letters):
            letter = self.letters[self.index]
            self.index += 1
            return letter
        else:
            raise StopIteration


alphabet = Alphabet()
for letter in alphabet:
    print(letter)


# ---------------------------5-misol-------------------

import psycopg2

def connect_to_db(database='n48', user='postgres', host='localhost', port='5432', password='1305'):
    try:
        conn = psycopg2.connect(database=database, user=user, host=host, port=port, password=password)
        print("Connection to database established successfully.")
        return conn
    except Exception as e:
        print(f"Error connecting to database: {e}")
        return None

def create_product_table(conn):
    try:
        with conn.cursor() as cur:
            create_table_query = """
                CREATE TABLE IF NOT EXISTS product (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(100) NOT NULL,
                    price INT NOT NULL,
                    color VARCHAR(50) NOT NULL,
                    image VARCHAR(500) NOT NULL
                );
            """
            cur.execute(create_table_query)
            conn.commit()
            print("Table created successfully.")
    except Exception as e:
        print( e)



    def save(self, conn):
        try:
            with conn.cursor() as cur:
                insert_query = """
                    INSERT INTO product (name, price, color, image)
                    VALUES (%s, %s, %s, %s);
                """
                cur.execute(insert_query, (self.name, self.price, self.color, self.image))
                conn.commit()
                print("Product saved successfully.")
        except Exception as e:
            print(e)
# -----------------6-misol-------------------------

import psycopg2

class DbConnect:
    def __init__(self, database, user, host, port, password):
        self.database = database
        self.user = user
        self.host = host
        self.port = port
        self.password = password

    def __enter__(self):
        try:
            self.conn = psycopg2.connect(database=self.database, user=self.user, host=self.host, port=self.port, password=self.password)
            self.cur = self.conn.cursor()
            print("Connection to database established successfully.")
            return self.conn, self.cur
        except Exception as e:
            print(f"Error connecting to database: {e}")
            raise

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_tb is None:
            self.conn.commit()
        else:
            self.conn.rollback()
            print(f"Error occurred: {exc_val}")
        self.cur.close()
        self.conn.close()
        print("Connection closed.")
















