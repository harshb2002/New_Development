import psycopg2
import psycopg2.extras



hostname = 'localhost'
database = 'Demo'
username = 'postgres'
pwd = '1234'
port_id = 5433
conn = None
cur = None

try:
    conn = psycopg2.connect(
        host=hostname,
        database=database,
        user=username,
        password=pwd,
        port=port_id
    )

    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    cur.execute('DROP TABLE IF EXISTS employee')

    # Create query
    create_script = ''' CREATE TABLE IF NOT EXISTS employee (
                        id          int PRIMARY KEY,
                        name        VARCHAR(255) NOT NULL,
                        salary      int,
                        email       VARCHAR(255),
                        phone       VARCHAR(12))'''
    
    cur.execute(create_script)

    # Insert query
    insert_script = ''' INSERT INTO employee (id,name, salary, email, phone)
                        VALUES (%s,%s, %s, %s, %s)'''
    insert_value = [(1,'Rutul',10000,'rutul@gmail.com','4567892130'),
                    (2,'Kamiyab',12000,'kamiyab@gmail.com','7894561230'),
                    (3,'Diya',5000,'diya@gmail.com','1597536540'),
                    (4,'Jay',11000,'jay@gmail.com','25814733690')]
    for record in insert_value:
        cur.execute(insert_script, record)

    # Update query
    update_script = 'UPDATE EMPLOYEE SET salary = salary + (salary * 0.5)'
    cur.execute(update_script)


    # Delete query
        
    delete_script = 'DELETE FROM EMPLOYEE WHERE name = %s'
    delete_record = ('Diya',)
    cur.execute(delete_script, delete_record)
        
    # Select query
    cur.execute("SELECT * FROM EMPLOYEE")
    for record in cur.fetchall():
        print(record['name'], record['salary'])


    conn.commit()


except Exception as e:
    print(e)

finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()