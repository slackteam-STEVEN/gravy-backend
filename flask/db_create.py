import sqlite3

# EC.dbを作成する
# すでに存在していれば、それにアスセスする。
dbname = "EC.db"
conn = sqlite3.connect(dbname)

# sqliteを操作するカーソルオブジェクトを作成
cur = conn.cursor()

# customerというtableを作成してみる
# 大文字部はSQL文。
cur.execute(
    "CREATE TABLE customer(id INTEGER PRIMARY KEY AUTOINCREMENT, family_name STRING, first_name STRING, sex STRING)"
)
#実行
conn.commit()

# データベースへのコネクションを閉じる。(必須)
conn.close()


