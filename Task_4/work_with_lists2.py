from typing import List, Any, Dict, TypeVar

def longest_string(ls: List[str]) -> str:
    if not ls:
        raise ValueError("The list is empty")

    ans_idx = 0
    max_len = len(ls[0])

    for idx in range(1, len(ls)):
        str_len = len(ls[idx])
        if str_len > max_len:
            max_len = str_len
            ans_idx = idx

    return ls[ans_idx]

def acronym(ls: List[str]) -> str:
    if not ls:
        raise ValueError("The list is empty")

    ans = ""
    for idx in range(len(ls)):
        string = ls[idx].strip()
        if not len(string):
            continue
        string = string.capitalize()
        ans += string[0]
        ls[idx] = string

    return ans
        
def reverse_list(ls: List[Any]) -> None:
    for idx in range(len(ls) - 1, -1, -1):
        print(ls[idx])

T = TypeVar('T')
def is_present(ls: List[T], target: T) -> bool:
    for element in ls:
        if element == target:
            return True
    return False

def count_strings(ls: List[str]) -> Dict[str, int]:
    dic: Dict[str, int] = {}
    for string in ls:
        if string in dic:
            dic[string] += 1
        else:
            dic[string] = 1

    return dic

def odd_even(ls: List[int]) -> None:
    if not ls:
        return

    start = 0
    end = len(ls) - 1 

    while start < end:
        while ls[start] % 2 != 0:
            start += 1
            if start == end:
                return

        while ls[end] % 2 == 0:
            end -= 1
            if start == end:
                return

        ls[start], ls[end] = ls[end], ls[start]

if __name__ == "__main__":
    ls1 = [2, 1]
    ls2 = [1, 3, 5, 2, 4, 6, 9]
    ls3 = [2, 4, 6, 1, 3, 5, 23]
    ls4 = [1, 2, 3, 4, 5, 6, 7]

    print(f"og: {ls1}")
    odd_even(ls1)
    print(f"new: {ls1}")

    print(f"og: {ls2}")
    odd_even(ls2)
    print(f"new: {ls2}")

    print(f"og: {ls3}")
    odd_even(ls3)
    print(f"new: {ls3}")

    print(f"og: {ls4}")
    odd_even(ls4)
    print(f"new: {ls4}")
