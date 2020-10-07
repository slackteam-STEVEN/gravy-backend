import sqlite3

# EC.dbを作成する
# すでに存在していれば、それにアスセスする。
dbname = "EC.db"
conn = sqlite3.connect(dbname)

# sqliteを操作するカーソルオブジェクトを作成
cur = conn.cursor()

#"customerテーブル"に情報を登録する
cur.execute('INSERT INTO customer(family_name, first_name, sex) VALUES ("tama", "cyan", "男")')

#実行
conn.commit()

# データベースへのコネクションを閉じる。(必須)
conn.close()


