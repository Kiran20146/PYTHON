def main():
    us_in = input("please enter the message: ")
    twit(us_in)

def twit(message):
    vowels = ["a", "e","i","o","u", "A","E","I","O","U"]
    for letters in message:
        if letters in vowels:
            print("",end="")
        else:
            print(letters,end="")     

main()            





