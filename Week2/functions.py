
def fun(a:int = 3 , b:int = 1, *args) ->bool:
    if a > b:
        return True
    return False

if fun(2,3,4,5,6,7,8) == True:
    print("True")
else:
    print("False")

def fun2(*args):
    sum = 0
    sum += args[2]
    return sum

print(fun2(1,2,3,4,5,6))
