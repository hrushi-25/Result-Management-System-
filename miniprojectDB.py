import mysql.connector

conn=mysql.connector.connect(host='localhost',username='root',password='12345',database='result_management')
my_cursor=conn.cursor()

conn.commit()
conn.close()


print('connection succeesufully created')