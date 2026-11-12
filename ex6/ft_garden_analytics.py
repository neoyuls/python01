#!/usr/bin/env python3
class Plant:
    class Stats:
        def __init__(self, grow_stat: int = 0,
                     show_stat: int = 0,
                     age_stat: int = 0):
            self.grow_stat = grow_stat
            self.age_stat = age_stat
            self.show_stat = show_stat

        def display(self):
            print(f"Stats: {self.grow_stat} grow, ", end="")
            print(f"{self.age_stat} age, {self.show_stat} show")

    _stats: "Plant.Stats"

    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name.capitalize()
        self._height = height
        self._age = age
        self._stats = self.Stats()

    @classmethod
    def anonymous_plant(cls):
        return cls("Unknown plant", 0, 0)

    @staticmethod
    def older_than_year(age):
        if age > 365:
            return True
        else:
            return False

    def show(self) -> str:
        self._stats.show_stat += 1
        return f"{self._name}: {self._height:.1f}cm, {self._age} days old"

    def grow(self, days: int = 1, rate: float = 0.8) -> None:
        self._stats.grow_stat += 1
        self._height = round(self._height + (rate * days), 1)

    def age(self, days: int = 1) -> None:
        self._stats.age_stat += 1
        self._age += days

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def set_height(self, new_height: float):
        if new_height >= 0:
            self._height = new_height * 1.0
            print(f"Height updated: {new_height}cm")
        else:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")

    def set_age(self, new_age: int):
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

    def show(self) -> str:
        text = f"{super().show()}\n Color: {self._color}"
        if self._bloomed:
            return f"{text}\n {self._name} is blooming beautifully!"
        return f"{text}\n {self._name} has not bloomed yet"


class Tree(Plant):
    class Stats(Plant.Stats):
        def __init__(self, grow_stat: int = 0,
                     show_stat: int = 0,
                     age_stat: int = 0,
                     shade_stat: int = 0):
            super().__init__(grow_stat, show_stat, age_stat)
            self.shade_stat = shade_stat

        def display(self):
            super().display()
            print(f" {self.shade_stat} shade")

    _stats: "Tree.Stats"

    def __init__(self, name: str, height: float, age: int,
                 trunk_diameter: float) -> None:
        super().__init__(name, height, age)
        self._trunk_diameter = trunk_diameter

    def show(self) -> str:
        return (f"{super().show()}"
                f"\n Trunk diameter: {self._trunk_diameter:.1f}cm")

    def produce_shade(self) -> None:
        self._stats.shade_stat += 1
        print(f"Tree {self._name} now produces a shade of "
              f"{self._height:.1f}cm long and "
              f"{self._trunk_diameter:.1f}cm wide.")

    def grow(self, days: int = 1, rate: float = 0.8) -> None:
        self._stats.grow_stat += 1
        self._height = round(self._height + (rate * days), 1)


class Vegetable(Plant):
    def __init__(self, name: str, height: float, age: int,
                 harvest_season: str,
                 nutritional_value: int) -> None:
        super().__init__(name, height, age)
        self._harvest_season = harvest_season
        self._nutritional_value = nutritional_value

    def grow(self, days: int = 1, rate: float = 0.8) -> None:
        super().grow(days, rate)
        self._nutritional_value += days

    def show(self) -> str:
        return (f"{super().show()}"
                f"\n Harvest season: {self._harvest_season}"
                f"\n Nutritional value: {self._nutritional_value}")


class Seed(Flower):
    def __init__(self, name: str, height: float, age: int, color: str,
                 bloomed: bool,
                 seeds: int = 0) -> None:
        super().__init__(name, height, age, color)
        self._seeds = seeds

    def bloom(self) -> None:
        super().bloom()
        self._seeds += 42

    def show(self) -> str:
        return f"{super().show()}\n Seeds: {self._seeds}"


def display_stats(plant: Plant) -> None:
    plant._stats.display()


def ft_garden_analytics():
    rose = Flower("rose", 15, 10, "red")
    oak = Tree("oak", 200, 365, 5)
    sunflower = Seed("sunflower", 80, 45, "yellow", False)
    anonymous = Plant.anonymous_plant()
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.older_than_year(30)}")
    print(f"Is 400 days more than a year? -> {Plant.older_than_year(400)}\n")
    print("=== Flower")
    print(rose.show())
    print("[statistics for Rose]")
    display_stats(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow(1, 8)
    rose.bloom()
    print(rose.show())
    print("[statistics for Rose]")
    display_stats(rose)
    print("\n=== Tree")
    print(oak.show())
    print("[statistics for Oak]")
    display_stats(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    print("[statistics for Oak]")
    display_stats(oak)
    print("\n=== Seed")
    print(f"{sunflower.show()}")
    print("[make sunflower grow, age and bloom]")
    sunflower.grow(20, 1.5)
    sunflower.age(20)
    sunflower.bloom()
    print(f"{sunflower.show()}")
    print("[statistics for Sunflower]")
    display_stats(sunflower)
    print("\n=== Anonymous")
    print(f"{anonymous.show()}")
    print("[statistics for Unknown plant]")
    display_stats(anonymous)


if __name__ == "__main__":
    ft_garden_analytics()
