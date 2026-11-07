class Plant:
    def __init__(self, name: str, height: float,
                 age: int, growth: float) -> None:
        self.name: str = name
        self.height: float = height
        self.ages: int = age
        self.growth = growth

    def grow(self) -> None:
        self.height += self.growth

    def age(self) -> None:
        self.ages += 1

    def show(self) -> None:
        print("Created: ", self.name.capitalize(), ":  ",
              round(self.height, 1), "cm, ", self.ages, " days old", sep="")


if (__name__ == "__main__"):
    print("=== Plant Factory Output ===")
    p1 = Plant("Rose", 25.0, 30, 0.8)
    p2 = Plant("Oak", 200.0, 365, 6.2)
    p3 = Plant("Cactus", 5.0, 90, 0.6)
    p4 = Plant("Sunflower", 45.0, 45, 1.5)
    p5 = Plant("Fern", 15.0, 120, 0.3)
    object_list: list[Plant] = [p1, p2, p3, p4, p5]
    for index in range(5):
        object_list[index].show()
