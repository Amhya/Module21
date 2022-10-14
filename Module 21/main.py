from flask import *

app=Flask(__name__)

@app.route("/")
def login():
    return render_template("login.html")
@app.route("/login")
def login_():
    return render_template("login.html")
@app.route("/home/<username>")
def home(username):
    return render_template("home.html",user=username)
@app.route("/home")
def home_():
    return render_template("home.html")
@app.route("/gas")
def gas():
    return render_template("gas.html")
@app.route("/liquid")
def liquid():
    return render_template("liquid.html")
@app.route("/solid")
def solid():
    return render_template("solid.html")
@app.route("/plasma")
def plasma():
    return render_template("plasma.html")
@app.route("/process", methods=['POST','GET'])
def process():
    if request.method == 'POST':
        username = request.form['username']
        return redirect(url_for('home', username=username))
    else:
        username = request.args.get('user')
        return redirect(url_for('home', username=username))


if __name__ == '__main__':
    app.run()
