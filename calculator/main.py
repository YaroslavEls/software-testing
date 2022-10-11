import math

class CalculatorState:
    def __init__(self):
        self.screen = 0
        self.first_number = 0
        self.op = None
        self.start_new_number = True

nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
opers = ["+", "-", "*", "/"]

def operation(num1, num2, oper):
    match oper:
        case "+":
            return num1 + num2
        case "-":
            return num1 - num2
        case "*":
            return num1 * num2
        case "/":
            if num2 == 0:
                return
            return math.floor(num1 / num2)

def handle_key_press(calc_state, key):
    if key in nums:
        if (calc_state.start_new_number):
            calc_state.screen = int(key)
        else:
            calc_state.screen = int(str(calc_state.screen) + key)
        calc_state.start_new_number = False

    elif key in opers:
        calc_state.op = key
        calc_state.first_number = calc_state.screen
        calc_state.start_new_number = True

    elif key == "=":
        calc_state.screen = operation(calc_state.first_number, calc_state.screen, calc_state.op)

def calculate(exp):
    calc = CalculatorState()
    for i in exp.split(' '):
        handle_key_press(calc, i)
    return calc.screen


if __name__ == "__main__":
    f = open('input.txt', 'r')
    data = f.read()
    f.close()

    res = calculate(data)

    f = open('output.txt', 'w')
    f.write(str(res))
    f.close()
