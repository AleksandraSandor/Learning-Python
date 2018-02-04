# ===============================================================================
#               MySql laczenie relacje
# ===============================================================================
from mysql.connector import connect

cnx = connect(user="root", password="1", host="localhost")
cur = cnx.cursor()

sql = "use test_domowy;"
cur.execute(sql)

# cur = cnx.cursor(dictionary=False)
# sql = """create table customers(customer_id int not null auto_increment,
#         name varchar(255) not null,
#         primary key(customer_id));"""
# cur.execute(sql)
#
# sql = """create table addresses(customer_id int not null,
#         street varchar(255),
#         primary key(customer_id),
#         foreign key(customer_id) references customers(customer_id) on delete cascade);""" #<--------- jeden do jedn
# cur.execute(sql)
#
# sql = """create table orders(order_id int not null auto_increment,
#         customer_id int not null,
#         order_details varchar(255),
#         primary key(order_id),
#         foreign key(customer_id) REFERENCES customers(customer_id));""" #<--------- jeden do wielu
# cur.execute(sql)
# #
# sql = """create table items(item_id int not null auto_increment,
#         description varchar(255),
#         primary key(item_id));"""
# cur.execute(sql)
#
# sql = """create table items_orders(id int auto_increment,
#         item_id int not null,
#         order_id int not null,
#         primary key(id),
#         foreign key(order_id) REFERENCES orders(order_id),  #<--------- dodatkowa tableawiele do wielu
#         FOREIGN KEY(item_id) REFERENCES items(item_id))"""
# cur.execute(sql)
# sql = """insert into items_orders(order_id, item_id) VALUES (1,1), (2,1), (2,2);"""
# cur.execute(sql)



# sql = """insert into customers(name) VALUES ("Januszaaa"), ("Kubaaaa"), ("Wojtekkkk");"""
# cur.execute(sql)
# sql = """insert into addresses(customer_id, street) VALUES (1, "ul. jeden"), (2, "ulica dwa");"""
# cur.execute(sql)
# sql = """insert into orders(customer_id, order_details) VALUES (3, "zam1"), (3, "zam2"), (1, "zam3");"""
# cur.execute(sql)
# sql = """insert into items(description) VALUES ("itm1"), ("itm2"), ("itm3");"""
# cur.execute(sql);

# sql = """select * from customers join  addresses on customers.customer_id=addresses.customer_id
#         where customers.customer_id=2;"""
# cur.execute(sql)
# for row in cur:
#     print(row)

# sql = """select * from customers join  orders on customers.customer_id=orders.customer_id
#         where customers.customer_id=3;"""
# cur.execute(sql)
# for row in cur:
#     print(row)

# sql = """select * from orders join items_orders on orders.order_id=items_orders.order_id;"""
# cur.execute(sql)
# for row in cur:
#     print(row)




# insert into addresses(customer_id, street) values (6,"ul. zaciszna"); #<---6 dopisze adres jeśli jest ID u customers
# delete from customers where customer_id = 6; # <--- skasowało również adres
# ===============================================================================
#               Formatowanie zapytania
# ===============================================================================
a = "user_name"
b = "user_id"
i = 1
ii = 6

sql = """"select {}, {} from user where user_id = %s or user_id = %s""".format(b, a) #/todo dlaczegoto nie działą 1
cur.execute(sql,(i, ii))
for row in cur:
    print(row)




cnx.commit()
cur.close()
cnx.close()
