cnp = input("Input the social security number: ")

def validate_control_number(something :str) -> bool:
    control_digit = 0
    given_number = [2, 7, 9, 1, 4, 6, 3, 5, 8, 2, 7, 9]
    number_digits = [int(digits) for digits in something]
    for i in range(12):
        control_digit = control_digit + number_digits[i] * given_number[i]

    if control_digit % 11 == 10:
        control_digit = 1
    else:
        control_digit = control_digit % 11

    return control_digit == number_digits[-1]

def validate_nnn(something: str) -> bool:
    if int(something[9]) >= 0 and int(something[10]) >= 0 and int(something[11]) <= 9:
        return True
    return False

def validate_jj(something : str) -> bool:
    ww = int(something[7:9])
    if 1<= ww <= 46 or ww in [51,52]:
        return True
    return False

def validate_zz(something: str) -> bool:
    century = int(something[0])
    a1 = int(something[1])
    a2 = int(something[2])
    l1 = int(something[3])
    l2 = int(something[4])
    z1 = int(something[5])
    z2 = int(something[6])
    if z1 > 3:
        return False
    if z1 == 3 and z2 > 1:
        return False
    if l1 > 1:
        return False
    if l1 == 1 and l2 > 2:
        return False
    #in tema scrie pana la 2099 deci pot sa fie nascuti in anul 2024 - 2099?
    return True

def validate(something:str) -> str:
    if len(something) != 13:
        return "INVALID"
    if validate_control_number(something) and validate_zz(something) and validate_jj(something) and validate_nnn(something):
        return "VALID"

print(validate(cnp))
