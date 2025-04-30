'''
Single Inheritance :
In single inheritance, a child class inherits from a single parent class. The child class gets all the properties and methods of the parent class.
'''
# Creation of Parent Class
class Employee:
    def __init__(self, name, company, position, language):
        self.name = name
        self.company = company
        self.position = position
        self.language = language
        
    def show(self):
        print(f"The name of the employee is {self.name}, who is working in {self.company} as {self.position}, and their preferred language is {self.language}.")

# Creating Employee objects
employee_1 = Employee("Saurabh Kamboj", "Google", "Cloud Engineer", "Python")
employee_2 = Employee("Rahul Kamboj", "Amazon", "Data Analyst", "Python")

# Creation of Child class (Inheritance Class)
class Programmer(Employee):
    def __init__(self, name, company, position, language, project):
        # Call the Parent Class Constructor
        # super() is a built-in Python function used to call a method from the parent class. It allows the child class to access methods and attributes from the parent class.
        super().__init__(name, company, position, language)
        self.project = project

    def programmer_info(self):
        print(f"The name of the programmer is {self.name}, working at {self.company} as a {self.position}, using {self.language}, and currently working on the project '{self.project}'.")

# Creating a Programmer object
Programmer_1 = Programmer("Rahul Kamboj", "Amazon", "Data Analyst", "Python", "Data Analysis")
Programmer_1.show()

'''
Multiple Inheritance:
In multiple inheritance, a child class inherits from two or more parent classes. This allows the child class to inherit attributes and methods from multiple classes.
'''

# Parent Class 1: Employee
class Employee:
    def __init__(self, name, company):
        self.name = name
        self.company = company

    def show_employee_info(self):
        print(f"Employee: {self.name} works at {self.company}")

# Parent Class 2: Programmer
class Programmer:
    def __init__(self, language):
        self.language = language

    def show_programming_language(self):
        print(f"Programmer works with {self.language}.")

# Child Class: Developer (inherits from both Employee and Programmer)
class Developer(Employee, Programmer):
    def __init__(self, name, company, language, project):
        # Initialize both parent classes
        Employee.__init__(self, name, company)  # Initialize Employee class
        Programmer.__init__(self, language)  # Initialize Programmer class
        self.project = project

    def developer_info(self):
        print(f"Developer {self.name} is working on the project: {self.project}")

# Creating an object of the Developer class
developer_1 = Developer("Rahul Kamboj", "Amazon", "Python", "Data Analysis Project")
developer_1.show_employee_info()  # From Employee class
developer_1.show_programming_language()  # From Programmer class
developer_1.developer_info()  # From Developer class


'''
Multilevel Inheritance:
In multilevel inheritance, a class inherits from another class, which in turn inherits from a third class. This forms a chain of inheritance.

'''
# Parent Class: Employee
class Employee:
    def __init__(self, name, company):
        self.name = name
        self.company = company

    def show_employee_info(self):
        print(f"Employee: {self.name} works at {self.company}")

# Child Class 1: Programmer (inherits from Employee)
class Programmer(Employee):
    def __init__(self, name, company, language):
        super().__init__(name, company)  # Call the Parent Class constructor
        self.language = language

    def show_programming_language(self):
        print(f"Programmer works with {self.language}.")

# Child Class 2: Senior Programmer (inherits from Programmer, and thus also from Employee)
class SeniorProgrammer(Programmer):
    def __init__(self, name, company, language, years_of_experience):
        super().__init__(name, company, language)  # Call the Programmer class constructor
        self.years_of_experience = years_of_experience

    def show_experience(self):
        print(f"{self.name} has {self.years_of_experience} years of experience.")

# Creating an object of the SeniorProgrammer class
senior_programmer = SeniorProgrammer("Saurabh Kamboj", "Google", "Python", 5)
senior_programmer.show_employee_info()  # From Employee class
senior_programmer.show_programming_language()  # From Programmer class
senior_programmer.show_experience()  # From SeniorProgrammer class
