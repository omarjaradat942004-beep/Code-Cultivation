class Plant:
    name: str
    height: float
    age: int

    def show(self) -> None:
        print(self.name.capitalize(), ":  ", self.height,
              "cm, ", self.age, " days old", sep="")


if (__name__ == "__main__"):
    print("=== Garden Plant Registry ===")
    p1 = Plant()
    p2 = Plant()
    p3 = Plant()
    p1.name = "rose"
    p1.height = 25
    p1.age = 30
    p2.name = "sunflower"
    p2.height = 80
    p2.age = 45
    p3.name = "cactus"
    p3.height = 15
    p3.age = 120
    p1.show()
    p2.show()
    p3.show()
