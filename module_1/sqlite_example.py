# Step 0 - import sqlite3
import sqlite3
import queries as q

# Step 1 - connect to the database
# triple-check spelling of database
connection = sqlite3.connect("rpg_db.sqlite3")

# Step 2 - make cursor
cursor = connection.cursor()

# Step 3 - Write a query
# See queries.py

# Step 4 - Execute the query on the cursor and fetch the results
results = cursor.execute(q.SELECT_ALL).fetchall()

if __name__ == "__main__":
    print(results[:5])
