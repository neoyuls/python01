class Plant:
    name: str
    height: float
    plant_age: int

    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.plant_age = age

    def show(self) -> str:
        return f"{self.name.capitalize()}: {self.height}cm, {self.plant_age} days old"


def ft_plant_factory() -> None:
    plants = [
        Plant("rose", 25, 30),
        Plant("oak", 200, 365),
        Plant("cactus", 5, 90),
        Plant("sunflower", 80, 45),
        Plant("fern", 15, 120)
    ]

    print("=== Plant Factory Output ===")
    for plant in plants:
        print(f"Created: {plant.show()}")


if __name__ == "__main__":
    ft_plant_factory()
