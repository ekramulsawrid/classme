from models import user_exists, get_users_database, get_whole_database, user_registered, get_user_classes, get_user_class_posts, get_user_id_from_user_name
# add information about server
from flask import Flask, render_template, request, redirect, url_for
from flask_cors import CORS

# create server object
app = Flask(__name__)


CORS(app)

logged_in_user = None
user_logged_in = False

def log_out_user():
    global logged_in_user
    global user_logged_in
    user_logged_in = False
    logged_in_user = None

def print_user():
    print(str(logged_in_user)  + " " + str(user_logged_in))

@app.route('/')
def welcome():
    log_out_user()
    print_user()
    return render_template('index.html')

@app.route('/index', methods = ['GET'])
def classme():
    log_out_user()
    return render_template('index.html')

@app.route('/register', methods = ['GET', 'POST'])
def register():
    if request.method == 'GET':
        log_out_user()
        return render_template('register.html')
    if request.method == 'POST':
        user_first_name = request.form.get('firstname')
        user_last_name = request.form.get('lastname')
        user_name = request.form.get('username')
        user_email = request.form.get('email')
        user_password = request.form.get('password')
        if user_registered(user_first_name, user_last_name, user_name, user_email, user_password) == True:
            #return redirect(url_for('register_success'))
            return render_template('register.html', result = 'Register Successful!')
        else:
            #return redirect(url_for('register_failed'))
            return render_template('register.html', result = 'Register Failed.')

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'GET':
        log_out_user()
        return render_template('login.html')
    if request.method == 'POST':
        user_name = request.form.get('username')
        user_password = request.form.get('password')
        user_exists_res = user_exists(user_name, user_password)
        if user_exists_res == True:
            #return render_template('login.html', result = 'Login Success')
            global logged_in_user 
            logged_in_user = user_name
            global user_logged_in 
            user_logged_in = True
            return redirect(url_for('home'))
        else:
            return render_template('login_failed.html', result = 'Login Failed')

@app.route('/home', methods = ['GET', 'POST'])
def home():
    if request.method == 'GET':
        print_user()
        if user_logged_in == True:
            global logged_in_user
            user_classes = get_user_classes(logged_in_user)    
            if len(user_classes) > 0:
                user_class_posts = get_user_class_posts(user_logged_in, user_classes[0][0])
            else: user_class_posts = []  
            return render_template('home.html', username = logged_in_user, classes = user_classes, posts = user_class_posts)
        else: 
            return redirect(url_for('no_access'))

@app.route('/logout', methods=['GET'])
def logout():
    if request.method == 'GET':
        return redirect(url_for('welcome'))

@app.route('/no_access')
def no_access():
    return render_template('no_access.html')



@app.route('/test', methods=['GET', 'POST'])
def test():
    if request.method == 'GET':
        log_out_user()
        return render_template('test.html')
    # if request.method == 'POST':
    #     users = get_users_atabase()
    #     return render_template('test.html', users = users)
    if request.method == 'POST':
        classme_database = get_whole_database()
        return render_template('test.html', DB = classme_database)
    
    

# # create the route
#     # when you have server, you can have different routes that you can hit (endpoint routes, synonymous)
#         # they are unique endpoints, which tell server and server uses to decide which data to send to the view/user back
# # this is route for login page
# # when you send any information on the internet, we use things called methods
# # ex: when you make request to any webpage on internet, that is get request -> get information back for page
# @app.route('/', methods=['GET', 'LOGIN'])
# # create that is going to execute when we hit this endpoint
# def index():
#     if request.method == 'GET':
#         pass
#     # we want to grab content (via input fields on GUI)
#     if request.method == 'LOGIN':
#         user_name = request.form.get('username')
#         user_password = request.form.get('password')
#         # login_user(user_name, user_password)
#         login_result = login_user(user_name, user_password)
#         return redirect(url_for('login_error'))
#         if (login_result == None):
#             return redirect(url_for('login_error'))
#         # return render_template('index.html', login_result = login_result)

#     # login_result = login_user(user_name, user_password)
#     # if login_result == None:     # 0
#     #     return 
#     # return the template the we want user to see (b/c they are requesting to see webpage)
#     # return render_template('index.html', login_result = login_result)
#     return render_template('index.html')


# to get our server to run and get going
# these statements saying is if this is the file that selected to run -> execute this
if __name__ == '__main__':
    app.run(debug=True)