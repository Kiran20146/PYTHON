def main():
  user_input = int(input("please provide the coins: "))
  coins(user_input) 

def coins(x):
    allowed_coins = [5,10,25]
    constant = 50
    while constant > 0:
        if x in allowed_coins:
            constant -= x
            


main()              
 