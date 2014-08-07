import MySQLdb

conn = MySQLdb.connect("mysql.server", "FlappyBirds", "Admin2", "FlappyBirds$FlappyDB")

c = conn.cursor()

with open("udpate_activities.sql") as f:
    for q in f:
        print(q)
        c.execute(q)
        conn.commit()


rows = c.fetchall()

for row in rows:
	print row

