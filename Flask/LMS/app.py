from flask import *
from flask_sqlalchemy import SQLAlchemy
from customer.models import *
app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATION']=False

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/sign_up",methods=["GET","POST"])
def customer_reg():
    name=request.form.get('full-name')
    email=request.form.get('email')
    password=request.form.get('password')
    gender=request.form.get('gender')
    phone=request.form.get('phone')
    print(name,email,password,gender,phone)
    return render_template("customer_reg.html")

if __name__=="__main__":
    app.run(debug=True)