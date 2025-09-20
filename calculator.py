print("Which type of calculation do you want to do?")
print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division")
calculation = input("> ")

if calculation == "1":
    print("Addition:\n")
    x = input("x: ")
    y = input("y: ")
    result = float(x) + float(y)
    print(result)

elif calculation == "2":
    print("Subtraction:\n")
    x = input("x: ")
    y = input("y: ")
    result = int(x) - int(y)
    print(result)

elif calculation == "3":
    print("Multiplication:\n")
    x = input("x: ")
    y = input("y: ")
    result = float(x) * float(y)
    print(result)

elif calculation == "4":
    print("Division:\n")
    x = input("x: ")
    y = input("y: ")
    result = float(x) / float(y)
    print(result)
