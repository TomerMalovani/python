import pymysql

fav_actors = ["Tim Rose", "Dermot Crowley", "Kendra Wall"]

conention = pymysql.connect(host="localhost",
                            user="root",
                            password="root",
                            db="imdb",
                            charset='utf8mb4',
                            cursorclass=pymysql.cursors.DictCursor)

try:
    with conention.cursor() as cursor:
        sql = "select full_name from actors"
        cursor.execute(sql)
        result = cursor.fetchall()
        for i in result:
            for actor in fav_actors:
                if i['full_name'] == actor:
                    print(f"{i['full_name']} is in the list")
except:
    raise Exception
finally:
    conention.close()
