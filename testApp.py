#made by Oleksandr Horbun

class testApp:
    print ("Hello World!")
    print ("This is testApp for a Git")

    file = open('readme.txt', 'r', encoding="utf-8")
    print("\n", file.read())
    file.close()

    print("Hello World, again!!!")
