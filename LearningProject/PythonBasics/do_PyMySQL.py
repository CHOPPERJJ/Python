#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pymysql
# 打开数据库连接
db = pymysql.connect(host='localhost', user='root', password='123456', db='chopper', port='3306')

# 使用cursor()方法获取操作游标
cur = db.cursor()

# 1.查询操作
# 编写sql 查询语句 user 对应的表名
sql = 'select * from user'
try:
    # 执行sql语句
    cur.execute(sql)
    # 获取查询的所有记录
    result = cur.fetchall()
    print('id', 'name', 'password')

    # 遍历结果
    for row in result:
        id = row[0]
        name = row[1]
        password = row[2]
        print(id, name, password)

except Exception as e:
    raise e
finally:
    db.close()