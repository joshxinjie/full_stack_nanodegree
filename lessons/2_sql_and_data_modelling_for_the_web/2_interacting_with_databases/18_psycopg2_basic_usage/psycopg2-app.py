import psycopg2

conn = psycopg2.connect(dbname="psycopg2_example", user="myuser", password="password", host="127.0.0.1")

cursor = conn.cursor()

# Open a cursor to perform database operations
cur = conn.cursor()

# drop any existing todos table
cur.execute("DROP TABLE IF EXISTS example;")

# (re)create the todos table
# (note: triple quotes allow multiline text in python)
cur.execute("""
  CREATE TABLE example (
    id serial PRIMARY KEY,
    description VARCHAR NOT NULL
  );
""")

insert_sql = "INSERT INTO example (id, description) VALUES(%s, %s)"

value_list = [(1, 'cat'), (2, 'dog'), (3, 'pig')]

# execute the INSERT statement
cur.executemany(insert_sql, value_list)
            
# commit, so it does the executions on the db and persists in the db
conn.commit()

cur.close()
conn.close()