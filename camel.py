
userinput = input("please enter the camel case format : ")
for letter in userinput:
    if letter.isupper():
        print("_" + letter.lower(), end="")
    else:
        print(letter, end ="")    

 
       

