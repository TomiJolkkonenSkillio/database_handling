import psycopg2
from config import config

# query for all the rows in the person table and print them
def query_all_rows():
    con = None
    try:
        con = psycopg2.connect(**config())
        cursor = con.cursor()
        cursor.execute('SELECT * FROM person;')
        rows = cursor.fetchall()
        print("All records from person: ")
        for row in rows:
            print(row)
        print("\n")
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if con is not None:
            con.close()

# query for the column names in the person table and print them
def query_column_names():
    con = None
    try:
        con = psycopg2.connect(**config())
        cursor = con.cursor()
        cursor.execute("SELECT column_name FROM information_schema.columns WHERE table_name = 'person';")
        columns = cursor.fetchall()
        print("Column names of the table person: ")
        for column in columns:
            print(column[0])
        print("\n")
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if con is not None:
            con.close()

# query for the certificate table column names, as well as the rows, and print them
def query_certificates_columns():
    con = None
    try:
        con = psycopg2.connect(**config())  
        cursor = con.cursor()
        
        cursor.execute("SELECT column_name FROM information_schema.columns WHERE table_name = 'certificates'")
        columns = cursor.fetchall()
        print("Certificates Table Columns:")
        for column in columns:
            print(column[0])
        
        cursor.execute("SELECT * FROM certificates;")
        rows = cursor.fetchall()
        print("\n")
        print("Certificates Table Rows:")
        for row in rows:
            print(row)
        
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if con is not None:
            con.close()

# query person table for average age and print it
def query_person_age():
    con = None
    try:
        con = psycopg2.connect(**config())
        cursor = con.cursor()
        cursor.execute('SELECT AVG(age) FROM person;')
        avg_age = cursor.fetchone()[0]
        print("\n")
        print(f"Average Age: {avg_age}")
        print("\n")
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if con is not None:
            con.close()

# add new row to the certificate table in a way that the inserted
def insert_certificate_parameters(name):
    con = None
    try:
        con = psycopg2.connect(**config())
        cursor = con.cursor()
        cursor.execute(
            'INSERT INTO certificates (name) VALUES (%s);',
            (name)
        )
        con.commit()
        print("Row inserted into certificate table.")
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if con is not None:
            con.close()

# add a new row to the person table by entering values afterwards
def insert_person_parameters(name, age):
    con = None
    try:
        con = psycopg2.connect(**config())
        cursor = con.cursor()
        cursor.execute(
            'INSERT INTO person (name, age) VALUES (%s, %s);',
            (name, age)
        )
        con.commit()
        print("Row inserted into person table.")
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if con is not None:
            con.close()

def main():
    query_all_rows()
    query_column_names()
    query_certificates_columns()
    query_person_age()
    insert_certificate_parameters('Python Basics') # values are taken as function parameters
    insert_person_parameters('John Doe', 30) # values are taken as function parameters

if __name__ == "__main__":
    main()
