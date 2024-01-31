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

# cursor.execute('DROP TABLE IF EXISTS EMPLOYEES')
create_script = ''' CREATE TABLE IF NOT EXISTS EMPLOYEES (
                            id          SERIAL PRIMARY KEY,
                            name        VARCHAR(255),
                            department  VARCHAR(255),
                            salary      int)'''
        
cursor.execute(create_script)


while True:
    print("1. Add Employees \t2. Update Employees \t3. Delete Employees \t4. Show Employees List \t5. Exit")
    choice = input("Enter your choice : ")
    if choice == '1':
        num = int(input("How many employees you want to add : "))

        insert_query = "INSERT INTO employees (name, department, salary) VALUES (%s, %s, %s)"

        for _ in range(num):
            name = input("Enter name: ")
            department = input("Enter department: ")
            salary = input("Enter salary: ")

            try:
                salary_value = float(salary)
                cursor.execute(insert_query, (name, department, salary_value))
            except ValueError:
                print("Invalid input for salary. Please enter a numeric value.")
        
        print("Added to the database successfully.")
        conn.commit()

    elif choice == "2":
        num = int(input("How many employees you want to update : "))

        def update_name(cursor, old_name, new_name):
            cursor.execute("UPDATE employees SET name = %s WHERE name = %s", (new_name, old_name))

        def update_department(cursor, name, new_department):
            cursor.execute("UPDATE employees SET department = %s WHERE name = %s", (new_department, name))

        def update_salary(cursor, name, new_salary):
            cursor.execute("UPDATE employees SET salary = %s WHERE name = %s", (new_salary, name))

        for _ in range(num):
            name = input("Enter the name of the employee to update: ")
            ch = input("Which field do you want to update : 1.Name \t2.Department \t3.Salary : ")

            if ch == '1':
                new_name = input("Enter the new name: ")
                update_name(cursor, name, new_name)
            elif ch == '2':
                new_department = input("Enter the new department: ")
                update_department(cursor, name, new_department)
            elif ch == '3':
                new_salary = float(input("Enter the new salary: "))
                update_salary(cursor, name, new_salary)
            else:
                print("Invalid choice. Please enter 'name', 'department', or 'salary'.")
        
        print("Update the database successfully.")
        conn.commit()

    elif choice == "3":
        num = int(input("How many employees you want to delete : "))

        def delete_name(cursor, name):
            cursor.execute("DELETE FROM employees WHERE name = %s", (name,))

        def delete_department(cursor, department):
            cursor.execute("DELETE FROM employees WHERE department = %s", (department,))

        def delete_salary(cursor, salary):
            cursor.execute("DELETE FROM employees WHERE salary = %s", (salary,))

        for _ in range(num):
            ch = input("Which field do you want to use for deletion : 1.Name \t2.Department \t3.Salary : ")

            if ch == '1':
                name = input("Enter the name : ")
                delete_name(cursor, name)
            elif ch == '2':
                department = input("Enter the department : ")
                delete_department(cursor, department)
            elif ch == '3':
                salary = float(input("Enter the salary : "))
                delete_salary(cursor, salary)
    
        print("Deleted from the database successfully.")
        conn.commit()

    elif choice == "4":
        # num = int(input("How many Employees details you want to see : "))

        # select_query = sql.SQL("SELECT name FROM EMPLOYEES WHERE name = %s")

        # for _ in range(num):
        #     user_name = input("Enter a name to search for: ")
        #     cursor.execute(select_query, (user_name,))
        #     result = cursor.fetchone()
        #     if result:
        #         print("Name found:", result[0])
        #     else:
        #         print("Name not found:", user_name)
        # conn.commit()
        cursor.execute("SELECT * FROM EMPLOYEES")
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

