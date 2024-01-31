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

    cur.execute('DROP TABLE IF EXISTS student')

    # Create query
    create_script = ''' CREATE TABLE IF NOT EXISTS student (
                        id          int PRIMARY KEY,
                        name        VARCHAR(255) NOT NULL,
                        age         int,
                        email       VARCHAR(255),
                        phone       VARCHAR(12))'''

    cur.execute(create_script)
    
    #Insert query

    insert_script = ''' INSERT INTO student (id,name, age, email, phone)
                        VALUES (%s,%s, %s, %s, %s)'''
    insert_value = [(1,'Harsh',21,'harsh@gmail.com','4567892130'),
                    (2,'Kamiyab',20,'kamiyab@gmail.com','7894561230'),
                    (3,'Rutul',20,'rutul@gmail.com','1597536540'),
                    (4,'Jay',19,'jay@gmail.com','25814733690')]
    for record in insert_value:
        cur.execute(insert_script, record)

    # Update query
    update_script = 'UPDATE STUDENT SET age = age + 1'
    cur.execute(update_script)

    # Delete query
    delete_script = 'DELETE FROM STUDENT WHERE email = %s'
    delete_record = ('rutul@gmail.com',)
    cur.execute(delete_script, delete_record)


    # Select query
    cur.execute("SELECT * FROM STUDENT")
    for record in cur.fetchall():
        print(record)

    conn.commit()

except Exception as e:
    print(e)

finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()