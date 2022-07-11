import os
import pymysql

ip = [a for a in os.popen('route print').readlines() if ' 0.0.0.0 ' in a][0].split()[-2]
print(ip)

if __name__ == '__main__':
    # 1.创建与数据库连接对象
    db = pymysql.connect(host="127.0.0.1", user="root", password="00000000",
                         database="insect", charset="utf8")

    # 2.利用db方法创建游标对象
    cur = db.cursor()

    # 3.利用游标对象execute()方法执行SQL命令
    cur.execute('select * from information;')
    res = cur.fetchall()

    # 4.提交到数据库执行
    db.commit()
    print(res[10][5])

    # 5.关闭游标对象
    cur.close()

    # 6.断开数据库连接
    db.close()
