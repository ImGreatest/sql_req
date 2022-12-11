import pymysql.cursors

conn = pymysql.connect(host='5.183.188.132', user='db_vgu_student', password='thasrCt3pKYWAYcK', db='db_vgu_test', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

try:
    with conn.cursor() as cur:
        request = "select * from attribute"
        cur.execute(request)
        print('cursor.description: ', cur.description)
        [print(i) for i in cur]

finally:
    conn.close()