def main():
    #input
    answer = input("What time is it ? ")
    time = convert(answer)
    #breakfast time between 7:00 - 8:00 
    if time >= 7 and time <= 8:
        print("breakfast time")
    elif time >= 12 and time <= 13:
        print("lunch time")
    elif time >= 18 and time <=19:
        print("Dinner time ")
    else:
        print("no food")    

def convert(time):
    # Get hour and minute 
    hours,minutes = time.split(":")
    # Convert minutes
    new_minute = float(minutes)/60
    return float(hours) + new_minute

if __name__ == "__main__":
    main()