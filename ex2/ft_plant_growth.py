class Plant:
    def __init__(self, name: str, height: float,
                 age: int, growth: float) -> None:
        self.name: str = name
        self.height: float = height
        self._age: int = age
        self.growth = growth

    def grow(self) -> None:
        self.height += self.growth

    def age(self) -> None:
        self._age += 1

    def show(self) -> None:
        print(self.name.capitalize(), ":  ", round(self.height, 1),
              "cm, ", self._age, " days old", sep="")


if (__name__ == "__main__"):
    index: int = 1
    p1 = Plant("Rose", 25.0, 30, 0.8)
    origin_height: float = p1.height
    p1.show()
    for index in range(7):
        print("=== Day ", index, "===")
        p1.grow()
        p1.age()
        p1.show()
        index += 1
    print("Growth this week:  ", round(p1.height - origin_height, 1))
