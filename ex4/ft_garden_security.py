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
        print("Plant created: ", self._name.capitalize(), ":  ",
              round(self._height, 1), "cm, ", self._age, " days old", sep="")


if (__name__ == "__main__"):
    p1 = Plant("Rose", 21.7, 10, 0.5)
    p1.set_height(15.0)
    p1.show()
