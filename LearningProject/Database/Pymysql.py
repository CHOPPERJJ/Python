import pymysql.cursors

# 连接数据库
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='123456',
                             db='chopper',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        # 创建一个新数据
        sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"

        cursor.execute(sql, ('webmaster@python.org', 'very-secret'))

        # 连接默认不是自动提交，因此必须手动保存
        # 你的更改
    connection.commit()

    with connection.cursor() as cursor:
        # 读取数据记录
        sql = "SELECT `id`, `password` FROM `users` WHERE `email` = %s"
        cursor.execute(sql, ('webmaster@python.org',))
        result = cursor.fetchone()
        print(result)
finally:
    connection.close()





# # 打开数据库连接
# db = pymysql.connect(host='localhost',
#                      user='root',
#                      password='123456',
#                      db='chopper',
#                      port='3306')
#
# # 使用cursor()获取操作游标
# # 1.查询操作
# # 编写sql,查询语句 user 对应我的表名
# sql='SELECT * FROM USER'
# try:
#     cur.execute(sql)     #执行sql语句
#
#     result = cur.fetchall()     #获取查询的所有记录
#     print('id', 'username', 'password')
#     # 便利结果
#     for now in result:
#         id = row[0]
#         username = row[1]
#         password = row[2]
#         print(id, username, password)
#
# except Exception as e:
#     raise e
# finally:
#     db.close()    #关闭连接