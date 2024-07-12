def print_word_by_idx(word:str) -> None:
    for i in range(len(word)):
        print(f"{word[i]}: {i}")

if __name__ == "__main__":
    print_word_by_idx("Python")
