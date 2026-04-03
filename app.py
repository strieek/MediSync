class Pat:
    def __init__(self, name, age, cond):
        self.name = name
        self.age = age
        self.cond = cond


    def display_info(self):
        return f"Patient name is {self.name} ages {self.age} with a condition of {self.cond}"


if __name__ == "__main__":
    p1 = Pat("John", 28, "Fever")

print(p1.display_info())