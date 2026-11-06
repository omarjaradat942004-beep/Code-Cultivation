class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name: str = name
        self.height: int = height
        self.age: int = age

    def show(self) -> None:
        print(self.name.capitalize(), ":  ", self.height,
              "cm, ", self.age, " days old", sep="")


if (__name__ == "__main__"):
    p1 = Plant("Rose", 25, 30)
    p2 = Plant("Sunflower", 80, 45)
    p3 = Plant("Cactus", 15, 120)
    p1.show()
    p2.show()
    p3.show()
