COUNT_HOURS = 12
K_HOURS_ANGLE_PER_HOUR = 360 / COUNT_HOURS
K_HOURS_ANGLE_PER_MINUTE = K_HOURS_ANGLE_PER_HOUR / 60
K_MINUTES_ANGLE_PER_MINUTE = 360 / 60


def calculate_angle(hours: int, minutes: int) -> float:
    """
    Вычисляет угол между часовой и минутной стрелками часов.

    Args:
        hours (int): Часы.
        minutes (int): Минуты.

    Returns:
        (float): Значение угла между часовой и минутной стрелками часов.
    """
    if not (0 <= minutes < 60) or not (0 <= hours < 24):
        raise ValueError(
            "Некорректное значение времени. Часы должны быть в диапазоне "
            "от 0 до 23, минуты от 0 до 59."
        )

    hours_angle: float = (hours % COUNT_HOURS) * K_HOURS_ANGLE_PER_HOUR
    # Поправка на минутную стрелку
    hours_angle += minutes * K_HOURS_ANGLE_PER_MINUTE

    minutes_angle: int = minutes * K_MINUTES_ANGLE_PER_MINUTE

    angle_difference: int = abs(hours_angle - minutes_angle)

    if angle_difference > 180:
        return 360 - angle_difference
    return angle_difference


if __name__ == "__main__":
    try:
        hours: int = int(input("Введите часы: "))
        minutes: int = int(input("Введите минуты: "))
        angle: int = calculate_angle(hours, minutes)
        print(
            "Угол между часовой и минутной стрелками "
            "часов при значении времени "
            f"'{hours:02d}:{minutes:02d}' равен {angle}°."
        )
    except ValueError as err:
        print(f"Ошибка: {err}")
