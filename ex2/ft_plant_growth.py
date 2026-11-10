class Plant:
    name: str
    height: float
    plant_age: int

    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.plant_age = age

    def show(self):
        print(f"{self.name.capitalize()}: {self.height}cm", end="")
        print(f", {self.plant_age} days old")

    def grow(self):
        self.height = round(self.height + 0.8, 1)

    def age(self):
        self.plant_age += 1


def ft_plant_growth() -> None:
    growing_plant = Plant("rose", 25, 30)
    day = 1
    print("=== Garden Plant Growth ===")
    growing_plant.show()
    while day <= 7:
        print(f"=== Day {day} ===")
        growing_plant.age()
        growing_plant.grow()
        growing_plant.show()
        day += 1


if __name__ == "__main__":
    ft_plant_growth()
