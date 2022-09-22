def main():
    greet_mesg = input("please greet your message ").strip()
    greet(greet_mesg)
    
    
def greet(mesg):
    if mesg == "hello" or mesg == "Hello" in mesg:
        print("you have received $0")
    elif mesg[0] == "h" or mesg[0] == "H":
        print("you have received $10")
    else :
        print("you have received $100")

main()        


