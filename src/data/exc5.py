from queries import *
from exc2_1 import *
from exc2_2 import *
from exc3 import *
from exc4 import *
from exc6 import *

def ask_input():
    print("Database Application")
    print("Choose an action to perform:")
    print("1. Select everything from the table 'person'")
    print("2. Query for the column names in the person table and print them")
    print("3. Query for the certificate table column names and rows, then print them")
    print("4. Query the person table for the average age and print it")
    print("5. Add a new row to the certificate table by entering values")
    print("6. Add a new row to the person table by entering values")
    print("7. Update an existing row in the person table")
    print("8. Update an existing row in the certificate table")
    print("9. Remove an existing row from the person table")
    print("10. Remove an existing row from the certification table")
    print("11. Create the 'accounts' table if it doesn't exist yet")
    print("12. Create fake transactions between debit and credit accounts")
    print("13. Create a new table")
    print("14. Create an image blob")

    choice = int(input("Enter the number of your choice: "))

    if choice == 1:
        print(query_person())
    elif choice == 2:
        print(query_column_names())
    elif choice == 3:
        print(query_certificates_columns())
    elif choice == 4:
        print(query_person_age())
    elif choice == 5:
        print(insert_certificate_parameters('Python Basics'))
    elif choice == 6:
        print(insert_person_parameters('John Doe', 30))
    elif choice == 7:
        id = int(input("Enter id of the person to update: "))
        name = input("Enter new name: ")
        age = int(input("Enter new age: "))
        print(update_person(id, name, age=age))
    elif choice == 8:
        id = int(input("Enter id of the certificate to update: "))
        name = input("Enter new certificate name: ")
        person_id = input("Enter new person ID (or leave blank): ")
        person_id = None if person_id == "" else int(person_id)
        print(update_certificates(id, name=name, person_id=person_id))
    elif choice == 9:
        id = int(input("Enter id to delete: "))
        print(delete_person(id))
    elif choice == 10:
        id = int(input("Enter id to delete: "))
        print(delete_certificates(id))
    elif choice == 11:
        print(create_accounts_table(cursor))
    elif choice == 12:
        print(transaction())
    elif choice == 13:
        print(create_table())
    elif choice == 14:
        print(image_blob())
    else:
        print("Invalid choice. Please try again.")

def main():
    ask_input()

if __name__ == "__main__":
    main()
