class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        self._height = height
        self._plant_age = age

    def show(self) -> str:
        cap = self._name.capitalize()
        return f"{cap}: {self._height}cm, {self._plant_age} days old"

    def get_age(self) -> int:
        return self._plant_age

    def get_height(self) -> float:
        return self._height

    def set_age(self, newage: int) -> None:
        if newage >= 0:
            self._plant_age = newage
            print(f"Age updated: {newage} days")
        else:
            print(f"{self._name.capitalize()}: Error, age can't be negative")
            print("Age update rejected")

    def set_height(self, newheight: float) -> None:
        if newheight >= 0:
            self._height = float(newheight)
            print(f"Height updated: {newheight}cm")
        else:
            print(f"{self._name.capitalize()}: Error, height can't be negative")
            print("Height update rejected")


def ft_garden_security() -> None:
    plant = Plant("rose", 15.0, 10)
    print("=== Garden Security System ===")
    print(f"Plant created: {plant.show()} \n")
    plant.set_height(25)
    plant.set_age(30)
    print()
    plant.set_height(-1)
    plant.set_age(-1)
    print()
    print(f"Current state: {plant.show()}")


if __name__ == "__main__":
    ft_garden_security()
