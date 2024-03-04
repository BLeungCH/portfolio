def inter():
    expr = input("Enter an arithmetic expression: ")
    x, y, z = expr.split(" ")
    ans = 0
    if(y == "+"):
        ans = float(x) + float(z)
        print("Result: " + str(ans))
    elif(y == "-"):
        ans = float(x) - float(z)
        print("Result: " + str(ans))
    elif(y == "*"):
        ans = float(x) * float(z)
        print("Result: " + str(ans))
    elif(y == "/"):
        if(z == "0"):
            print("Cannot divide by zero.")
            return
        ans = float(x) / float(z)
        print("Result: " + str(ans))
    else:
        return
    return

inter()