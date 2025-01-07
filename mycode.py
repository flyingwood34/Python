class foura4:
    mft ="hod"
    def __init__(self,number,subject,classroom,name):
      self.number=number
      self.subject=subject 
      self.classroom= classroom
      self.name=name
      
    def __str__(self):
        return(f'''classinfo:
               {self.number}
               {self.subject}
               {self.classroom}
               {self.name}''')
      
myclass= foura4(70,"pfsd",132,"shivam")
myclass1= foura4(70,"cc",132,"abhishek")
print(myclass.mft)
print(myclass)
print(myclass1)


            
    