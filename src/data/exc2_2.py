import psycopg2
from config import config

def crud_update_delete():
    con = None
    try:
        # connect tothe database
        con = psycopg2.connect(**config())
        cursor = con.cursor()

        # the actual query, using update and delete in various ways
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

def main():
    crud_update_delete()

if __name__ == "__main__":
    main()