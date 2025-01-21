import psycopg2
import requests
from io import BytesIO
from config import config

def create_image_table(cursor):
    # create the 'images' table with a BYTEA column for the image
    SQL = '''
    CREATE TABLE IF NOT EXISTS images (
        id SERIAL PRIMARY KEY,
        image_name VARCHAR(255),
        image_data BYTEA
    );
    '''
    cursor.execute(SQL)

def insert_image_to_db(cursor, image_url, image_name):
    # fetch image from the internet
    response = requests.get(image_url)
    if response.status_code != 200:
        print(f"Failed to retrieve image from {image_url}")
        return

    # convert the image to binary format
    image_data = BytesIO(response.content).read()

    #insert image into the database
    insert_query = "INSERT INTO images (image_name, image_data) VALUES (%s, %s);"
    cursor.execute(insert_query, (image_name, image_data))

def retrieve_image_from_db(cursor, image_id, output_file):
    # retrieve image data from the database
    cursor.execute("SELECT image_data FROM images WHERE id = %s;", (image_id,))
    result = cursor.fetchone()

    if result:
        # write the image to a file
        with open(output_file, 'wb') as f:
            f.write(result[0])
        print(f"Image saved as {output_file}")
    else:
        print("Image not found in the database.")

def transaction():
    con = None
    try:
        # connect to database
        con = psycopg2.connect(**config())
        cursor = con.cursor()

        # create the images table if it doesn't exist
        create_image_table(cursor)

        # example image url
        image_url = "https://pbs.twimg.com/media/FtYsR78aIAA8_6k.jpg"
        image_name = "FtYsR78aIAA8_6k"

        # insert image into the database
        insert_image_to_db(cursor, image_url, image_name)
        con.commit()
        print(f"Image '{image_name}' inserted into the database.")

        # retrieve image and save it as a file
        retrieve_image_from_db(cursor, 1, "retrieved_image.jpg")

        cursor.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error: {error}")
        if con is not None:
            con.rollback()  # rollback if any error occurs during transaction
            print("Transaction rolled back.")
    finally:
        if con is not None:
            con.close()

def main():
    transaction()

if __name__ == "__main__":
    main()
