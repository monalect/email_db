import sqlite3
con = sqlite3.connect('email.db')
cur = con.cursor().execute("CREATE TABLE IF NOT EXISTS email (emails text not null unique)")
con.commit()
con.close()
