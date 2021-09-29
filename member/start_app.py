from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/memberlist')
def memberlist():
    # DB 연동
    conn = sqlite3.connect("c:/webdb/webdb.db")
    cur = conn.cursor()
    sql = "SELECT * FROM member"
    cur.execute(sql)
    rs = cur.fetchall()
    # print(rs)
    conn.close()
    return render_template('memberlist.html', rs=rs) # 데이터를 가져올때에만 rs 사용

@app.route('/register', methods = ['GET', 'POST'])
def register():
    if request.method == 'POST':
        # 웹페이지에서 데이터 가져오기
        id = request.form['memberid']
        pwd = request.form['passwd']
        name = request.form['name']
        age = request.form['age']
        date = request.form['reg_date']

        # DB 연동
        conn = sqlite3.connect("c:/webdb/webdb.db")
        cur = conn.cursor()
        sql = "INSERT INTO member VALUES ('%s', '%s', '%s', '%s', '%s')" % (id, pwd, name, age, date) # 웹에서는 ? 사용 X
        cur.execute(sql)
        conn.commit()
        conn.close()
        return redirect(url_for('memberlist')) # 강제로 주소(페이지) 이동
        # url_for에는 html(확장자) 생략
    else:
        return render_template('register.html')

app.run()