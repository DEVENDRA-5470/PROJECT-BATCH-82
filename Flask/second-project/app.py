from flask import Flask,render_template
app=Flask(__name__)

@app.route("/")
def table():
    s=""
    for i in range(1,11):
       s+=f" <li> 2 x {i} = {2*i} </li>"
    return s

@app.route("/home")
def home():
    return render_template("Home.html")

@app.route("/form")
def form():
    return render_template("Form.html")

app.run()
