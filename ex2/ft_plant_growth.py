class Plant:
    name: str
    height: float
    plant_age: int

    def __init__(self, name: str, height: float, plant_age: int) -> None:
        self.name = name
        self.height = height
        self.plant_age = plant_age

    def show(self) -> str:
        cap = self.name.capitalize()
        return f"{cap}: {self.height}cm, {self.plant_age} days old"

    def grow(self):
        self.height = round(self.height + 0.8, 1)

    def age(self):
        self.plant_age += 1


def ft_plant_growth() -> None:
    rose = Plant("rose", 25.0, 30)
    day = 1
    initial = rose.height
    print("=== Garden Plant Growth ===")
    print(rose.show())
    while day <= 7:
        print(f"=== Day {day} ===")
        rose.age()
        rose.grow()
        print(rose.show())
        day += 1
    print(f"Growth this week: {round(rose.height - initial, 1)}cm")


if __name__ == "__main__":
    ft_plant_growth()
