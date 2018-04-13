import sqlite3

connection = sqlite3.connect("testing.db")

cur = connection.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS new_users(id NUMBER, name VARCHAR(50), phone NUMBER)")

cur.execute("INSERT INTO new_users VALUES (9, 'Hansel', 9072)")
print("Inserted!!")
connection.commit()

u = int(input("Entert ID :"))
n = input("Entert Name :")
p = int(input("Enter Phone : "))
cur.execute("INSERT INTO new_users(id, name, phone) VALUES (?, ?, ?)", [u, n, p])
print("Inserted again!!")
connection.commit()

cur.execute("INSERT INTO new_users(id, name, phone) VALUES ({}, '{}', {})".format(u, n, p))
print("Inserted again!!")
connection.commit()

cur.execute("UPDATE new_users SET name='Bush' WHERE name='Pratheekshith'")
connection.commit()

cur.execute("DELETE FROM new_users WHERE name='Hansel'")
connection.commit()

cur.execute("SELECT * FROM new_users ORDER BY name DESC;")
row = cur.fetchall()
for r in row:
	print("ID - ", r[0])
	print("Name - ", r[1])
	print("Phone - ", r[2])

# print(row)