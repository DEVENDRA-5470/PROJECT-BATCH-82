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

@app.route("/sign_up")
def customer_reg():
    return render_template("customer_reg.html")

if __name__=="__main__":
    app.run(debug=True)