from typing import List

def max_list_elem(ls: List[int]) -> int:
    if not ls:
        raise ValueError("The list is empty")

    max = float("-inf")

    for element in ls:
        if element > max:
            max = element

    return int(max)

def min_list_elem(ls: List[int]) -> int:
    if not ls:
        raise ValueError("The list is empty")

    min = float("inf")

    for element in ls:
        if element < min:
            min = element

    return int(min)

def max_list_idx(ls: List[int]) -> int:
    if not ls:
        raise ValueError("The list is empty")

    max = ls[0]
    ans = 0

    for idx in range(1, len(ls)):
        if ls[idx] > max:
            max = ls[idx]
            ans = idx

    return ans

def min_list_idx(ls: List[int]) -> int:
    if not ls:
        raise ValueError("The list is empty")

    min = ls[0]
    ans = 0

    for idx in range(1, len(ls)):
        if ls[idx] < min:
            min = ls[idx]
            ans = idx

    return ans

def max_min_sum(ls: List[int]) -> int:
    return max_list_elem(ls) + min_list_elem(ls)

def get_sum(ls: List[int]) -> int:
    ans = 0
    for element in ls:
        ans += element

    return ans

def mean_list(ls: List) -> None:
    size = len(ls)
    for idx in range(size):
        ls[idx] /= size


if __name__ == "__main__":
    ls = [1, 2, 3, 6, 234, 5436, 2212]
    print(ls)
    print(max_list_elem(ls))
    print(min_list_elem(ls))
    print(max_list_idx(ls))
    print(min_list_idx(ls))
    print(max_min_sum(ls))
    print(get_sum(ls))
    print(mean_list(ls))





