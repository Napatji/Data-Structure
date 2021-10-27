class MyInt:
    def __init__(self,number):
        self.decimal = number
    def __add__(a,b):
        sum = a.decimal+b.decimal+(a.decimal+b.decimal)//2
        return sum
    def toRoman(self):
        number = self.decimal
        temp = ""
        #Check Roman
        if number >= 1000:
            multiple =  int((number) / 1000)
            temp = temp + "M"*multiple
            number = number % 1000
            if number < 1000 and number >=100:
                if number == 900:
                    temp = temp + "CM"
                elif number < 900 and number > 500:
                    multiple = int((number-500) / 100)
                    temp = temp + "D" + ("C"*multiple)
                elif number == 500:
                    temp = temp + "D"
                elif number < 500 and number >= 400:
                    temp = temp + "CD"
                elif number == 100:
                    multiple = int(number / 100)
                    temp = temp + "C"*multiple 
                number = number % 100   
                if number > 10 and number < 100:
                    if number == 90:
                        temp = temp + "XC"
                    elif number < 90 and number > 50:
                        multiple = int((number-50) / 10)
                        temp = temp + "L" + ("X"*multiple)
                    elif number == 50:
                        temp = temp + "L"
                    elif number == 40:
                        temp = temp + "XL"
                    elif number < 40 and number >= 10:
                        multiple = int(number / 10)
                        temp = temp + ("X"*multiple)  
                    number = number % 10  
                    if number >= 0 and number < 10:
                        if number == 9:
                            temp = temp + "IX"
                        elif number < 9 and number > 5:
                            multiple = int(number-5 / 1)
                            temp = temp + "V" + ("I"*multiple)
                        elif number == 5:
                            temp = temp + "V"
                        elif number == 4:
                            temp = temp + "IV"
                        elif number < 4 and number >= 1:
                            multiple = int(number / 1)
                            temp = temp + ("I"*multiple)
            return temp
        if number < 1000 and number >=100:
            if number == 900:
                temp = temp + "CM"
            elif number < 900 and number > 500:
                multiple = int((number-500) / 100)
                temp = temp + "D" + ("C"*multiple)
            elif number == 500:
                temp = temp + "D"
            elif number < 500 and number >= 400:
                temp = temp + "CD"
            elif number == 100:
                multiple = int(number / 100)
                temp = temp + "C"*multiple  
            number = number % 100   
            if number > 10 and number < 100:
                if number == 90:
                    temp = temp + "XC"
                elif number < 90 and number > 50:
                    multiple = int((number-50) / 10)
                    temp = temp + "L" + ("X"*multiple)
                elif number == 50:
                    temp = temp + "L"
                elif number == 40:
                    temp = temp + "XL"
                elif number < 40 and number >= 10:
                    multiple = int(number / 10)
                    temp = temp + ("X"*multiple)  
                number = number % 10  
                if number >= 0 and number < 10:
                    if number == 9:
                        temp = temp + "IX"
                    elif number < 9 and number > 5:
                        multiple = int(number-5 / 1)
                        temp = temp + "V" + ("I"*multiple)
                    elif number == 5:
                        temp = temp + "V"
                    elif number == 4:
                        temp = temp + "IV"
                    elif number < 4 and number >= 1:
                        multiple = int(number / 1)
                        temp = temp + ("I"*multiple)
            return temp     
        if number >= 10 and number < 100:
            if number == 90:
                temp = temp + "XC"
            elif number < 90 and number > 50:
                multiple = int((number-50) / 10)
                temp = temp + "L" + ("X"*multiple)
            elif number == 50:
                temp = temp + "L"
            elif number == 40:
                temp = temp + "XL"
            elif number < 40 and number >= 10:
                multiple = int(number / 10)
                temp = temp + ("X"*multiple)
            number = number % 10  
            if number >= 0 and number < 10:
                if number == 9:
                    temp = temp + "IX"
                elif number < 9 and number > 5:
                    multiple = int(number-5 / 1)
                    temp = temp + "V" + ("I"*multiple)
                elif number == 5:
                    temp = temp + "V"
                elif number == 4:
                    temp = temp + "IV"
                elif number < 4 and number >= 1:
                    multiple = int(number / 1)
                    temp = temp + ("I"*multiple)
            return temp  
        if number >= 0 and number < 10:
            if number == 9:
                temp = temp + "IX"
            elif number < 9 and number > 5:
                multiple = int(number-5 / 1)
                temp = temp + "V" + ("I"*multiple)
            elif number == 5:
                temp = temp + "V"
            elif number == 4:
                temp = temp + "IV"
            elif number < 4 and number >= 1:
                multiple = int(number / 1)
                temp = temp + ("I"*multiple)
            return temp 

if __name__ == "__main__":
    print(" *** class MyInt ***")
    user_input = input("Enter 2 number : ").split(" ")
    fisrt_num = MyInt(int(user_input[0]))
    second_num = MyInt(int(user_input[1]))
    print("{0} convert to Roman : {1}".format(user_input[0],fisrt_num.toRoman()))
    print("{0} convert to Roman : {1}".format(user_input[1],second_num.toRoman()))
    print("{0} + {1} = {2}".format(user_input[0],user_input[1],fisrt_num + second_num))
    