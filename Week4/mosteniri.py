class Exemplu1:

    counter = 1
    def nume(self):
        return "Ion"


class Exemplu2:
    counter = 2
    # def nume(self):
    #     return "Robert"


class Exemplu3(Exemplu1, Exemplu2):
    def name(self):
        return "Silviu"

obiect = Exemplu3()
print(obiect.name())