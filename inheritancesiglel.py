class a:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return f"name :{self.name} age :{self.age}"
    def run(self):
        pass
    
class b(a):
    def __init__(self, name, age,id,location):
        super().__init__(name, age)
        self.id=id
        self.location=location
    def run(self):
        print("running")
        
    def __str__(self):
        return super().__str__() +f" \nid: {self.id}\nlocation :{self.location}"
b1= b('rerf',33,1,"red")
print(b1)
b1.run()
        