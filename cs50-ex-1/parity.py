def main():
    value = int(input("enter the value"))
    if is_even(value):
        print("Even")
    else:
        print("odd")



def is_even(n):
    if n%2 == 0:
        return True

main()