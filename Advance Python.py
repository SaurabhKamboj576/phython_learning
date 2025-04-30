# Walrus Operator 
if (n := len([1,2,3,4,5]))>3:
    print(f"The list can contian only 3 number but containing {n}")

# Type definition : for declaring the type of the  variable and also the return type of the function sothat programmer can code efficiently

n : int = 5

def sum(a:int, b:int)-> int:
    return a+b

from typing import List, Tuple , Dict , Union

n : list[int] = [1,2,3,4,5]
person : Tuple[str , int] = ("Saurabh", 22)
scores : Dict[str , int] = {"Saurabh": 98, "Gurjot":99}
identity : Union[str , int] = "IDR123"
identity = 1234

# Match case
 
def check_day(day):
    match day.lower():
        case "monday":
            return "Start of the workweek!"
        case "friday":
            return "Weekend is near!"
        case "saturday" | "sunday":
            return "It's the weekend!"
        case _:
            return "It's a regular day."

print(check_day("Friday"))   # Output: Weekend is near!
print(check_day("Sunday"))   # Output: It's the weekend!
print(check_day("Wednesday"))  # Output: It's a regular day.

 # Global Keyword
a = 89
def mydef():
    global a
    a = 3
    print(a)
mydef()
print(a)

# List Comprehension

list = [1,2,3,4,5,6,7,8,9]
squaredlist = [i*i for i in list]
print(squaredlist)


# enumerate Function 

list = [1,2,3,4,5,6]
for i,j in enumerate(list):
    print(f"The number at index{i} is {j}")
    