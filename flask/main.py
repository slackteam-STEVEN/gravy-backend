from flask import Flask
from flask import request


app = Flask(__name__)

@app.route("/")
def top():
    return render_template("top.html")

@app.route("/profile", methods=["POST"])
def profile():

    family_name = request.form["family_name"]
    first_name = request.form["first_name"]
    sex = request.form["sex"]

    if sex == "man":
        sex = "男"
    elif sex == "woman":
        sex = "女"

    # EC.dbを作成する
    # すでに存在していれば、それにアスセスする。
    dbname = "EC.db"
    conn = sqlite3.connect(dbname)

    # sqliteを操作するカーソルオブジェクトを作成
    cur = conn.cursor()

    #"customerテーブル"に情報を登録する
    cur.execute(f'INSERT INTO customer(family_name, first_name, sex) VALUES ("{family_name}", "{first_name}", "{sex}")')

    #実行
    conn.commit()

    # データベースへのコネクションを閉じる。(必須)
    conn.close()

    return render_template("profile.html",family_name=family_name,first_name=first_name,sex=sex)

@app.route("/show", methods=["POST"])
def show():
    customer_id = request.form["customer_id"]


    customer_id = int(customer_id)

    dbname = "EC.db"
    conn = sqlite3.connect(dbname)

    # sqliteを操作するカーソルオブジェクトを作成
    cur = conn.cursor()

    #"customerテーブル"に情報を登録する
    cur.execute(f'SELECT * FROM customer WHERE id={customer_id}')
  
    customer_info = cur.fetchone()
    # データベースへのコネクションを閉じる。(必須)
    conn.close()

    return render_template("/show.html", customer_info=customer_info)

    # メイン関数
    # メイン関数とは、Pythonを実行した際、最初に呼ばれる関数
if __name__ == "__main__":
    app.run(debug=True)