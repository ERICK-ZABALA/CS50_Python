expresion = str(input("Operation:"))
x, y, z = expresion.split()
# print(expresion.split())

match y:
    case "+":
        print(float(x) + float(z))
    case "-":
        print(float(x) - float(z))
    case "*":
        print(float(x) * float(z))
    case "/":
        print(float(x) / float(z))


