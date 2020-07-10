import psycopg2

conn = psycopg2.connect(database="testdb", user = "postgres", password = "puja1404", host = "127.0.0.1", port = "5432")

print("Opened database successfully")

conn = psycopg2.connect(database = "testdb", user = "postgres", password = "puja1404", host = "127.0.0.1", port = "5432")
print ("Opened database successfully")

cur = conn.cursor()
cur.execute('''CREATE TABLE COMPANY2
      (ID INT PRIMARY KEY     NOT NULL,
      NAME           TEXT    NOT NULL,
      AGE            INT     NOT NULL,
      ADDRESS        CHAR(50),
      SALARY         REAL);''')
print("Table created successfully")

conn.commit()
conn.close()