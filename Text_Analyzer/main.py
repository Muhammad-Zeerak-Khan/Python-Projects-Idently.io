from ast import Tuple
from collections import Counter


def open_file(file_path: str) -> str:
    with open(file_path, "r") as f:
        text: str = f.read()
        return text


# Get the total chars incl spaces ,exc spaces, total spaces, total words


def text_analyzer(text: str) -> dict[str, int]:
    result: dict[str, int] = {
        "total_chars_with_spaces": len(text),
        "total_chars_without_spaces": len(text.replace(" ", "")),
        "total_number_of_spaces": text.count(" "),
        "total_words": len(text.split()),
    }
    return result


def get_top_k_common_word(text: str, k: int = 5) -> list[str]:
    """Get the top k common word"""
    words_count: Counter[str] = Counter(text.split())
    k_most_common_words: list[str] = [
        word[0] for word in words_count.most_common(k) if word[1] == k
    ]
    return k_most_common_words


if __name__ == "__main__":
    text: str = open_file("note.txt")
    report: dict[str, int] = text_analyzer(text)
    print("#" * 50)
    print(f"{' ' * 10}Text Analyzer Report{' ' * 10}")
    print(
        f"The text contains : {report.get('total_chars_with_spaces')} total characters."
    )
    print(f"The text contains : {report.get('total_chars_without_spaces')} characters.")
    print(f"The text contains : {report.get('total_number_of_spaces')} spaces.")
    print(f"The text contains : {report.get('total_words')} words.")
    n: int = 10
    print(f"The top {n} most common words are : {get_top_k_common_word(text, n)}")
    print("#" * 50)
