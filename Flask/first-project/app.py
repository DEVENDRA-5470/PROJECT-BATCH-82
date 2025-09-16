from flask import Flask
app=Flask(__name__)
@app.route("/")
def hello():
    return "Hello world From Flask "

@app.route("/home")
def home():
    return "I am home page"

@app.route("/about")
def about():
    return "I am about page"


if __name__=="__main__":
    app.run(debug=True)