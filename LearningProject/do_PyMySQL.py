#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pymysql

db = pymysql.connect('localhost', 'user', '123456', 'TESTDB')
cursor = db.cursor()
cursor.execute('DROP TABLE IF EXISTS EMPLOYEE')

sql = """CREAT TABLE EMPLOYEE (
         FIRST_NAME CHAR(20) NOT NULL,
         LAST_NAME CHAR(20),
         AGE INT,
         SEX CHAR(1),
         INCOME FLOAT )"""

cursor.execute(sql)

db.close()