# def decorator_depozit(functia_noastra):
#     def ambalaj_metoda(carti):
#         return f"Ambalam produse din {functia_noastra.__name__} care contine {carti}"
#     return ambalaj_metoda
#
# @decorator_depozit
# def impachetare(nume):
#     return nume
#
# print(impachetare("Baltagul"))

# def decorator_depozit(material):
#    def ambalaj(functia_noastra):
#        def ambalaj_intern(*carte):
#            return f"Ambalam produse din {functia_noastra.__name__} cu {material} care contine {', '.join(x for x in carte)}"
#        return ambalaj_intern
#    return ambalaj
#
# @decorator_depozit("hartie")
# def impachetare_carti(*nume):
#     return nume
#
# print(impachetare_carti("baltagul","amintiri"))
import time


def calculeaza_timpul(functia):
    def functia_interioara(parametru):
        inceput = time.time()
        suma=functia(parametru)
        sfarsit=time.time()
        print(f"Timp total de executie :{sfarsit-inceput}")
        return suma
    return functia_interioara

@calculeaza_timpul
def adunare(number):
    suma=0
    for i in range(number):
        suma+=i
    return suma

print(adunare(10000))