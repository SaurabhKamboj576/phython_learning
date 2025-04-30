word = input ("Enter the word to be replaced: ")
new = input("Enter the new word to be replaced by :")
file_name = input("Enter the file name : ")
with open(file_name, "r") as file:
    content = file.read()
file.close()
if word.lower()  in content.lower():
    content_new = content.replace(word,new)
    exit
with open(file_name , "w") as file:
    file.write(content_new)
    print("word got replaced")
file.close()