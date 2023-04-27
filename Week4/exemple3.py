class Exemplu:
    def __init__(self, val):
        self.val = val
        self.a , self.b = None, None
        if val % 2 != 0:
            self.a = 1
        else:
            self.b = 1

    def denumire(self):
        return self.val

obiect = Exemplu(1)
print(obiect.a)
try:
    print(obiect.b)
except AttributeError:
    pass
print(obiect.b)
print(obiect.denumire())