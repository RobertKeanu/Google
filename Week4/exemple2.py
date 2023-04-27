class FirstClass:

    __counter = 0

    def __init__(self, val=1):
        self.__first = val
        FirstClass.__counter += 1

obiect1 = FirstClass()
obiect2 = FirstClass()
obiect3 = FirstClass()

print(obiect1.__dict__,obiect1._FirstClass__counter)
print(obiect2.__dict__,obiect2._FirstClass__counter)
print(obiect3.__dict__,obiect3._FirstClass__counter)