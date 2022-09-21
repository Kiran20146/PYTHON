string = "Kiran Manjunath"
string1 = "Akasha"

age = 90
salary = 8976.555
profit = 7893

print(string[0]) 
print(len(string))
print("iran" in string)
print("akash" not in string)

print(string[2:8])
print(string[:10])
print(string[8:])
print(string[-15:-8])

print(string.upper())
print(string.lower())
print(string.strip())# removes  the white spaces only in the end left and right
print(string.replace("Kiran","Akash"))
print(string.split("n")) #split method provides the output as an list 

string3 = string[4:8].capitalize().strip().replace("M","opi" ).split("a")
print(string[2:8] + string1)
print(string3)

# we can combine  strings and numbers by using the format() method!
print(f"{profit} {salary} {age} ") # it prints the values in which order we provide the arguments
# one more method 
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price)) # 0, 1, 2 are taken from here not from the variables order 

print("hey \"kiran\" ") # escape sequence are always before of the string 
