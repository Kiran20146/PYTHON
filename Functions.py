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
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")

#If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.
#This way the function will receive a tuple of arguments,

def my_function(*kids):
  print(f" printing all the kids name {kids} \n calling the second kid {kids[2]} " ) 

my_function("Emil", "Tobias", "Linus")

