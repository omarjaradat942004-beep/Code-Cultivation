class Plant:
    name: str
    height: float
    ages: int
    growth: float

    def grow(self) -> None:
        self.height += self.growth

    def age(self) -> None:
        self.ages += 1

    def show(self) -> None:
        print(self.name.capitalize(), ":  ", round(self.height, 1),
              "cm, ", self.ages, " days old", sep="")


if (__name__ == "__main__"):
    index: int = 1
    p1 = Plant()
    p1.name = "rose"
    p1.height = 25.0
    p1.ages = 30
    p1.growth = 0.8
    origin_height: float = p1.height
    p1.show()
    for index in range(7):
        print("=== Day ", index, "===")
        p1.grow()
        p1.age()
        p1.show()
        index += 1
    print("Growth this week:  ", round(p1.height - origin_height, 1))
