import mysql.connector

conn = mysql.connector.connect(
    host="your-host",
    user="your-username",
    password="your-password",
    database="your-database"
)

cursor = conn.cursor()
cursor.execute("SHOW TABLES")
for table in cursor:
    print(table)
conn.close()
