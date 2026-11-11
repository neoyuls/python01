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


def ft_garden_data():
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
