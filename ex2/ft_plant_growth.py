#!/usr/bin/env python3
class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name.capitalize()
        self._height = height
        self._age = age

    def show(self) -> str:
        return f"{self._name}: {self._height}cm, {self._age} days old"

    def grow(self, days: int = 1, rate: float = 0.8) -> None:
        self._height = round(self._height + (rate * days), 1)

    def age(self, days: int = 1) -> None:
        self._age += days

    def get_height(self) -> float:
        return self._height


def ft_plant_growth() -> None:
    rose = Plant("rose", 25.0, 30)
    initial = rose.get_height()
    print("=== Garden Plant Growth ===")
    print(rose.show())
    day = 1
    while day <= 7:
        print(f"=== Day {day} ===")
        rose.age()
        rose.grow()
        print(rose.show())
        day += 1
    print(f"Growth this week: {round(rose.get_height() - initial, 1)}cm")


if __name__ == "__main__":
    ft_plant_growth()
