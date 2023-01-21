import sqlite3 as sq

conn = sq.connect('db/user.db', check_same_thread=False)
cursor = conn.cursor()

def db_table_val(user_id: int, username: str, grp: str):
    cursor.execute('INSERT INTO test (user_id, username, grp) VALUES (?, ?, ?)', (user_id, username, grp))
    conn.commit()
def db_table_main(user_id: int, username: str):
    cursor.execute('INSERT INTO test (user_id, username) VALUES (?, ?)', (user_id, username))
    conn.commit()
def db_table_ed(grp: str, user_id: int):
    sqlff = 'UPDATE test SET grp =? where user_id = ?'
    data = (grp, user_id)
    cursor.execute(sqlff, data)
    conn.commit()
def getName(conn, user_id: int):
    c = conn.cursor()
    c.execute("SELECT grp FROM test WHERE user_id = ?", (user_id, ))
    result = c.fetchone()
    if result:
        return result[0]
def getTrue(user_id: int):
    check_id = user_id
    all_id = [x[0] for x in cursor.execute("SELECT user_id FROM test").fetchall()]
    if check_id in all_id:
        return True
    else:
        return False
