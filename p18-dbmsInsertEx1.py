import pymysql

try :
    dbConnection = pymysql.connect(host="127.0.0.1", port=3306, user='root', password='1234', db='distinctao', charset='utf8')
except :
    print("DB Connection Error")
else :
    print(dbConnection)
    cursur = dbConnection.cursor() # statement 객체와 같은 역할
    sql = "insert into board (writer, title, content) values (%s, %s, %s)"

    result = cursur.execute(sql, ('peter', '파이썬 DB', "인서트 잘 되는지 Test 중"))

    if result == 1 :
        dbConnection.commit()
    dbConnection.close()