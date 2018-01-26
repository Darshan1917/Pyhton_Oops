#This is a classes in python demo ex:

class Employee:
    def __init__(self,firstname,lastname,salary):
        """"anything inside is the methods of the class and always starts with self and followed by arguments in init method """
        self.firstname = firstname
        self.lastname = lastname
        self.email = firstname+'.'+lastname+"@company.com"
        self.salary = salary

    def fullname(self):
        return "{} {}".format(self.firstname,self.lastname)
        # We have written a function inside the call and we can call this method to perform functions on this class values
    # Here it prints the full name



emp1 = Employee("Ravi" , "Kumar" , 40000)
emp2 = Employee("chiru", "kumar" , 39741)

print(emp1) # se the output what happens it prints an object of employee class
print(emp2)
# For an organisation or a web appliction there will be many user or employee we can use class
# to reduce the code length

print(emp1.firstname)
print (emp2.lastname)
print (emp1.email,"\n",emp2.email)

#calling fullname

print (emp1.fullname()) # NOTE here the emp1 is passed as an argument that is why we use self in the method



