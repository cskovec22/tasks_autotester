import random
from typing import List, Tuple


def create_random_arr(number: int, max_value: int) -> List[int]:
    """
    Создает массив целых положительных чисел.

    Args:
        number (int): Количество чисел в массиве.
        max_value (int): Максимально возможное значение в массиве.

    Returns:
        List[int]: Массив случайных целых положительных чисел.
    """
    return [round(random.random() * max_value) for _ in range(number)]


def get_max_min_avg(arr: List[int]) -> Tuple[int, int, float]:
    """
    Возвращает максимальное, минимальное и среднее значение входящего массива.

    Args:
        arr (List[int]): Входной массив чисел.

    Returns:
        (Tuple[int, int, float]): Кортеж из максимального,
            минимального и среднего значения входящего массива.
    """
    return max(arr), min(arr), round(sum(arr) / len(arr), 2)


if __name__ == "__main__":
    number: int = int(input("Введите количество чисел в массиве: "))
    max_value: int = int(
        input("Введите максимально возможное значение в массиве: ")
    )
    arr: List[int] = create_random_arr(number, max_value)
    max_num, min_num, avg_num = get_max_min_avg(arr)
    print(
        f"\nМассив случайных чисел: {arr}\n"
        f"Максимальное значение в массиве: {max_num}\n"
        f"Минимальное значение в массиве: {min_num}\n"
        f"Среднее значение в массиве: {avg_num}"
    )
