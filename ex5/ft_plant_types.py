class Plant:
    def __init__(self, name: str, height: float,
                 age: int, growth: float) -> None:
        self._name: str = name
        self._height: float = height
        self._age: int = age
        self._growth = growth
        if (self._age < 0):
            print(self._name, ":Error, age can’t be negative")
            self._age = 1
        if (self._height < 0):
            print(self._name, ":Error, height can’t be negative")
            self._height = 10

    def grow(self) -> None:
        self._height += self._growth

    def age(self) -> None:
        self._age += 1

    def set_height(self, new_height: float) -> None:
        self._height = new_height
        if (self._height < 0):
            print(self._name, ":Error, height can’t be negative ")
            print("Height update rejected")
            self._height = 10
        else:
            print("Height updated: ", self._height, "cm", sep="")

    def set_age(self, new_age: int) -> None:
        self._age = new_age
        if (self._age < 0):
            print(self._name, ":Error, age can’t be negative")
            print("Age update rejected")
            self._age = 1
        else:
            print("Age updated: ", self._age, "Days", sep="")

    def get_height(self) -> None:
        print(self._height)

    def get_age(self) -> None:
        print(self._age)

    def show(self) -> None:
        print(self._name.capitalize(), ":  ",
              round(self._height, 1), "cm, ", self._age, " days old", sep="")


class Flower(Plant):
    def __init__(self, name: str, height: float,
                 age: int, growth: float, color: str) -> None:
        super().__init__(name, height, age, growth)
        self.color = color
        self.blooms: bool = False

    def bloom(self) -> None:
        self.blooms = True

    def show(self) -> None:
        super().show()
        print("Color:  ", self.color)
        if (self.blooms):
            print("Rose is blooming beautifully!")
        else:
            print("Rose has not bloomed yet")


class Tree(Plant):
    def __init__(self, name: str, height: float,
                 age: int, growth: float, trunk_diamete: float) -> None:
        super().__init__(name, height, age, growth)
        self._trunk_diamete = trunk_diamete

    def produce_shade(self) -> None:
        print("Tree Oak now produces a shade of ", self._height,
              "cm long and ", self._trunk_diamete, "cm wide.", sep="")

    def show(self) -> None:
        super().show()
        print("Trunk diameter: ", self._trunk_diamete, "cm", sep="")


class Vegetable(Plant):
    def __init__(self, name: str, height: float,
                 age: int, growth: float, harvest_season: str) -> None:

        super().__init__(name, height, age, growth)
        self._harvest_season = harvest_season
        self._nutritional_value: int = 0

    def age(self) -> None:
        super().age()
        self._nutritional_value += 1

    def grow(self) -> None:
        super().grow()
        self._nutritional_value += 1

    def show(self) -> None:
        super().show()
        print("Harvest season: ", self._harvest_season)
        print("Nutritional value: ", self._nutritional_value)


if (__name__ == "__main__"):
    print("=== Garden Plant Types ===")
    f1 = Flower("Rose", 15.0, 10, 0.6, "red")
    print("=== Flower")
    f1.bloom()
    f1.show()
    t1 = Tree("Oak", 200.0, 365, 0.2, 1.0)
    print("=== Tree")
    t1.show()
    t1.produce_shade()
    v1 = Vegetable("Tomato", 5.0, 10, 0.4, "April")
    print("=== Vegetable")
    v1.show()
    v1.age()
    v1.age()
    v1.grow()
    v1.show()
