from collections import Counter
from typing import Dict


def find_duplicate_char(word: str) -> Dict[str, int]:
    """
    Возвращает повторяющиеся символы в строке.

    Args:
        word (str): Входная строка.

    Returns:
        (Dict[str, int]): Словарь с повторяющимися символами и их количеством.
    """
    char_count: Counter = Counter(word)
    return {key: value for key, value in char_count.items() if value > 1}


if __name__ == "__main__":
    word: str = input(
        "Введите строку, в которой нужно найти повторяющиеся символы: "
    )
    dict_char: Dict[str, int] = find_duplicate_char(word)
    print(f"\nВ строке '{word}'\n")
    for key, value in dict_char.items():
        if value > 1:
            print(f"символ '{key}' повторяется {value} раз")
