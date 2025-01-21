import psycopg2
from config import config

# update an existing row in the person table
def update_person(id, name=None, age=None, student=None):
    con = None
    try:
        con = psycopg2.connect(**config())
        cursor = con.cursor()
        query = 'UPDATE person SET '
        values = []

        if id:
            query += 'id = %s, '
            values.append(id)
        if name:
            query += 'name = %s, '
            values.append(name)
        if age:
            query += 'age = %s, '
            values.append(age)
        if student:
            query+= 'student = %s, '
            values.append(student)

        query = query.rstrip(', ') + ' WHERE id = %s;'
        values.append(id)
        cursor.execute(query, tuple(values))
        con.commit()
        print("Person row updated.")
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if con is not None:
            con.close()

# update an existing row in the certificate table
def update_certificates(id, name=None, person_id=None):
    con = None
    try:
        con = psycopg2.connect(**config())
        cursor = con.cursor()
        query = 'UPDATE certificates SET '
        values = []

        if id:
            query += 'id = %s, '
            values.append(id)
        if name:
            query += 'name = %s, '
            values.append(name)
        if person_id:
            query += 'person_id = %s, '
            values.append(person_id)

        query = query.rstrip(', ') + ' WHERE id = %s;'
        values.append(id)
        cursor.execute(query, tuple(values))
        con.commit()
        print("Certificate row updated.")
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if con is not None:
            con.close()

# remove an existing row from the person table
def delete_person(id):
    con = None
    try:
        con = psycopg2.connect(**config())
        cursor = con.cursor()
        cursor.execute('DELETE FROM person WHERE id = %s;', (id,))
        con.commit()
        print("Person row deleted.")
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if con is not None:
            con.close()

# remove an existing row from the certification table
def delete_certificates(id):
    con = None
    try:
        con = psycopg2.connect(**config())
        cursor = con.cursor()
        cursor.execute('DELETE FROM certificates WHERE id = %s;', (id,))
        con.commit()
        print("Certificate row deleted.")
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if con is not None:
            con.close()

def main():
    update_person(4, 'Alice', age=30) # values are taken as function parameters
    update_certificates(2, name='Scrum', person_id=None) # values are taken as function parameters
    delete_person(2) # the id of the row to be deleted is taken as a function parameter
    delete_certificates(1) # the id of the row to be deleted is taken as a function parameter

if __name__ == "__main__":
    main()
