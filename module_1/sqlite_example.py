import sqlite3
import queries as q

# DB Connect function
def connect_to_db(db_name="rpg_db.sqlite3"):
    return sqlite3.connect(db_name)

# Execute Query function
def execute_q(conn, query):
    # Make the cursor
    curs = conn.cursor()
    #Execute the query
    curs.execute(query)
    # Pull and return the results
    return curs.fetchall()

if __name__ == "__main__":
    conn = connect_to_db()
    print(execute_q(conn, q.SELECT_ALL)[:5])
