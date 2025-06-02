import mysql.connector

# 创建连接
conn = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='123456',
    database='pet'
)
# 获取 mysql 操作游标
cursor =conn.cursor()

#构造查询
cursor.execute('select * from user')
# 获取查询结果
results = cursor.fetchall()
print(results)