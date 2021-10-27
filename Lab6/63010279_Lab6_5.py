def asteroid_collision(asts):
    data = []
    addData(asts,data)
    return data

def check_collision(stack, asts):
    if not stack:
        stack.append(asts)
    elif asts < 0 and stack[-1] > 0:
        if asts + stack[-1] == 0:  # Asteroids of same size cancel each other
            stack.pop()
        elif asts + stack[-1] < 0:  # This is where a recursion might appear: a collision is detected
            stack.pop()
            check_collision(stack, asts)
    else:
        stack.append(asts)

def addData(input, stack):
    if input != []:
        check_collision(stack, input[0])
        input.pop(0)
        addData(input, stack)

if __name__ == "__main__":
    x = input("Enter Input : ").split(",")
    x = list(map(int,x))
    print(asteroid_collision(x))