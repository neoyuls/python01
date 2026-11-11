class Plant:
    name: str
    height: float
    plant_age: int

    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name.capitalize()
        self.height = height
        self.plant_age = age

    def show(self) -> str:
        return f"{self.name}: {round(1).self.height}cm, {self.plant_age} days old"

class Flower(Plant):
    color: str
    bloomed: bool

    def __init__(self, name, height: float, age, color):
        super().__init__(name, height, age)
        self.color = color
        self.bloomed = False

    def bloom(self):
        self.bloomed = True

    def show(self) -> None:
        print(f"{super().show()}\nColor: {self.color}")
        if self.bloomed is True:
            print(f"{self.name} is bloming beautifully!")
        else:
            print(f"{self.name} has not bloomed yet.")


class Tree(Plant):
    def __init__(self, name: str, height: float, age: int,
                 trunk_diameter: float):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def show(self) -> None:
        print(f"{super().show()}")
        print(f"Trunk diameter: {round(2).self.trunk_diameter}")
    def produce_shade(self):
        print(f"Tree {self.name} now produces shade of {self.height}", end="")
        print(f" and {round(2).self.trunk_diameter} wide")


def ft_plant_types() -> None:
    rose = Flower("rose", 15, 10, "red")
    oak = Tree("oak", kkk)
    print("=== Garden Plant Types ===")
    print("=== Flower")
    rose.show()
    print("[asking the rose to bloom]")
    rose.bloom()
    rose.show()
    print()
    print("=== Tree")



if __name__ == "__main__":
    ft_plant_types()
