from typing import List

def is_prime(num: int) -> bool:
    if num == 2:
        return True

    if num < 2 or not num % 2:
        return False

    for i in range(3, int(num ** 0.5)):
        if num % i == 0:
            return False

    return True

def find_max_of_3(num1: int, num2: int, num3: int) -> int:
    ans = num1 if num1 > num2 else num2
    return ans if ans > num3 else num3

def fib(num: int) -> List[int]:
    if num < 0:
        return []

    ans = [0]
    prev = 0
    curr = 1

    for _ in range(num):
        ans.append(curr)
        curr, prev = prev + curr, curr

    return ans

def is_square(num: int) -> bool:
    return bin(num).count("1") == 1

if __name__ == "__main__":
    for i in range(14):
        if is_prime(i):
            print(i, end=" ")

    print("\n")
    print(find_max_of_3(1, 3, 2), end="\n\n")
    print(fib(10), end="\n\n")
    for i in range(1000):
        if is_square(i):
            print(i, end=" ")
    print()
