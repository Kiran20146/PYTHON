def main():
    expression = (input("please enter the mathematical expression with spaces "))
    maths(expression)

def maths(exp):
    x,y,z = exp.split(" ")
    xfloat = float(x)
    zfloat = float(z)
    if y == "+" :
        print(xfloat+zfloat)
    elif y == "-" :
        print(xfloat-zfloat)
    elif y == "*" :
        print(xfloat*zfloat)
    elif y == "/" and zfloat != 0:
        print(xfloat/zfloat)
    elif y == "/" or zfloat == 0:
        print("error")
    else:
        print("error")                

main()


  

