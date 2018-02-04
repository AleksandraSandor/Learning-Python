#===============================================================================
#                 Klasy
#===============================================================================
# class Auto:
#     name = "Honda"
#     __silnik = "v6"
#     def __init__(self):
#         print("Nowe auto")
#     def print_info(self):
#         print(self.__silnik)
#         print(self)
#     def __str__(self):
#         return("Nazwa auto " + self.name)
# 
# a1 = Auto()
# a2 = Auto()
# print(a1)

# print(a1.name)
# print(a2.name)
# print(a1._Auto__silnik)         
# a1.name = "Audi"
# print(a1.name)
# a1.print_info()
# a1.print_info()
#print(a1)

# __init__()    
# __new__()    
# __str__()    
# __repr__()    
# __unicode__()    
# __eq__()    
# __call__()    
# __del__()    
# __name__()    
# __setattr__()    
# __len__()    
# __add__()    
# __div__()    
# __int__()    
# __get__()    
# __set__()
#===============================================================================
#         Dziedziczenie
#===============================================================================
# class Book:
#     name = "Hobbit"
#     price = 33.33
#     autor = "Ble ble"
#      
# # class Ebook:
# #     name = "Hobbit"
# #     price = 33.33
# #     autor = "Ble ble"
# #     size_in_mg = 12
#      
# class Ebook(Book):
#     size_in_mb = 12    
#     def __str__(self):
#         return(self.name + str(self.price) + self.autor + str(self.size_in_mb))
#      
# #print("-----------------------------")
# a = Ebook()
# print(a)
# #print(a.name)
#===============================================================================
#         Dziedziczenie z super
#===============================================================================
# class Book(object):
# #     name = None
# #     price = None
# #     author = None
#     def __init__(self, n, p, a):
#         print("Tworzę nowa książkę")
#         self.name = n
#         self.price = p
#         self.author = a
#     def __repr__(self):
#         return "{} by {} for {}".format(self.name, self.price, self.author)
#      
# class EBook(Book):
#     size_in_mb = None
#     def __init__(self, n, p, a, s):
#         print("Tworzę nowego EBooka")
#         super(EBook,self).__init__(n, p, a)
#         self.size_in_mb = s
#      
#      
# a1 = Book("test", 12.12, "test1")
# print(a1)
# a2 = EBook("test", 13.12, "test1", 12)
# print(a2)
#===============================================================================
#         Nadpisywanie metod 
#===============================================================================
class Book:
    def __init__(self):
        self.name = "hobbi"
        self.price = 12.13
        self.author = "piercura"
    def print_book_info(self):
        print(self.name)
        print(self.price)
        print(self.author)
          
          
class EBook(Book):
    def __init__(self):
        super(EBook,self).__init__()
        self.size_in_mb = 44
    def print_book_info(self):
        super(EBook,self).print_book_info()
        print(self.size_in_mb)
      
          
a1 = Book()
a1.print_book_info()
print("--------")
a2 = EBook()
a2.print_book_info()
print("-----------")
a1.print_book_info()


