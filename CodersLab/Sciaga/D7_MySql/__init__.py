# ===============================================================================
#               mysql
# ===============================================================================
from mysql.connector import connect

cnx = connect(user="root", password="1", host="localhost")
cur = cnx.cursor()
# cnx.autocommit = True
# cnx.commit() <--- dużo szybciej bo nie zapisuje co chwile
# cur = cnx.cursor(dictionary=True)


# sql = "create database test_domowy;"
# cur.execute(sql)
# print(cur)

sql = "use test_domowy;"
cur.execute(sql)
print(cur)

# sql = """create table user(
#             user_id int auto_increment,
#             user_name varchar(255),
#             user_email varchar(255) UNIQUE,
#             primary key(user_id));"""
# cur.execute(sql)
# print(cur)

# for i in range(10000, 100000):
#     sql = """insert into user(user_id, user_name, user_email)
#                         VALUES(DEFAULT , "Wojtek", "wojtek@{}op.pl");""".format(i)
#     cur.execute(sql)
#     print(cur)

# last_id = cur.lastrowid #<----------------------------ostatni ID nad kturym pracowaliśmy
# print("Nowy rekord o id %s został dodoany" %last_id)

# sql = "drop database test_domowy"
# cur.execute(sql)
# print(cur)

# cur = cnx.cursor(dictionary=True)
# sql = """SELECT * FROM user;"""
# cur.execute(sql)
# for row in cur:
#     print(row)

# print("Resoult = ", resoult)
# resoult = cur.execute(sql) #<--- /todo !!!!! dlaczego nie działa ?


sql = """select * from user where user_id <= 50 order by user_id;"""
cur.execute(sql)
for row in cur:
    print(row)

# sql = """delete from user where user_id = 50;"""
# cur.execute(sql)
#
# sql ="""insert into user values(50, "testy", "testy")"""
# cur.execute(sql)

# sql ="""alter table user add opis varchar(255)"""
# cur.execute(sql)

# sql ="""alter table user drop column opis;"""
# cur.execute(sql)

sql = """alter table user modify column opis varchar(66);"""
cur.execute(sql)

cnx.commit()
cur.close()
cnx.close()
