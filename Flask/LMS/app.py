from flask import *
from flask_sqlalchemy import SQLAlchemy
from customer.models import *
from send_mail import *

app=Flask(__name__)
app.secret_key="this_is_secret_key"

app.config['SQLALCHEMY_DATABASE_URI']='mysql://flask_new_user:flask_123@localhost/my_flask_db'
app.config['SQLALCHEMY_TRACK_MODIFICATION']=False

db.init_app(app)

with app.app_context():
    db.create_all()

def load_template(filename,**kwargs):
    with open(filename,"r",encoding="utf-8") as f:
        template=f.read()
    return template.format(**kwargs)


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/sign_up",methods=["GET","POST"])
def customer_reg():
    # 1.Get data from html form
    if request.method=="POST":
        name=request.form.get('full-name')
        email=request.form.get('email')
        password=request.form.get('password')
        gender=request.form.get('gender')
        phone=request.form.get('phone')

        exists=Customer.query.filter_by(email=email).first()
        if exists:
            flash("This email already exists.","error")
            return render_template("customer_reg.html")
        
        exists=Customer.query.filter_by(phone=phone).first()
        if exists:
            flash("This phone already exists.","error")
            return render_template("customer/customer_reg.html")
        
        try:
            new_customer=Customer(email=email,password=password,name=name,gender=gender,phone=phone)
            db.session.add(new_customer)
            db.session.commit()
            subject=load_template("subject.txt")
            body=load_template("body.txt",username=name,email=email,phone=phone)
            send_mail([email],subject,body)

            return redirect(url_for('all_customer'))
        
           
        except Exception as e:
            return f"Error : {e}"
    else:
        return render_template("customer/customer_reg.html")
    

@app.route("/all-customer")
def all_customer():
    data=Customer.query.all()
    return render_template("customer/all-customer.html",users=data)


@app.route("/delete-customer/<int:id>")
def delete_customer(id):
    data=Customer.query.get(id)
    db.session.delete(data)
    db.session.commit()
    return redirect(url_for('all_customer'))

@app.route("/delete-all")
def delete_customer_all():
    Customer.query.delete()
    db.session.commit()
    return redirect(url_for('all_customer'))

@app.route("/update-customer/<int:id>",methods=["GET","POST"])
def update_customer(id):
    data=Customer.query.get(id)
    if request.method=="POST":
        data.name=request.form.get('full-name')
        data.email=request.form.get('email')
        data.password=request.form.get('password')
        data.gender=request.form.get('gender')
        data.phone=request.form.get('phone')
        db.session.commit()
        return redirect(url_for('all_customer'))
    else:
        return render_template("customer/update-customer.html",data=data)


if __name__=="__main__":
    app.run(debug=True)