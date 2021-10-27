def getDigit(number, bit): #หาค่าหลัก
    if number >= 0:
        for i in range(bit - 1):
            number //= 10
        return number % 10
    else:
        number *= -1
        for i in range(bit - 1):
            number //= 10
        return number % 10

print(getDigit(-3, 1))
