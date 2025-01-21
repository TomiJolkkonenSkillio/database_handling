import psycopg2
from config import config

def create_table():
    con = None
    try:
        # connect to database
        con = psycopg2.connect(**config())
        cursor = con.cursor()

        # the actual query
        SQL = '''
        CREATE TABLE IF NOT EXISTS new_table (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            age INT NOT NULL,
            email VARCHAR(100) UNIQUE
        );
        '''
        cursor.execute(SQL)

        con.commit()
        print("Table created successfully.")

        cursor.execute('SELECT * FROM new_table;')
        rows = cursor.fetchall()

        # printout
        print("Table contents:")
        for row in rows:
            print(row)

        cursor.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if con is not None:
            con.close()

def main():
    create_table()

if __name__ == "__main__":
    main()
