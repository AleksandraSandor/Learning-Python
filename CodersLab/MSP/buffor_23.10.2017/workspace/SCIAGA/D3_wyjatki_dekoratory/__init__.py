#===============================================================================
#                 Wyjatki
#===============================================================================
a = "test"
arr = [1,2]
dane_w_tupli = (1, 2, 3, 4, 5)
tupla = (1, 2, 3)
#dane_w_tupli = dane_w_tupli + 1
b = 0
c = 3

try:
    print("test" + "42")                #print("test" + 42)
    print(arr[1])                       #print(arr[3])
    dane_w_tupli = dane_w_tupli + tupla #dane_w_tupli = dane_w_tupli + tupl
    b = int(10)                          #b = int("a")
    if c not in tupla:
        raise KeyError("c nie ma w tupli")
        
except TypeError:
    print("zły typ zmiennej")
except IndexError:
    print("nie ma takiego indexu")
except NameError:
    print("zła nazwa tupli")
except ValueError:
    print("to nie jest liczba")
except KeyError:
    print("zmiennej nie ma w tupli")
except Exception:   # Dowolny błąd
    print("coś zpatroliłeś")
     
#===============================================================================
#             Dekoratory
#===============================================================================
def double_pi_result(fun):
    def wrapping_function():
        doubled_value = fun() * 2 
        return doubled_value   
    return wrapping_function

def triple_pi_result(fun):
    def wrapping_function():
        triple = fun() * 3
        return triple 
    return wrapping_function


@double_pi_result
@triple_pi_result
def get_pi():
    return 3.141592

print(get_pi())







#===============================================================================
#            KONIEC
#===============================================================================