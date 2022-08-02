from flask import Flask, render_template, request
import sqlite3
d = 'Xəta Baş Verdi!'  
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/add')
def add():
    p_info = request.args.get('p_info')
    p_name = request.args.get('p_name')
    conn = sqlite3.connect('packagez.db')   
    if p_name != "" and p_info != "":
        query = f"insert into packages(name,information) values('{p_name}','{p_info}')"
        conn.execute(query)
        conn.commit()
        return render_template('index.html')
    return render_template('index.html',d=d)
@app.route('/result')
def result():
    conn = sqlite3.connect('packagez.db')
    query = f"Select * from Packages"
    d=conn.execute(query)
    conn.commit()
    d=d.fetchall()
    return render_template('/index.html',d=d)
@app.route('/python')
def rest():
    conn = sqlite3.connect('packagez.db')
    query = f"Select * from Packages where name = 'sql'"
    d=conn.execute(query)
    conn.commit()
    d=d.fetchall()
    return render_template('/index.html',d=d)
@app.route('/Python(advanced)')
def resut():
    conn = sqlite3.connect('packagez.db')
    query = f"Select * from Packages where name = 'Python(inter)'"
    d=conn.execute(query)
    conn.commit()
    d=d.fetchall()
    return render_template('/index.html',d=d)
@app.route('/sql')
def derrr():
    conn = sqlite3.connect('packagez.db')
    query = f"Select * from Packages where name = 'SQL'"
    d=conn.execute(query)
    conn.commit()
    d=d.fetchall()
    if d==[]:
        d='Hər Hansısa Dərs Əlavə Edilməyib'
        return render_template('index.html',d=d)
    else:
        return render_template('/index.html',d=d)
@app.route('/flask')
def resscdut():
    conn = sqlite3.connect('packagez.db')
    query = f"select * from packages where name='Flask '"
    d=conn.execute(query)
    conn.commit()
    d=d.fetchall()
    return render_template('/index.html',d=d)
@app.route('/django')
def resudddt():
    conn = sqlite3.connect('packagez.db')
    query = f"Select * from Packages where name = 'django'"
    d=conn.execute(query)
    conn.commit()
    d=d.fetchall()
    if d==[]:
        d='Hər Hansısa Dərs Əlavə Edilməyib'
        return render_template('index.html',d=d)
    else:
        return render_template('/index.html',d=d)
if __name__ == '__main__':
    app.run(debug=True)