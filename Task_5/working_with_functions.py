from typing import List, Any

def print_rev_scope(num: int) -> None:
    for i in range(num + 1):
        print(num - i, end = " ")

def print_scope(num: int) -> None:
    for i in range(num + 1):
        print(i, end = " ")

def print_list(ls: List) -> None:
    for element in ls:
        print(element, end = " ")

def num_sum(num: int) -> int:
    ans = 0
    while num:
        ans += num % 10
        num //= 10
    return ans

def first_upper(string: str) -> str:
    for ch in string:
        if 'A' <= ch <= 'Z':
            return ch

    return ""

def max_list_element(ls: List[Any]) -> Any:
    if not ls:
        return None

    if not hasattr(ls[0], "__gt__"):
        raise ValueError("Invalid argument")

    max = ls[0]

    for idx in range(1, len(ls)):
        if max < ls[idx]:
            max = ls[idx]

    return max

if __name__ == "__main__":
    print("printing n to 0")
    print_rev_scope(10)
    print("\n\nprinting 0 to n")
    print_scope(10)

    ls = [1, 2, 3, 4, 5, 6]
    print("\n\nprinting list")
    print_list(ls)

    print("\n\nprinting sum of 123 digits")
    print(num_sum(123))

    print("\nprinting first upper of hello World")
    print(first_upper("hello World"))

    print(f"\nprinting max element of {ls}")
    print(max_list_element(ls))










