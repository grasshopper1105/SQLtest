import MySQLdb

path = 'C22345105005 美国白蛾/img240048.jpg'
conn = MySQLdb.connect(host='localhost', port=3306, user='root', passwd='00000000', db='insect', charset='utf8')
print('successfully connect')
cursor = conn.cursor()
fin = open(path, 'rb')  # 'rb'加上才能将图片读取为二进制
img = fin.read()  # 将二进制数据读取到img中
fin.close()

sql = "INSERT INTO image VALUES  (%s,%s);"  # 将数据插入到mysql数据库中，指令
args = ('Hyphantria_cunea_Adult', img)  # 对应表格的数据

cursor.execute(sql, args)  # 执行相关操作
conn.commit()  # 更新数据库
# print(2)
cursor.close()
conn.close()
