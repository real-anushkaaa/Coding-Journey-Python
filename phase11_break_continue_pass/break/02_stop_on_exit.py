# Take user input continuously and stop when user enters "exit". 

while True:
    text = input("write : ")
    if text == "exit":
        break
    print(text)