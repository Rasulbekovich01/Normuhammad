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





