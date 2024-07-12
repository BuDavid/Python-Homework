def vowel_cons_count(text: str) -> None:
    vowels = "aeiouy"
    vowel = 0
    consonant = 0

    for ch in text:
        if ch.isalpha():
            if ch in vowels:
                vowel += 1
            else:
                consonant += 1

    print(f"There are {vowel} vowels and {consonant} consonants in: {text}")

if __name__ == "__main__":
    vowel_cons_count("aabbccddef")
