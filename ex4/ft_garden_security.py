class Plant:
    name: str
    height: float
    plant_age: int

    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name.capitalize()
        self.height = height
        self.plant_age = age

    def show(self) -> str:
        return f"{self.name}: {self.height}cm, {self.plant_age} days old"

    def grow(self):
        self.height = round(self.height + 0.8, 1)

    def age(self):
        self.plant_age += 1

    def get_height(self, newheight: float):
        if newheight < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self.height = newheight
            print(f"Height updated: {self.height}cm")

    def get_age(self, newage: int):
        if newage < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self.plant_age = newage
            print(f"Age updated: {self.plant_age} days")


def ft_garden_security() -> None:
    plant = Plant("rose", 15, 10)
    print("=== Garden Security System ===")
    print(f"Plant created: {plant.show()} \n")
    plant.get_height(25)
    plant.get_age(30)
    print()
    plant.get_height(-1)
    plant.get_age(-1)
    print()
    print(f"Current state: {plant.show()}")


if __name__ == "__main__":
    ft_garden_security()
