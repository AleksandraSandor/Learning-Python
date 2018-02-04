#--------------------------------------------------------------------------------------
#-------------------- IF warunek ELIF warunek ELSE:------------------------------------
#--------------------------------------------------------------------------------------
if 1 > 2:
    print("blok kodu jesli warunek spełniony") 
elif 1 < 2:
    print("blok kodu jesli spełniony 2 warunek") 
elif 2 < 3:
    pass
elif 3 < 4:
    pass   #jesli nie chce wykonywac żadnego bloku instrukji
else:
    print("blok kodu jeśli inne nie spełnione")
#--------------------------------------------------------------------------------------
#-------------------- FOR zmienna IN zmienna,zakres:----------WHILE warunek:-----------
#--------------------------------------------------------------------------------------
heros = ["a", 2, "44", "ssdf"]
 
for pozycje in heros:  # pozycje otrzymuje kolejno pozycje z tablicy
    print(pozycje)
     
i = 0
while i < len(heros):
    print("test z ,", heros[i]) # robi spacje
    print("test z +" + str(heros[i])) # nie robi spacji, str dlatego ze element [1] jest int'em
    i += 1
     
print(len(heros))   #długosc tablicy, ilośc elementów tablicy
print(len(heros[2]))#długość strigna w tablicy
 
print(type(heros))  #zwrca typ zmiennej
print(type(heros[0]), type(heros[1])) #zwraca typ zmiennej w liscie
#--------------------------------------------------------------------------------------
#-------------------- FUNKCJE ! -----DEF func(zmienna1,zmienna2...):-------------------
#--------------------------------------------------------------------------------------
def sum_0(x, y): #funkcja def naza_funk(zmienna1, zmienna2) zmienne przekazywane do funkcji
    z = x + y
    return z    #zmienna zwracana z funkcji jako wartosc funkcji
  
def sum_1(x, y, c = 2): # wartość domysla 
    print("suma z funkcji =\t",x + y + c)
      
      
num1 = 20
num2 = 15
num_suma = sum_0(num1,num2)
print("suma z poza func =\t",num_suma)
  
sum_1(num1, num2, 0)
      
print(sum_0(num1, num2)) # func zwraca konkretną wartość
print(sum_1(1, 2, 0))   # ta funkcjia nie zwraca wartości \
                        #dlatego None, natomiast print wywołuje tą funkcjie dlatego suma z .....
#--------------------------------------------------------------------------------------
#-------------------- FUNKCJE ! -----MAGICZNE PARAMETRY:-------------------------------
#--------------------------------------------------------------------------------------

tee = ["Han", "Luke", "Leia", "Ben", "Chewie"]

def show_tablica(tablica):
    for i in range(len(tablica)):
        print(tablica[i])

def show_ship_passengers(ship, *psngrs):
    print("Ship:", ship)
    for p in psngrs:
        print(p)
        
        
def list_me(**kwargs):
    if kwargs is not None:
        for a in kwargs:
            print(a, "-", kwargs[a])
        
 
 

show_tablica(tee)
print("---------------")
show_ship_passengers("Millenium Falcon", "Han", "Luke", "Leia", "Ben", "Chewie")
print("---------------")
list_me(race = "Wookie", name_web = "Chewbacca", name_next = "Luca")
#--------------------------------------------------------------------------------------
#-------------------- KONIEC-----------------------------------------------------------
#--------------------------------------------------------------------------------------