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

    def get_age(self) -> int:
        return self._age

    def set_height(self, new_height: float) -> None:
        if new_height >= 0:
            self._height = float(new_height)
            print(f"Height updated: {new_height}cm")
        else:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")

    def set_age(self, new_age: int) -> None:
        if new_age >= 0:
            self._age = new_age
            print(f"Age updated: {new_age} days")
        else:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")


def ft_garden_security() -> None:
    plant = Plant("rose", 15.0, 10)
    print("=== Garden Security System ===")
    print(f"Plant created: {plant.show()}\n")
    plant.set_height(25)
    plant.set_age(30)
    print()
    plant.set_height(-1)
    plant.set_age(-1)
    print()
    print(f"Current state: {plant.show()}")


if __name__ == "__main__":
    ft_garden_security()
