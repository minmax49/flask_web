from flask import Flask, redirect, url_for, render_template, request
app = Flask(__name__)

@app.route('/<user>')
def hello_name(user):
   return render_template('hello.html', name = user)


@app.route('/form')
def form():
   return render_template('form.html')


@app.route('/bootstrap')
def bootstrap():
   return render_template('bootstrap.html')


@app.route("/login", methods=["POST", "GET"])
def login():
    user_dict = {'minh':'1234', 'ngoc':'2345'}

    if request.method == "POST":
        user = request.form["username"]
        password = request.form["password"]

        if (user, password) in user_dict.items():
            return redirect(url_for("user", usr=user))
	    #if (user, password) in user_dict.items():

    else:
    	return render_template("login.html")

@app.route('/')
def index():
    return render_template("hello.html", name="Testing", x=4)


@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"

@app.route('/SomeFunction')
def SomeFunction():
    print('In SomeFunction')
    return "Nothing"


if __name__ == '__main__':
   app.run(debug=True)


