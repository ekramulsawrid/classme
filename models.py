# this file is going to interact with our DB

import sqlite3 as sql
from os import path
 
ROOT = path.dirname(path.relpath((__file__)))

def user_exists(username, password):
    user_id = None
    try:
        user_id = get_user_id_from_user_name(username)
    except:
        False
    con = sql.connect(path.join(ROOT, 'classme.DB')) 
    cur = con.cursor() 
    cur.execute('PRAGMA foreign_keys = ON')
    cur.execute('SELECT user_id, password FROM login WHERE user_id = ? AND password = ?', (user_id, password))
    login_result = cur.fetchall()
    con.close()
    try:
        test = login_result[0][0]
        test = login_result[0][1]
    except:
        return False
    return (str(login_result[0][0]) == str(user_id)) and (str(login_result[0][1]) == str(password))

def user_registered(user_first_name, user_last_name, user_name, user_email, password):
    con = sql.connect(path.join(ROOT, 'classme.DB'))
    cur = con.cursor()
    cur.execute('PRAGMA foreign_keys = ON')
    try:
        cur.execute('INSERT INTO users (first_name, last_name, user_name, email) VALUES (?, ?, ?, ?)',
            (user_first_name, user_last_name, user_name, user_email))
        cur.execute('SELECT user_id FROM users WHERE user_name = ?', (user_name,))
        user_info = cur.fetchall()
        cur.execute('INSERT INTO login VALUES (?, ?)', (user_info[0][0], password))
    except:
        return False    
    con.commit()
    con.close()
    return True


def get_users_database():
    con = sql.connect(path.join(ROOT, 'classme.DB'))
    cur = con.cursor()
    cur.execute('SELECT * FROM users')
    users = cur.fetchall()
    con.close()
    return users

def get_user_id_from_user_name(username):
    print('username')
    print(username)
    con = sql.connect(path.join(ROOT, 'classme.DB'))
    cur = con.cursor()
    cur.execute('PRAGMA foreign_keys = ON')
    cur.execute('SELECT user_id FROM users WHERE user_name = ?', (username,))
    user_id = cur.fetchall()
    con.close()
    print('userid')
    print(user_id)
    print(user_id[0])
    print(user_id[0][0])
    print('userid_finish')
    # print(user_id[0][0])
    return user_id[0][0]

def get_user_first_name(username):
    user_id = get_user_id_from_user_name(username)
    con = sql.connect(path.join(ROOT, 'classme.DB'))
    cur = con.cursor()
    cur.execute('SELECT first_name FROM users WHERE user_id = ?', (user_id,))
    user_first_name = cur.fetchall()
    con.close()
    return user_first_name[0][0]

def get_user_last_name(username):
    user_id = get_user_id_from_user_name(username)
    con = sql.connect(path.join(ROOT, 'classme.DB'))
    cur = con.cursor()
    cur.execute('SELECT last_name FROM users WHERE user_id = ?', (user_id,))
    user_last_name = cur.fetchall()
    con.close()
    return user_last_name[0][0]

def get_user_email(username):
    user_id = get_user_id_from_user_name(username)
    con = sql.connect(path.join(ROOT, 'classme.DB'))
    cur = con.cursor()
    cur.execute('SELECT email FROM users WHERE user_id = ?', (user_id,))
    user_email = cur.fetchall()
    con.close()
    return user_email[0][0]


def get_user_classes(username):
    user_id = get_user_id_from_user_name(username)
    con = sql.connect(path.join(ROOT, 'classme.DB'))
    cur = con.cursor()
    cur.execute('SELECT classes.class_id, classes.class_name, classes.class_section, classes.class_year, classes.class_semester FROM users, classes, ischedule WHERE users.user_id = ischedule.user_id AND classes.class_id = ischedule.class_id and users.user_id = ?;', (user_id,))
    user_classes = cur.fetchall()
    con.close()
    print(user_classes)
    return user_classes



def get_user_class_posts(username, userclassid):
    # print(username)
    # print(userclassid)
    user_id = get_user_id_from_user_name(username)
    con = sql.connect(path.join(ROOT, 'classme.DB'))
    cur = con.cursor()
    cur.execute('SELECT  users.user_name, posts.posted, posts.message FROM users, posts WHERE users.user_id = posts.user_id AND class_id = ?', (userclassid,))
    class_posts = cur.fetchall()
    con.close()
    # print(class_posts)
    return class_posts

def add_post(user, classId, message):
    print('add_post')
    print(user)
    print(classId)
    print(message)
    user_id = get_user_id_from_user_name(user)
    print(user_id)
    con = sql.connect(path.join(ROOT, 'classme.DB'))
    cur = con.cursor()
    cur.execute('INSERT INTO posts (user_id, class_id, message) VALUES (?, ?, ?)', (user_id, classId, message))
    con.commit()
    con.close()
    return

def get_class_name_from_class_id(currentClassId):
    con = sql.connect(path.join(ROOT, 'classme.DB'))
    cur = con.cursor()
    cur.execute('SELECT class_name FROM classes WHERE class_id = ?', (currentClassId,))
    class_name = cur.fetchall()
    con.close()
    # print(user_id[0][0])
    try:
        test = class_name[0][0]
    except:
        return "Are you not in any classes right now."
    return class_name[0][0]

def is_in_class(username, classId):
    user_id = get_user_id_from_user_name(username)
    con = sql.connect(path.join(ROOT, 'classme.DB'))
    cur = con.cursor()
    cur.execute('SELECT * FROM ischedule WHERE user_id = ? AND class_id = ?', (user_id, classId))
    isTrue = cur.fetchall()
    con.close()
    print(isTrue)
    if not isTrue:
        return False
    else:
        return True

def class_exists(classID):
    con = sql.connect(path.join(ROOT, 'classme.DB'))
    cur = con.cursor()
    cur.execute('SELECT * FROM classes WHERE class_id = ?', (classID, ))
    isTrue = cur.fetchall()
    con.close()
    if not isTrue:
        return False
    else:
        return True

def user_join_class(username, classID):
    user_id = get_user_id_from_user_name(username)
    con = sql.connect(path.join(ROOT, 'classme.DB'))
    cur = con.cursor()
    cur.execute('INSERT INTO ischedule (user_id, class_id) VALUES (?, ?)', (user_id, classID))
    con.commit()
    con.close()
    return

def user_leave_class(username, classID):
    user_id = get_user_id_from_user_name(username)
    con = sql.connect(path.join(ROOT, 'classme.DB'))
    cur = con.cursor()
    cur.execute('DELETE FROM ischedule WHERE user_id = ? AND class_id = ?', (user_id, classID))
    con.commit()
    con.close()
    return


def add_class_and_join_user(username, ccName, ccSection, ccYear, ccSemester):
    user_id = get_user_id_from_user_name(username)
    print('Got here')
    con = sql.connect(path.join(ROOT, 'classme.DB'))
    cur = con.cursor()
    cur.execute('PRAGMA foreign_keys = ON')
    # try:
    #     print("add + joing 1")
    #     cur.execute('INSERT INTO classes (class_name, class_section, class_year, class_semester) VALUES (?, ?, ?, ?)', (ccName, ccSection, ccYear, ccSemester))
    #     con.commit()
    #     cur.execute('SELECT class_id FROM classes WHERE class_id = (SELECT MAX(class_id) FROM classes)')
    #     print("add + joing 2")
    # except:
    #     con.close()
    #     return
    
    print("add + joing 1")
    cur.execute('INSERT INTO classes (class_name, class_section, class_year, class_semester) VALUES (?, ?, ?, ?)', (ccName, ccSection, ccYear, ccSemester))
    con.commit()
    cur.execute('SELECT class_id FROM classes WHERE class_id = (SELECT MAX(class_id) FROM classes)')
    print("add + joing 2")

    new_class_id = cur.fetchall()
    con.commit()
    con.close()
    user_join_class(username, new_class_id[0][0])
    return 

def get_whole_database():
    con = sql.connect(path.join(ROOT, 'classme.DB'))
    cur = con.cursor()
    cur.execute('SELECT * FROM users')
    users = cur.fetchall()
    cur.execute('SELECT * FROM classes')
    classes = cur.fetchall()
    cur.execute('SELECT * FROM posts')
    posts = cur.fetchall()
    cur.execute('SELECT * FROM ischedule')
    ischedule = cur.fetchall()
    cur.execute('SELECT * FROM login')
    login = cur.fetchall()
    con.close()
    return users, classes, posts, ischedule, login
     