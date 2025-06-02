import this

import mysql.connector


class DataConnect:
    def __init__(self, host='127.0.0.1', user='root', passwd='123456', database='pet'):
        # 数据库 连接
        self.conn = mysql.connector.connect(host=host, user=user, passwd=passwd, database=database)
        # 获取操作游标
        self.cursor = self.conn.cursor()
    def selectData(self, query,val=(),size=0):
        self.cursor.execute(query,val)
        if size == 0:
           return self.cursor.fetchall()
        if size == 1:
            return self.cursor.fetchone()
        else:
            return self.cursor.fetchmany(size)

    def commitData(self):
        self.conn.commit()

    def addData(self, query,val=()):
        self.cursor.execute(query,val)
        self.conn.commit()


    def deleteData(self, query,val=()):
        self.cursor.execute(query,val)
        self.conn.commit()


    def updateData(self, query,val=()):
        self.cursor.execute(query,val)
        self.conn.commit()
    def queryData(self, query,val=(),size=0):
        if 'select' in query:
            raise Exception('查询操作请使用 selectData')
        self.cursor.execute(query,val)
        self.conn.commit()
if __name__ == '__main__':
    db = DataConnect()
    print(db.selectData('select * from user'))
    # 添加
    # db.addData('insert into user(user_id,password,role) values (%s,%s,%s)',(1456,'sdfsdf','OWNER'))
    # 删除
    # db.deleteData('delete from user where user_id=%s',(1456,))
    # 更新
    # db.updateData('update user set username=%s where user_id=%s',('ac',465465))
    # 抛异常
    db.queryData('select * from user')