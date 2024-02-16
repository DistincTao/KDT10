import pymysql

try :
    dbConnection = pymysql.connect(host="127.0.0.1", port=3306, user='root', password='1234', db='distinctao', charset='utf8')
except :
    print("DB Connection Error")
else :
    print(dbConnection)
    cursur = dbConnection.cursor() # statement 객체와 같은 역할
    sql = "select * from member"

    cursur.execute(sql)
    result = cursur.fetchall()

    for row in result :
        print(row[0], end=", ")
        print(row[1], end=", ")
        print(row[2], end=", ")
        print(row[3])

    dbConnection.close()