class Catalog:
    def __init__(self,nume,prenume):
        self.nume = nume
        self.prenume = prenume
        self.materii = {}
        self.absente = 0

    def __str__(self):
        return f"Numarul de absente al studentului {self.nume} este {self.absente}"

    def incrementare_absente(self):
        self.absente += 1

    def decrement_absente(self,scutiri):
        if type(scutiri) == int:
            self.absente -= scutiri
        else:
            return "Numar de scutiri invalid!"

class Extensie1(Catalog):
    def __init__(self, nume, prenume):
        super().__init__(nume, prenume)
        self.lista_note = []
        self.materie = ''

    def adaugare_in_dictionar(self,materie,lista_note):
        self.materii.update({materie : lista_note})

    def afisare_materii(self):
        for key in self.materii.keys():
            print("Materiile studentului " + self.nume + " sunt " + key)

    def afisare_medie_note(self):
        new_list = []
        index = 0
        for q in self.materii.values():
            new_list.append(sum(q) / len(q))
        for key in self.materii.keys():
            print(f"Notele studentului {self.nume} la materia: " + key + " sunt " + str(new_list[index]))
            index += 1


student1 = Extensie1('Roata','Ion')
student1.incrementare_absente()
student1.incrementare_absente()
student1.incrementare_absente()
# print(student1)

student2 = Extensie1('Cerc','George')
for i in range(4):
    student2.incrementare_absente()
# print(student2)
student2.decrement_absente(2)
# print(student2)
# print(student1)
# print(student2)
student1.adaugare_in_dictionar("Python",[5,6,8])
student2.adaugare_in_dictionar("Python",[3,6,9])
student2.adaugare_in_dictionar("Matematica",[2,5,2])
student1.adaugare_in_dictionar("Romana",[6,5,3])
student1.afisare_materii()
student2.afisare_materii()
student1.afisare_medie_note()
student2.afisare_medie_note()


