import psycopg2
from psycopg2 import sql

# Database connection parameters
db_params = {
    'dbname': 'Demo',
    'user': 'postgres',
    'password': '1234',
    'host': 'localhost',
    'port': 5433
}

# Connect to the PostgreSQL database
conn = psycopg2.connect(**db_params)
cursor = conn.cursor()

# cursor.execute('DROP TABLE IF EXISTS STUDENTS')
create_script = ''' CREATE TABLE IF NOT EXISTS STUDENTS (
                            id          SERIAL PRIMARY KEY,
                            name        VARCHAR(255) NOT NULL)'''
        
cursor.execute(create_script)


while True:
    print("1. Add Students \t2. Update Students \t3. Delete Students \t4. Show Students List \t5. Exit")
    choice = input("Enter your choice : ")
    if choice == '1':
        num = int(input("How many students you want to add : "))

        insert_query = sql.SQL("INSERT INTO STUDENTS (name) VALUES (%s)")

        for _ in range(num):
            user_name = input("Enter a name to add: ")
            cursor.execute(insert_query, (user_name,))
        print("Name added to the database successfully.")
        conn.commit()

    elif choice == "2":
        num = int(input("How many students you want to update : "))

        update_query = sql.SQL("UPDATE STUDENTS SET name = %s WHERE name = %s")

        for _ in range(num):
            old_name = input("Enter the current name: ")
            new_name = input("Enter the new name: ")
            cursor.execute(update_query, (new_name, old_name))
        print("Name updated from the database successfully.")
        conn.commit()

    elif choice == "3":
        num = int(input("How many students you want to delete : "))

        delete_query = sql.SQL("DELETE FROM STUDENTS WHERE name = %s")

        for _ in range(num):
            user_name = input("Enter the name to delete: ")
            cursor.execute(delete_query, (user_name,))
        print("Name deleted from the database successfully.")
        conn.commit()

    elif choice == "4":
        # num = int(input("How many students details you want to see : "))

        # select_query = sql.SQL("SELECT name FROM STUDENTS WHERE name = %s")

        # for _ in range(num):
        #     user_name = input("Enter a name to search for: ")
        #     cursor.execute(select_query, (user_name,))
        #     result = cursor.fetchone()
        #     if result:
        #         print("Name found:", result[0])
        #     else:
        #         print("Name not found:", user_name)
        # conn.commit()
        cursor.execute("SELECT * FROM STUDENTS")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        print()
    elif choice == "5":
        break


# Commit the changes
# conn.commit()

# Close the connection
cursor.close()
conn.close()

