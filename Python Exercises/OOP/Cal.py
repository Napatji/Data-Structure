class Calculator:
    def __init__(self,name):
        self.name = name
    def calculate(self,number1,number2,operator):
        self.number1 = int(number1)
        self.number2 = int(number2)
        self.operator = operator

        if operator == "+":
            answer = number1 + number2
        elif operator == "-":
            answer = number1 - number2
        elif operator == "*":
            answer = number1 * number2
        elif operator == "/":
            answer = number1 / number2

        print("Your answer is : " + str(answer))
