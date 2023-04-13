a = input("Introduceti o valoare ")
try:
    print(int(a)) # arunca eroare
    print(var)
except ValueError:
    print("Am avut eroare")
    a = input("Introduceti o valoare ")
except NameError:
    var = None
except Exception as e:
    print(e)
finally:
    print("Nu conteaza daca a fost prinsa in exceptie ", var)
