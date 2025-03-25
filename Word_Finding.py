with open("log.html", "r") as file:
    content = file.readline()
    line_number = 1
    while (content != ""):
        if ("python" in content):
            print(f"yes python is present at line {line_number} ")
        line_number+=1
        content = file.readline()
file.close()
    
 