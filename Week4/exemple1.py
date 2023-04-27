"""
Max este o pisica mare care doarme toata ziua.
Max este obiectul (instantiaza clasa / substantive)
Pisica este clasa (prop. generala pe care noi adaugam proprietati si atribute/ definesc obiectul)(substantiv)
Proprietatea este marimea pisicii (adjectivul)
Atributul este ca doarme (adverb)

O masina Dacia merge repede.
Dacia este obiectul
O masina este clasa
Proprietatea este repede
Atributul este ca merge
"""

# class Pisica:
#     pass
#
# primul_obiect = Pisica()

stack = []

def push(val):
    stack.append(val)

def pop():
    value = stack[-1]
    del stack[-1]
    return value

push(3)
push(2)

print(pop())

