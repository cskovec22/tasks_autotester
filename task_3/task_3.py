from typing import Tuple


class BaseConverter:
    """
    Класс конвертера из градусов по Цельсию в Кельвины​ или ​Фаренгейты.
    """

    UNITS: Tuple[str, str] = ("F", "K")

    K_ADD_FROM_CELSIUS_TO_FAHRENHEIT: int = 32
    K_MULT_FROM_CELSIUS_TO_FAHRENHEIT: float = 9 / 5
    K_FROM_CELSIUS_TO_KELVIN: float = 273.15

    def convert(self, degrees: float, unit: str) -> Tuple[float, str]:
        """
        Конвертировать значение градусов по Цельсию в Кельвины или Фаренгейты.

        Args:
            degrees (float): Значение градусов.
            unit (str): Единица измерения, в которую нужно
                конвертировать градусы по Цельсию.

        Returns:
            Tuple[float, str]: Кортеж конвертированных градусов
                и единица измерения.
        """
        if unit not in self.UNITS:
            raise ValueError(
                f"Недопустимое значение единицы измерения: {unit}. "
                f"Допустимые значения: {', '.join(self.UNITS)}."
            )

        if unit == "K":
            return round(degrees + self.K_FROM_CELSIUS_TO_KELVIN, 2), unit
        elif unit == "F":
            return round(
                degrees * self.K_MULT_FROM_CELSIUS_TO_FAHRENHEIT
                + self.K_ADD_FROM_CELSIUS_TO_FAHRENHEIT,
                3
            ), unit


if __name__ == "__main__":
    converter: BaseConverter = BaseConverter()
    try:
        degrees: float = float(input("Введите градусы Цельсия: "))
        unit: str = input(
            "Введите единицу измерения, в которую нужно конвертировать, "
            "в виде K (для перевода в Кельвины) или F "
            "(для перевода в Фаренгейты): "
        )
        converted_degrees = converter.convert(degrees, unit)
        print(
            f"{degrees} °C = {converted_degrees[0]} °{converted_degrees[1]}"
        )
    except ValueError as err:
        print(f"Ошибка: {err}")
