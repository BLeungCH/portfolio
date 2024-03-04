def coke():
    change = 50
    while(change > 0):
        coin = input("Insert a coin (Accepted demoninations: 25, 10, 5 cents): ")
        if(coin == "25" or coin == "10" or coin == "5"):
            change -= int(coin)
        if(change <= 0):
            break
        print("Amount due: " + str(change) + " cents.")
          
    change *= -1
    print("You have paid in full. Your change is " + str(change) + " cents.")
    return

coke()