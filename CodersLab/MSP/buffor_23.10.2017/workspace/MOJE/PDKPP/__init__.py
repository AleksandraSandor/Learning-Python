#===============================================================================
#         R8.1 Prosty zwierzak
#===============================================================================
class Critter(object):
    """Wirtualny pupil"""
    total = 0
      
    @staticmethod
    def status():
        print("Liczba zwierzaków:", Critter.total)    
      
    def __init__(self, name):
        print("Urodził się nowy zwierzak")
        self.name = name    
        Critter.total += 1
    def __str__(self):
        rep = "Obiekt klasy Critter\n"
        rep += "name: " + self.name + "\n"
        return rep    
    def talk(self):
        print("Cześć ! Jestem ", self.name)
  
          
  
#-------Część główna programu:
  
  
crit = Critter("Maniek")
crit2 = Critter("Paniek")
# crit.talk()
# crit2.talk()
# print(crit)
print(crit)
  
# print(Critter.total)
# print(crit2.total)
# crit2.status()
# Critter.total = 10
# crit2.status()
# Critter.status()
test = input("test")
#===============================================================================
#         R8.2 Prywatny zwierzak
#===============================================================================
# 
# class Critter(object):
#     total = 0
#      
#     @staticmethod
#     def status():
#         print("Aktualnie jest",Critter.total, "zwierzaków")
#          
#     def __init__(self,name,mood = "Angry"):
#         print("Urodził się nowy zwierzak!")
#         self.name = name
#         self.__mood = mood
#         Critter.total += 1
#     def talk(self):
#         print("Jestem", self.name)
#         print("W tej chwili czuje się ", self.__mood)
#         self.__mood = "Happy"
#     def __prywatna(self):
#         print("Metoda prywatna")
#     def metoda(self):
#         print("Metoda publicza")
#         self.__prywatna()
#      
#      
#      
#      
# zwierzak1 = Critter("Staś")
# zwierzak1.metoda()
# zwierzak1._Critter__prywatna()  
# zwierzak1._Critter__mood = "blee"
# zwierzak2 = Critter("Jaś")
# Critter.status()
# zwierzak1.talk()
# zwierzak1.name = "Pierd"
# zwierzak1.talk()
#===============================================================================
#             R8.3 Zwierzak z właściwością 
#===============================================================================
class Critter(object):
    def __init__(self, name):
        print("Urodził się zierzak")
        self.__name = name
         
    @property
    def name(self):
        return self.__name
     
    @name.setter
    def name(self, new_name):
        if new_name == "":
            print("Nie dałeś imienia")
        else:
            self.__name = new_name
            print("Zmieniłes imie")
             
    def talk(self):
        print("Cześć! Jestem", self.name)
         
#GŁÓWNA CZĘŚĆ
zwierz1 = Critter("reks")
zwierz1.talk()
zwierz1.name = "nowe"
zwierz1.talk()
#===============================================================================
#             R.8.Opiekun zwierzaka
#===============================================================================
class Critter(object):
    def __init__(self, name, hunger = 0, boredom = 0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom        
    def __str__(self):
        opis = "opis" + self.name + str(self.hunger + self.boredom)
        return opis 
    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1        
    @property  #<--------------------
    def mood(self):
        unhappines = self.hunger + self.boredom
        if unhappines < 5:
            m = "szczęśliwy"
        elif 5 <= unhappines <= 10:
            m = "zadowolony"
        elif 11 <= unhappines <= 15:
            m = "podenerwowany"
        else:
            m = "wściekły"
        return m
    def talk(self):
        print("Nazywam się ", self.name,"i jestem ", self.mood, "teraz. \n")
        self.__pass_time()
    def eat(self, food = 4):
        print("Mniam mniam, dziękuję :)")
        self.hunger -= food
        if self.hunger <= 0:
            self.hunger = 0
        self.__pass_time()
    def play(self, fun = 4):
        self.boredom -= fun
        if self.boredom <= 0:
            self.boredom = 0
        self.__pass_time()
    
    
def main():
    crit_name = input("Podaj imie dla zwierzaka")
    crit = Critter(crit_name)
    
    choise = None
    while choise != "0":
        print \
        ("""
        Opiekun zwierzaka
        0 - zakończ
        1 - słuchaj 
        2 - nakarm
        3 - powab się ze zwierzakiem
        """)        
        choise = input("Wibierasz:")
        print()
        if choise == "0":
            print("Do widzenia")
        elif choise == "1":
            crit.talk()
        elif choise == "2":
            a = int(input("Ile żarcia:"))
            crit.eat(a)
        elif choise == "3":
            a = int(input("Ile czasu:"))
            crit.play(a)
        elif choise == "4":
            print(crit)
        else:
            print("Coś ty nasicnał ?!")
            
            
main()
        
x = len(a)
        



