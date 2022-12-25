"""
The temperature module: Manipulate your temperature easily

Easily calculate daily average temperature
"""

from typing import List


class HighTemperature:
    """Class representing very high temperatures"""

    def __init__(self, value: float):
        """
        :param value: value of temperature
        """

        self.value = value


def daily_average(temperatures: List[float]) -> float:
    """
    Get average daily temperature

    Calculate average temperature from multiple measurements

    >>> daily_average([10.0, 12.0, 14.0])
    12.0

    :param temperatures: list of temperatures
    :return: average temperature
    """

    return sum(temperatures) / len(temperatures)
