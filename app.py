from models import user_exists, get_users_database, get_whole_database, user_registered, get_user_classes, get_user_class_posts, add_post, is_in_class, get_class_name_from_class_id, class_exists, user_join_class, add_class_and_join_user
# add information about server
from flask import Flask, render_template, request, redirect, url_for
from flask_cors import CORS

# create server object
app = Flask(__name__)


CORS(app)

user_logged_in = False
logged_in_user = None
current_class_id = None

def log_out_user():
    global logged_in_user
    global user_logged_in
    global current_class_id
    user_logged_in = False
    logged_in_user = None
    current_class_id = None

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
            # print(15.0)
            # print(logged_in_user)
            # print(user_classes)  
            if len(user_classes) > 0:
                global logged_in_user
                user_class_posts = get_user_class_posts(logged_in_user, user_classes[0][0])
                global current_class_id
                if current_class_id == None:
                    current_class_id = user_classes[0][0]
                else:
                    user_class_posts = get_user_class_posts(logged_in_user, current_class_id)
            else: 
                user_class_posts = []
            current_class_name = get_class_name_from_class_id(current_class_id)
            # print(16.0)
            # print(user_classes)
            # print(user_class_posts) 
            return render_template('home.html', username = logged_in_user, classes = user_classes, currentClass = current_class_name, posts = user_class_posts)
        else: 
            return redirect(url_for('no_access'))
    if request.method == 'POST':
        message = request.form.get('post')
        if message != None:
            print('Add post POST')
            global logged_in_user
            global current_class_id
            print(current_class_id)
            if current_class_id == None:
                return redirect(url_for('home'))
            add_post(logged_in_user, current_class_id, message)
            return redirect(url_for('home'))
        else:
            pass
        searched_class_id = request.form.get('searchClassPosts')
        if searched_class_id != None:
            if (is_in_class(logged_in_user, searched_class_id) == True):
                print(is_in_class(logged_in_user, searched_class_id))
                global current_class_id 
                current_class_id = searched_class_id
                print("current id" + str(current_class_id))
                return redirect(url_for('home'))
            else:
                return redirect(url_for('home'))
        searched_class_id = request.form.get('searchedClassID')
        if searched_class_id != None:
            print('post 1')
            if(class_exists(searched_class_id)):
                print('post 2')
                if(is_in_class(logged_in_user, searched_class_id) == True):
                    print('post 3')
                    return redirect(url_for('home'))
                else:
                    print('post 5')
                    user_join_class(logged_in_user, searched_class_id)
                    print('post 6')
                    return redirect(url_for('home'))
            else:
                print('post 6')
                return redirect(url_for('home'))
        print('LAST            LAST          LAST')
        cc_name = request.form.get('createdClassName')
        cc_section = request.form.get('createClassSection')
        cc_year = request.form.get('createdClassYear')
        cc_semester = request.form.get('createdClassSemester')
        try:
            test = int(cc_year)
        except:
            return redirect(url_for('home'))
        cc_year = int(cc_year)
        print('LAST 2       LSAT     2       LAST 2')
        print(cc_name)
        print(cc_section)
        print(cc_year)
        print(cc_semester)
        if (cc_name != None) and (cc_section != None) and (cc_year != None) and (cc_semester != None):
            print('last            last       last')
            add_class_and_join_user(logged_in_user, cc_name, cc_section, cc_year, cc_semester)
        print('finish last')
        return redirect(url_for('home'))
        # if len(searched_class) > 0:
        #     if is_search_class() == True:
        #         print(searched_class)
        #         global current_class_id 
        #         current_class_id = get_class_id_from_class_name(searched_class)
        #         return redirect(url_for('home'))
        # else:
        #     pass
        

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