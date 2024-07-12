def print_negative(ls:list) -> None:
    for num in ls:
        if num < 0:
            print(num)

if __name__ == "__main__":
    ls = [-5, 3, -1, 101, -33, 44, 0, 7]
    print_negative(ls)
