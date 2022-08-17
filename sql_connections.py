import mysql.connector

customers_db = mysql.connector.connect(user="server",
                                       password="gcp-server-mysql",
                                       host="34.131.201.218",
                                       database="students")
cursor = customers_db.cursor()

