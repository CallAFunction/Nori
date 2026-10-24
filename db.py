import sqlite3
def link(database="fuckyou.db"):
    global con
    global cur
    con=sqlite3.connect(database)
    cur = con.cursor

def get_values(value="*", table="fuckyou.db"):
    execution = "SELECT {_value} FROM {_table}".format(_value = value, _table = table)
    cur.execute(execution)

link()
get_values()



