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


def ft_plant_factory() -> None:
    plants = [
        Plant("rose", 25.0, 30),
        Plant("oak", 200.0, 365),
        Plant("cactus", 5.0, 90),
        Plant("sunflower", 80.0, 45),
        Plant("fern", 15.0, 120)
    ]

    print("=== Plant Factory Output ===")
    for plant in plants:
        print(f"Created: {plant.show()}")


if __name__ == "__main__":
    ft_plant_factory()
