import psycopg2
from config import config

def create_accounts_table(cursor):
    # Create the 'accounts' table if it doesn't exist yet
    SQL = '''
    CREATE TABLE IF NOT EXISTS accounts (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100),
        balance DECIMAL(10, 2) NOT NULL
    );
    '''
    cursor.execute(SQL)

def transaction():
    con = None
    try:
        # connect to database
        con = psycopg2.connect(**config())
        cursor = con.cursor()

        create_accounts_table(cursor)

        # initial data
        cursor.execute('INSERT INTO accounts (name, balance) VALUES (%s, %s) ON CONFLICT DO NOTHING;', ('Alice', 1000.00))
        cursor.execute('INSERT INTO accounts (name, balance) VALUES (%s, %s) ON CONFLICT DO NOTHING;', ('Bob', 1000.00))
        con.commit()

        # start transaction
        con.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_REPEATABLE_READ)

        transfer_amount = 100
        account_from = 1  # debit account
        account_to = 2  # credit account

        # check if 1st account has enough balance
        cursor.execute('SELECT balance FROM accounts WHERE id = %s;', (account_from,))
        balance = cursor.fetchone()

        if balance is None:
            print(f"account {account_from} not found.")
            return
        
        if balance[0] < transfer_amount:
            print(f"no money in accountt {account_from}.")
            return
        
        # take oney from debit
        cursor.execute('UPDATE accounts SET balance = balance - %s WHERE id = %s;', (transfer_amount, account_from))

        # put money to credit
        cursor.execute('UPDATE accounts SET balance = balance + %s WHERE id = %s;', (transfer_amount, account_to))

        # commit transaction (both updates must be OK)
        con.commit()
        print(f"Transaction successful: {transfer_amount} transferred from debit {account_from} to credit {account_to}.")

        # Fetch and print the updated table to verify
        cursor.execute('SELECT * FROM accounts;')
        rows = cursor.fetchall()

        print("Table contents after transaction:")
        for row in rows:
            print(f"ID: {row[0]}, Name: {row[1]}, Balance: {float(row[2]):.2f}")

        cursor.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error: {error}")
        if con is not None:
            con.rollback()  # rollback if any errors occur during transaction
            print("Transaction rolled back.")
    finally:
        if con is not None:
            con.close()

def main():
    transaction()

if __name__ == "__main__":
    main()
