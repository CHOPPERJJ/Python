import pymysql.cursors

# 连接数据库
connection = pymysql.connect(host='localhost',
                             user='root',
                             passward='123456',
                             db='db',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        # 创建新的记录
        sql = "INSERT INTO 'users' ('email', 'password') VALUES (%s, %s)"
        cursor.execute(sql,('webmaster@python.org', 'very-secret'))

    # 连接默认不是自动提交，因此必须手动保存
    # 你的修改
    connection.commit()

    with connection.cursor() as cursor:
        # 读取一条单独的记录
        sql = "SELECT 'id', 'password' FROM 'users' WHERE 'email' = %s"
        cursor.execute(sql, ('webmaster@python.org', ))
        result = cursor.fetchone()
        print(result)
finally:
    connection.close()
