def greet(name):
     return f"hello,{name}"
age =20 #global
class Person:
       id =10 #class variable
       def __init__(self, name):
           self.name=name# local instance in this case
           
       def introduce(self):
           return f"my name is {self.name}"
person1 =Person("red")
person2 =Person('blue')

print(person1.introduce())
print(person2.introduce())

#print (person1.greet)
print(greet(person1.name))
print(greet(person2.name))
        