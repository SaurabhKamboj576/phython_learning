# How to open and read a file

variable = open("file_name", "mode") #  by default the mode of open function is read
data_of_file_tobe_read = variable.read()
print(data_of_file_tobe_read)
variable.close()

# How to make new file and write into it

string_to_be_inseted = "hello i am making a new file and writing into it by using python"
variable = open("file_tobe_create","w") 
variable.write(string_to_be_inseted)
variable.close()

 # How to read line by line

f = open("file_name","r")
line = f.readline()
while (line != ""):
    print(line, type(line)) 
    line = f.readline()
f.close()

# how to read multiline

f = open("filename", "r")
lines = f.readlines()
print(lines)


# type of readlines function is list and that of readline is string

'''modes of open function
w - write 
r - read
a - append at the last of the existing file
rt - read in text
rb - read in binary

'''
# if you want not to close the file after opening then use with command:

with open("filename") as f:
    print(f.read())
