# ===============================================================================
#         metody statyczne i klasowe !!!!!!!!!!!!!!! klasowe nie działa !!!!!
# ===============================================================================
# class book:
#     def __init__(self):
#         self.name = "hobbi"
#         self.price = 12.13
#         self.author = "piercura"
#     def print_book_info(self):
#         print(self.name)
#         print(self.price)
#         print(self.author)
#     @staticmethod               #<--------------------------------
#     def get_silmarillion():
#         b = book()
#         b.name = "silmarillion"
#         b.author = "j. r. r. tolkien"
#         b.price = 42.50
#         return b
#     @classmethod
#     def cm(cls):
#         print("pozdrowienia z klasy")
#         cls.print_book_info(cls)
#
#
# b1 = book()
# b1.print_book_info()
# book.cm()
# b2 = book.get_silmarillion()
# print(b2)
# ===============================================================================
#             dynamiczne własciwości
# ===============================================================================
# from math import sqrt
# class example:
#     number = 0
#     @property   #<--- pobieranie zmiennej prywatnej
#     def number_squared(self):
#         return self.number ** 2
#     @number_squared.setter #<--- ustawianie zmiennej prywatnej
#     def number_squared(self, new_number):
#         self.number = sqrt(new_number)
#
#
#
# e = example()
# e.number = 2
# print(e.number)
# print(e.number_squared)
# print("--------------")
# e.number_squared = 100
# print(e.number)
# ===============================================================================
#               Iteratory
# ===============================================================================
# class numbers(object):
#     def __iter__(self):
#         self.counter = 0
#         return self
#     def __next__(self):
#         if self.counter >= 5:
#             raise StopIteration
#         self.counter += 1
#         return self.counter
#
# for num in numbers():
#     print(num)
# print("-----------------")
# a = numbers()
# for num in a:
#     print(num)
# ===============================================================================
#               Generatory
# ===============================================================================
# powe = [2 ** i for i in range(0, 8)]  # <--- lista składana
# print(powe)
#
# powa = (2 ** i for i in range(0, 8))  # <--- wyrażenie generatorowe
# for i in powa:
#     print(i)
#
# jedis = ["obi",
#          "ank",
#          "Qui",
#          "Yo",
#          "Lu", ]
#
#
# def jedi_generator(a):
#     for person in a:
#         yield person
#
#
# for jed in jedi_generator(jedis):
#     print(jed.title())
#
# gen = jedi_generator(jedis)
# print("Pierwsze")
# for jedi in gen:
#     print(jedi)
#
# # gen = jedi_generator(jedis)  #<--- drugi raz generujemy
# print("Drugie")
# for jedi in gen:
#     print(jedi)
# ===============================================================================
#               Wyrażenia reguralne
# ===============================================================================
#/todo ?
