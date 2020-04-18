# this file is going to interact with our DB
# we created a DB, we creating server to handle requests, now we a way for server to interact with DB
# we are going to use a thin layer of functions that our server is going to use to add/remove from DB
# when we get this file, it will allow server to interact with DB

import sqlite3 as sql
from os import path

# this is basically saying: get directory name, then direct path to whatever file we pass in sa the file for this function
ROOT = path.dirname(path.relpath((__file__)))

def user_exists(user_name, user_password):
    # create connection to DB
    con = sql.connect(path.join(ROOT, 'classme.DB')) # we just created connection to DB

    # in order to effiently traverse DB and find info we need, we need to use cursor
    # cursor, instead of gradding whole database, it goes to what we need and makes it more efficient
    # define cursor
    cur = con.cursor() # this is variable that represents thing object is going to move over to DB and find info we need
    # execute raw SQL syntex
    sql_match_login = 'SELECT user_name, password FROM login WHERE user_name = ? AND password = ?'
    cur.execute(sql_match_login, (user_name, user_password))
    # login_result = cur.fetchall()
    return cur.rowcount > 0
     




