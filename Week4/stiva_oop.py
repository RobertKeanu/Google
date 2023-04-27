class Stack:
    def __init__(self, val_stiva):
        self.__stacklist = []

    def push(self, val):
        self.__stacklist.append(val)

    def pop(self):
        self.second = 5
        value = self.__stacklist[-1]
        del self.__stacklist[-1]
        return value

    def __str__(self):
        return f"{self.__stacklist}{self.second}"


obiect1 = Stack(val_stiva=1)
obiect1.push(4)
obiect1.push(5)
obiect1.pop()
obiect1.third = 6
print(obiect1.__dict__) #ce am folosit in clasa
# print(obiect1.stacklist)
print(obiect1._Stack__stacklist) #pentru atribute private
print(obiect1)