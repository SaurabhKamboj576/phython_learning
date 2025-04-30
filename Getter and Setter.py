class Employee:
    a = 5  # Class variable

    @classmethod
    def show(cls):
        print(f"The value of class method is {cls.a}")  

    @property
    def name(self):
        return f"{self.fname} {self.lname}"

    @name.setter
    def name(self, value):
        self.fname = value.split(" ")[0] 
        self.lname = value.split(" ")[1]

# Object Creation
e = Employee()
e.a = 45  # Changes instance attribute, not class variable
e.name = "Saurabh Kamboj"  # Calls the setter

print(e.fname, e.lname)  # Output: Saurabh Kamboj
