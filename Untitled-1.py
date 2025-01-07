class std:  
       name =""
       rollno=0
def accept():
       name=(input("rnter the name"))
       rollno=(input("enter the roll no"))
       
def show(self):
       print (f"name :{self.name} roll no: {self.rollno}")
        
student =std()
student.accept()
student.show()