lista_op = ['+', '-' , '*', '/' ]
#litere in loc de cifre
#impartire la 0

print("Numarul de operatii dorite este: ")
opernr = int(input())
while opernr:
    operator1 = input("Add first operator: ")
    operator2 = input("Add second operator: ")
    operatie = input("Add operation: ")
    if operatie in lista_op and operator2.isdigit() and operator1.isdigit():
        if operatie == '+' and operator2.isdigit() and operator1.isdigit():
            print(f"Suma celor 2 numere : {operator1} si {operator2} este: ")
            print(int(operator1) + int(operator2))
        if operatie == '*' and operator2.isdigit() and operator1.isdigit():
            print(f"Inmultirea celor 2 numere : {operator1} si {operator2} este:")
            print(int(operator1) * int(operator2))
        if operatie == '-' and operator2.isdigit() and operator1.isdigit():
            print(f"Scaderea celor 2 numere : {operator1} si {operator2} este:")
            print(int(operator1) - int(operator2))
        if operatie == '/' and operator2.isdigit() and operator1.isdigit() and operator2 != 0:
            print(f"Impartirea celor 2 numere : {operator1} si {operator2} este:")
            print(int(operator1) / int(operator2))
        if operator2 == 0 and operatie == '/':
            break
            print("Nu e valid!")
        opernr = opernr - 1
    else:
        print(f"Alege o operatie din lista {','.join(lista_op)}")