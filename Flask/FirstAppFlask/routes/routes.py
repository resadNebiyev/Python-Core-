from flask  import redirect, render_template,request,flash
from run import app
app.secret_key = '_5#y2L"F4Q8z\n\xec]/'
import sqlite3

# @app.route('/',methods=['GET','POST'])
# def index():
#     return render_template('index.html')

@app.route('/contact',methods=['GET','POST'])
def contact():
    if request.method=='POST':
        conn = sqlite3.connect('mydb.db')
        username = request.form.get('u_name')
        usermail = request.form.get('u_email')
        usermessage = request.form.get('u_message')   
        query = f"insert into User(username,usermail,message) values('{username}','{usermail}','{usermessage}')"
        conn.execute(query)
        conn.commit()
        return render_template('index.html') 
    return render_template('index.html')

@app.route('/message')
def message():
    conn = sqlite3.connect('mydb.db')
    query2 =f"select is_active from login where id=1"
    is_active=conn.execute(query2)
    is_active=is_active.fetchall()
    if 1 in is_active[0]:
        query = f"select * from user"
        d=conn.execute(query)
        d=d.fetchall()
        return render_template('message.html',d=d)
    print(is_active)
    return render_template('login.html')

@app.route('/delete/<id>')
def delete(id):
    conn = sqlite3.connect('mydb.db')
    query = f"delete from user where id = {id}"
    conn.execute(query)
    conn.commit()
    return redirect('/message')

@app.route('/update/<id>',methods=['GET','POST'])
def update(id):
    conn = sqlite3.connect('mydb.db')
    if request.method=='POST':
        username = request.form.get('username')
        usermail = request.form.get('usermail')
        usermessage = request.form.get('usermessage')  
        conn.execute("UPDATE user set username=?,usermail =?,message=? WHERE ID=?",[username,usermail,usermessage,id])
        conn.commit()
        print('dogru')
        return redirect('/message')
    return render_template('update.html',x=id)

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=='POST':
        conn = sqlite3.connect('mydb.db')
        username = request.form.get('u_name')
        passward = request.form.get('u_pass')
        u=conn.execute("select username from login where id=1")
        u=u.fetchall()
        p=conn.execute("select passward from login where id=1")
        p=p.fetchall()
        if username in u[0] and passward in p[0]:
            query = f"update login set is_active=1 where id=1"
            conn.execute(query)
            conn.commit()
            return redirect('/message')
        else:
            flash('Istifadəçi Adı və Şifrə Daxil Edilməyib və ya Yanlışdır')
            return render_template("login.html")
    return render_template('login.html')
    
@app.route('/logout')
def logout():
    conn = sqlite3.connect('mydb.db')
    query = f"update login set is_active=0 where id=1"
    conn.execute(query)
    conn.commit()
    return render_template('index.html')
