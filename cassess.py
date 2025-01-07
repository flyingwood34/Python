class Demo0:
    def __init__(self, name, id, age):
        self.name = name
        self.id = id
        self.age = age

    def __str__(self):
        return f"name: {self.name}, Id: {self.id}, Age: {self.age}"

    def hi(self):
        print("Say hi to the user")

# This should be correctly written as:
if __name__ == "__main__":
    print("Main class")
    
    stu1 = Demo0("Vishal", 22, 20)
    print(stu1)
12