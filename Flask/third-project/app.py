from flask import *
from db import get_connection,init_db,DB_NAME
app=Flask(__name__)
init_db()
@app.route("/",methods=['GET','POST'])
def stu_reg():
    if request.method=="POST":
        full_name=request.form.get('full-name')
        email=request.form.get('email')
        password=request.form.get('password')
        
        conn=get_connection(DB_NAME)
        try:
            with conn.cursor() as cursor:
                    query='''INSERT INTO STUDENTS (SFULL_NAME,SEMAIL,SPASS) VALUES(%s,%s,%s)'''
                    values=(full_name,email,password)
                    cursor.execute(query,values)
                    conn.commit()
                    return redirect(url_for('get_all_stu'))
        except Exception as e:
             print("Error :",e)
        finally:
             conn.close()
        return render_template("stu_reg.html")
    
    else:
        
        return render_template("stu_reg.html")
    

@app.route("/get-stu")
def get_all_stu():
    user=[]
    conn=get_connection(DB_NAME)
    try:
        with conn.cursor() as cursor:
                query='''SELECT * FROM STUDENTS'''
                cursor.execute(query)
                for i in cursor.fetchall():
                      user.append(i)
                
    except Exception as e:
             print("Error :",e)
    finally:
            conn.close()
    return render_template("all_stu.html",users=user)


# Delete data

@app.route('/delete/<int:id>')
def delete_stu(id):
    print(id)
    try:
        conn=get_connection(DB_NAME)
        cur=conn.cursor()
        query=f"DELETE FROM STUDENTS WHERE SID={id}"
        cur.execute(query)
        conn.commit()
        return redirect(url_for('get_all_stu'))
    except Exception as e:
         print(e)
    return f"Data not deleted"
      

     

app.run(debug=True)