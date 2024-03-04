def bank():
    greet = input("Enter a greeting: ")
    greet = greet.lower()
    if(greet[0:5] == 'hello'):
        print("$0")
    elif(greet[0:1] == 'h'):
        print("$20")
    else:
        print("$100")
    return

bank()