# add information about server
from flask import Flask, render_template, request
    # render_template: this is going to be for displaying the HTML we want to display on screen
    # request: to grab the information that is going to be the content off the resquest that is coming in

# create server object
app = Flask(__name__)

# create the route
    # when you have server, you can have different routes that you can hit (endpoint routes, synonymous)
        # they are unique endpoints, which tell server and server uses to decide which data to send to the view/user back
# this is route for login page
# when you send any information on the internet, we use things called methods
# ex: when you make request to any webpage on internet, that is get request -> get information back for page
@app.route('/login', methods=['GET', 'LOGIN'])
# create that is going to execute when we hit this endpoint
def index():
    if request.method == 'GET':
        pass
    # we want to grab content (via input fields on GUI)
    if request.method == 'LOGIN':
        user_name = request.form.get('username')
        user_password = request.form.get('password')
        login_user(user_name, user_password)

    login_result = login_user(user_name, user_password)

    # return the template the we want user to see (b/c they are requesting to see webpage)
    return render_template('login.html')