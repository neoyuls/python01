#!/usr/bin/env python3
class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name.capitalize()
        self._height = height
        self._age = age

    def show(self) -> str:
        return f"{self._name}: {self._height}cm, {self._age} days old"


def ft_garden_data() -> None:
    plants = [
        Plant("rose", 25, 30),
        Plant("sunflower", 80, 45),
        Plant("cactus", 15, 120)
    ]
    print("=== Garden Plant Registry ===")
    for plant in plants:
        print(plant.show())


if __name__ == "__main__":
    ft_garden_data()
