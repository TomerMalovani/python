
import pymysql

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
        # sql = "alter table actors ADD num_of_movies int"
        # cursor.execute(sql)

        sql_join = "select a.full_name, count(c.movie_id) from actors as a inner join cast as c on c.actor_id = a.id group by actor_id"
        cursor.execute(sql_join)
        result = cursor.fetchall()
        sql = "select * from actors"
        cursor.execute(sql)
        actors = cursor.fetchall()

        for i in range(len(result)):
            cursor.execute(
                "update actors set num_of_movies={} where full_name =  '{}'".format(
                    result[i]["count(c.movie_id)"], result[i]["full_name"]))

        connection.commit()


except:
    raise Exception
finally:
    connection.close()
