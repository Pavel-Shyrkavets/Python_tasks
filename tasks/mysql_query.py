import mysql.connector

database = mysql.connector.connect(
    host = "host",
    user = "user",
    password = "password",
    database = "database"
)
cursor = database.cursor()
cursor.execute("SELECT * FROM Customers LIMIT 5 OFFSET 2;")
result = cursor.fetchall()

for row in result:
    print(row)
