from typing import Callable

def add(num1: float, num2: float) -> float:
    return num1 + num2

def sub(num1: float, num2: float) -> float:
    return num1 - num2

def mul(num1: float, num2: float) -> float:
    return num1 * num2

def div(num1: float, num2: float) -> float:
    if num2 == 0:
        pass
    return num1 / num2

def get_action() -> Callable[[float, float], float]:
    while True:
        symbol = input("Choose:  + | - | * | / \n").strip()

        if len(symbol) > 1:
            pass
        elif symbol == '+':
            return add
        elif symbol == '-':
            return sub
        elif symbol == '*':
            return mul
        elif symbol == '/':
            return div

        print("Invalid input")

def is_float(num: str) -> bool:
    return num.isdigit() or (num.replace(".", "", 1).isdigit())

def get_number(pos: str) -> float:
    while True:
        num = input(f"Give the {pos} number: ").strip()

        if is_float(num):
            return float(num) 

        print("Invalid input")

def calculator() -> float:
    action = get_action()
    num1 = get_number("First")
    num2 = get_number("Second")
    return action(num1, num2)

if __name__ == "__main__":
    print(calculator())



















