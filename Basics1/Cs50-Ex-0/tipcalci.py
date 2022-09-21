def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = (dollars * percent)
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    flot_dollars = float(d)
    return flot_dollars
    


def percent_to_float(p):
    flot_percent = float(p) /float(100)
    return flot_percent

main()