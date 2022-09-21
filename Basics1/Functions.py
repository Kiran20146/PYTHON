string = "Kiran Manjunath"

#simple function to print data on the screen
def my_func():
    print(string)

my_func()   

# function with arguments 
def my_func1(fname):
    print(f"{fname} hi how are you")

my_func1("Kiran")
my_func1("Manju")
my_func1(89)

# function with multiple arguments ,a function must be called with the correct number of arguments.
def my_function1(fname, lname):
  print(fname + " " + lname)

my_function1("Emil", "Refsnes")

#If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.
#This way the function will receive a tuple of arguments,
def my_function2(*kids):
  print(f" printing all the kids name {kids} \n calling the second kid {kids[2]} " ) 

my_function2("Emil", "Tobias", "Linus")

# using key word arguments 
def my_function3(child3, child2, child1):
  print("The youngest child is " + child3)

my_function3(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

# my own program 

def my_function4(kid1,kid2,kid3):
  kid1 = input ("Enter the name of the first kid")
  kid2 = input ("Enter the name of the second kid")
  kid3 = input ("Enter the name of the third kid")
  print(f"the youngest one is {kid3}")

my_function4()  