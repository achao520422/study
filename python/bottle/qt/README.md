# 1. python 连接数据库
数据库依赖 mysql-connector-python

```python
import mysql.connector
conn = mysql.connetor.connect(
    host='0.0.0.0', # 数据库地址
    port=3306,  # 端口
    database='database',    #数据库
    user='user',    #用户
    password='password' #密码
)
cursor = conn.cursor    #获取操作游标

cursor.execute('select * from table')   # 构建操作指令
cursor.fetchall()   #如果是查询，拉取查询结果
conn.commit() # 如果是插入，更新，删除等操作
```