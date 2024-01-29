import sqlite3

def create_connection(db_file):
    """ Create a database connection to the SQLite database specified by db_file """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

def insert_interaction(conn, matriculation_number, user_question, gpt_answer):
    """ Insert a new interaction into the user_interactions table """
    sql = ''' INSERT INTO user_interactions(matriculation_number, user_question, gpt_answer)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, (matriculation_number, user_question, gpt_answer))
    conn.commit()
    return cur.lastrowid

database = "app.db"
matriculation_number = '123456'
conn = create_connection(database)
insert_interaction(conn, matriculation_number, 'prova', 'reply')
conn.close()
