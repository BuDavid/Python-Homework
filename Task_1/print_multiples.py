def print_multiple(target: int, scope: int) -> None:
    for i in range(1, scope + 1):
        if (i % target == 0):
            print(i)

if __name__ == "__main__":
    print_multiple(3, 20)
