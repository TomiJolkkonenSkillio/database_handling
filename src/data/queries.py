import psycopg2
from config import config

def query_person():
    con = None
    try:
        # connect tothe database
        con = psycopg2.connect(**config())
        cursor = con.cursor()

        # the actual query
        SQL = 'SELECT * FROM person;'
        cursor.execute(SQL)

        # fetch all rows from the result
        row = cursor.fetchall()
        for i in row:
            print(i)

        # close cursor
        cursor.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if con is not None:
            con.close()

query_person()