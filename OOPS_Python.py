class Employee:
    language = "py"
    salary = "1200000"
    def __init__(self, name , language , salary):
        self.name = name
        self.language = language
        self.salary = salary
        print("I am creating a new user")
    # self Parameter
    def getinfo(self):
        print(f"The language is {self.language} and the salary is {self.salary}")
        
    @staticmethod
    def greet():
        print("Good Morning, today you have to finish python")
    
harry = Employee("Harry","Java Script", "13000000")
print(harry.name, harry.language)
harry.getinfo()  # this way of calling the function is equals to Employee.getinfo(harry) hence require one parameter as object, which will be represented as self in the function.
# Here name is object attribute (instance attribute) while language and salary are class attribute.
# instance attribute take preference over class attributes during assignment and retrieval. 

