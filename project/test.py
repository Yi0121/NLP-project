import mysql.connector
db = mysql.connector.connect(
    host = "localhost",
    user = "DBuser",
    password = "1234",
    database = "world"
)
print("連線成功")
