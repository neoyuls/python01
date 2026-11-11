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


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int,
                 color: str) -> None:
        super().__init__(name, height, age)
        self._color = color
        self._bloomed = False

    def bloom(self) -> None:
        self._bloomed = True

    def show(self) -> None:
        print(super().show())
        print(f"Color: {self._color}")
        if self._bloomed:
            print(f"{self._name} is blooming beautifully!")
        else:
            print(f"{self._name} has not bloomed yet.")


class Tree(Plant):
    def __init__(self, name: str, height: float, age: int,
                 trunk_diameter: float) -> None:
        super().__init__(name, height, age)
        self._trunk_diameter = trunk_diameter

    def show(self) -> None:
        print(super().show())
        print(f"Trunk diameter: {self._trunk_diameter}cm")

    def produce_shade(self) -> None:
        print(f"Tree {self._name} now produces a shade of "
              f"{self._height}cm long and {self._trunk_diameter}cm wide.")


class Vegetable(Plant):
    def __init__(self, name: str, height: float, age: int,
                 harvest_season: str,
                 nutritional_value: int = 0) -> None:
        super().__init__(name, height, age)
        self._harvest_season = harvest_season
        self._nutritional_value = nutritional_value

    def grow(self, days: int = 1, rate: float = 0.8) -> None:
        super().grow(days, rate)
        self._nutritional_value += days

    def show(self) -> None:
        print(super().show())
        print(f"Harvest season: {self._harvest_season}")
        print(f"Nutritional value: {self._nutritional_value}")


def ft_plant_types() -> None:
    rose = Flower("rose", 15.0, 10, "red")
    oak = Tree("oak", 200.0, 365, 5.0)
    tomato = Vegetable("tomato", 5.0, 10, "April")

    print("=== Garden Plant Types ===\n")

    print("=== Flower\n")
    rose.show()
    print("\n[asking the rose to bloom]\n")
    rose.bloom()
    rose.show()

    print("\n=== Tree\n")
    oak.show()
    print("\n[asking the oak to produce shade]\n")
    oak.produce_shade()

    print("\n=== Vegetable\n")
    tomato.show()
    print("\n[make tomato grow and age for 20 days]\n")
    tomato.age(20)
    tomato.grow(20, 2.1)
    tomato.show()


if __name__ == "__main__":
    ft_plant_types()
