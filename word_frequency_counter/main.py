from collections import Counter
import re

def get_frequency(text: str) -> list[tuple[str, int]]:
    lowered_text: str = text.lower()
    words : list[str] = re.findall(r'\b\w+\b', lowered_text)
    word_count: Counter = Counter(words)

    return word_count.most_common()

def main() -> None:
    input_text: str = input("Enter your text: ").strip() # Removes leading and trailing whitespaces

    word_frequencies: list[tuple[str, int]] = get_frequency(input_text)
    for word, count in word_frequencies:
        print(f" {word} : {count}")

if __name__ == "__main__":
    main()    


"""
Create a function that allows the user to read a file directly (such as text)
so that the user doesnot have to copy and paste text
"""