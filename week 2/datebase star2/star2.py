import pymysql

actors = [{"full_name": "dvir rabbani", "id": 207418963, "gender": "m"},
          {"full_name": "ben abu", "id": 247047047, "gender": "m"},
          {"full_name": "Tomer Malovani", "id": 301245896, "gender": "m"},
          {'id': 15921, 'full_name': 'Guillaume Aretos', 'gender': 'M'},
          {'id': 12508, 'full_name': 'David Andrews', 'gender': 'M'},
          ]

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="root",
    db="imdb",
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

try:
    with connection.cursor() as cursor:
        sql = "select * from actors"
        cursor.execute(sql)
        result = cursor.fetchall()
        for currnet_actor in result:
            for actor in actors:
                if actor["id"] == currnet_actor["id"]:
                    print(".")
                else:
                    sql = "INSERT INTO actors(id,full_name,gender) VALUES ('{}','{}','{}')".format(
                        actor["id"], actor["full_name"], actor["gender"])
                    cursor.execute(sql)
                    connection.commit()

                    print(f"{actor['full_name']} was insert")

except:
    raise Exception
finally:
    connection.close()
