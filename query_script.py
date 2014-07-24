import MySQLdb

conn = MySQLdb.connect("mysql.server", "FlappyBirds", "Admin2", "FlappyBirds$FlappyDB")

c = conn.cursor()

with open("flappysql.sql") as f:
    for q in f:
	    c.execute(q)
	    conn.commit()


rows = c.fetchall()

for row in rows:
	print row

