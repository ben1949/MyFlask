from flask import Flask
from flask import render_template
from flask import request
from flask import flash
from flask import abort
from models import User
app = Flask(__name__)
app.secret_key = '123'

@app.route('/')
def hello_world():
    print "helloword was called"
    #flash("hello,world")
    return render_template("index.html")

@app.route('/one')
def fone():
    userlist = []
    print "one was called"
    for i in range(10):
        user = User(i,"weihuap"+str(i))
        userlist.append(user)
    return render_template("./one_base.html",users=userlist)

@app.route('/two')
def ftwo():
    userlist = []
    print "one was called"
    for i in range(10,20):
        user = User(i,"weihuap"+str(i))
        userlist.append(user)
    return render_template("./one_base.html",users=userlist)

@app.route('/login',methods=['POST'])
def login():
    print "login was called"
    form = request.form
    username = form.get('username')
    password = form.get('password')
    if not username:
        flash("please input username")
    if not password:
        flash("please input password")

    if username == "weihuap" and password == "123456":
        flash("login success")
        return render_template("index.html")
    else:
        flash("username or password is incorrect")
        return render_template("index.html")

@app.errorhandler(404)
def not_found(e):
    return render_template("error.html")

@app.route('/users/<user_id>')
def users(user_id):
    if int(user_id) == 1:
        return render_template("one_base.html")
    else:
        abort(404)

if __name__ == '__main__':
    app.run()