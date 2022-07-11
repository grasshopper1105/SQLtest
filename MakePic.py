import base64

import MySQLdb
import sys

import PIL.Image as Image
import cv2

conn = MySQLdb.connect(host='localhost', port=3306, user='root', passwd='00000000', db='insect', charset='utf8')
print('successfully connect')

cursor = conn.cursor()
cursor.execute("SELECT IMG FROM image LIMIT 5")

res = cursor.fetchall()
for i in range(len(res)):
    fout = open('test' + str(i) + '.jpg', 'wb')
    fout.write(res[i][0])
    fout.close()

cursor.close()
conn.close()
