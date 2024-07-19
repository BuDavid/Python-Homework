from typing import List, Any, Dict

def print_range(num: int):
    if num < 1:
        return 

    print_range(num - 1)
    print(num)

def print_range_reverse(num: int):
    if num < 1:
        return 

    print(num)
    print_range_reverse(num - 1)

def factorial(num: int) -> int:
    if num < 0:
        return num

    if num == 0:
        return 1

    return num * factorial(num - 1)

def sum_up_to(num: int) -> int:
    if num < 0:
        return num

    if num == 1:
        return 1

    return num + sum_up_to(num - 1)

def print_list(ls: List[Any]):
    if not ls:
        return

    print(ls[0])
    print_list(ls[1:])

def list_len(ls: List[Any]) -> int:
    if not ls:
        return 0

    return 1 + list_len(ls[1:])

def reverse_string(string: str) -> str:
    if not string:
        return ""

    return reverse_string(string[1:]) + string[0] 

def fib(idx: int, seen: Dict[int, int] = {}) -> int:
    if idx in seen:
        return seen[idx] 

    if idx < 2:
        return idx

    ans = fib(idx - 1) + fib(idx - 2)
    seen[idx] = ans
    return ans

def print_string(string: str) -> str:
    if not string:
        return ""

    print(string[0])
    return print_string(string[1:]) 

def is_palindrom(string: str) -> bool:
    if len(string) <= 1:
        return True
    if string[0] != string[-1]:
        return False

    return is_palindrom(string[1:-1])

def sum_of_digits(num: int) -> int:
    if num < 10:
        return num

    return num % 10 + sum_of_digits(num // 10)

if __name__ == "__main__":
    print_range(5)
    print()
    print_range_reverse(5)
    print()
    print(factorial(5))
    print()
    print(sum_up_to(5))
    print()
    ls = [1, 2, 3, 4, 5]
    print_list(ls)
    print()
    print(list_len(ls))
    print()
    string = "hello"
    print(reverse_string(string))
    print()
    print(fib(10))
    print()
    print_string(string)
    print(is_palindrom("tattat"))
    print(sum_of_digits(23075982))


