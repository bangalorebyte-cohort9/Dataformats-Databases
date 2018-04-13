import sqlite3

conn = sqlite3.connect('example.db')

c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS stocks
             (date text, trans text, symbol text, qty real, price real)''')

c.execute("INSERT INTO stocks VALUES ('2006-01-11','BUY','RHAT',20,31.09)")
c.execute("INSERT INTO stocks VALUES ('2006-01-11','BUY','RGAT',20,31.09)")

conn.commit()

c.execute("SELECT * FROM stocks")
row = c.fetchall()
print(row)
conn.commit()
print("0000000000000000000000000000000000")
c.execute("DELETE FROM stocks WHERE symbol='RHAT'")
conn.commit()

c.execute("SELECT * FROM stocks")
row = c.fetchall()
print(row)
conn.commit()