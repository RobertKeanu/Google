cnp = input("Input the social security number: ")
print(validate(cnp))

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

    if control_digit == something[len(something)]:
        return True
    return False

def validate_nnn(something: str) -> bool:
    if something[9] >= 0 and something[10] >= 0 and something[11] <= 9:
        return True
    return False

def validate_jj(something : str) -> bool:
    day = int(something[7:9])
    if 1<= day <= 46 or day in [51,52]:
        return True
    return False

def validate_zz(something: str) -> bool:


