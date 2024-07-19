from typing import List, Any

def flatten_list(ls: List[Any]) -> List[Any]:
    ans = []
    for element in ls:
        if isinstance(element, list):
            ans += flatten_list(element)
        else:
            ans.append(element)

    return ans

def list_sum(ls: List[int], idx: int = 0) -> int:
    if idx == len(ls) - 1:
        return ls[-1]

    return ls[idx] + list_sum(ls, idx + 1)

def is_sorted_ascending(ls: List[int]) -> bool:
    if len(ls) <= 1:
        return True

    if ls[0] > ls[1]:
        return False

    return is_sorted_ascending(ls[1:])

if __name__ == "__main__":
    ls = [1, [2, [3, 4], 5], 6, [7, 8]]
    print(flatten_list(ls))
    ls2 = [1, 2, 3, 5, 4]
    print(list_sum(ls2))
    print(is_sorted_ascending(ls2))
