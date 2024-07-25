from typing import Optional, Dict, Any

def great_user(name: str, surname: str, msg: str = "Hello") -> None:
    print(f"{msg} {name} {surname}")

def count_price(item1: int, item2: int, item3: int, /, tax: int = 25) -> int:
    return item1 + item2 + item3 + tax

def print_user_profile(name: str, surname: str, *, age: int, city: str) -> None:
    print(f"{name} {surname} age: {age} city: {city}")

def calculator(num1: int, num2: int, /, op: str = "sum") -> Optional[int]:
    if op == "sum":
        return num1 + num2
    elif op == "sub":
        return num1 - num2
    else:
        return None

def unpack(*, name: str, price: int, section: str) -> None:
    print(f"{name} price: {price} section: {section}") 

def report(first_paragraph: str, second_paragraph: str, date: str, /, header: str = "", footer: str = "") -> None:
    print(f"{date}\n{header}{first_paragraph}{second_paragraph}{footer}")

def log_msg(*args, **kwargs) -> None:
    print("Metadata:")
    for key, val in kwargs.items():
        print(f"{key} : {val}")
    print("\nData:")
    for arg in args:
        print(arg)

if __name__ == "__main__":
    great_user("Alan", "Turing", "Hello Mr.")
    print(count_price(1, 2, 3))
    print_user_profile("Alan", "Turing", age=41, city="London")
    dic: Dict[str, Any] = {"price" : 100, "name" : "toy", "section" : "B2"}
    unpack(**dic)
