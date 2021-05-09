import psycopg2

conn = psycopg2.connect(dbname="psycopg2_example", user="myuser", password="password", host="127.0.0.1")

cursor = conn.cursor()

# Open a cursor to perform database operations
cur = conn.cursor()

# drop any existing todos table
cur.execute("DROP TABLE IF EXISTS example2;")

# (re)create the todos table
# (note: triple quotes allow multiline text in python)
cur.execute("""
  CREATE TABLE example2 (
    id serial PRIMARY KEY,
    description VARCHAR NOT NULL,
    isAnimal BOOLEAN NOT NULL DEFAULT False
  );
""")

insert_sql = "INSERT INTO example2 (id, description, isAnimal) VALUES (%(id)s, %(description)s, %(isAnimal)s)"

data = {'id': 1, 'description': 'cat', 'isAnimal': True }

# execute the INSERT statement
cur.execute(insert_sql, data)
            
# commit, so it does the executions on the db and persists in the db
conn.commit()

cur.close()
conn.close()