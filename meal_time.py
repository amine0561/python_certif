import datetime

def main(): 
    time = input("What time is it? (format HH:MM) ")
    updated_time = convert(time)
    if datetime.time(7, 0) <= updated_time <= datetime.time(8, 0):
        print("Breakfast time")
    elif datetime.time(12, 0) <= updated_time <= datetime.time(13, 0):
        print("Lunch time")
    elif datetime.time(18, 0) <= updated_time <= datetime.time(19, 0):
        print("Dinner time")

def convert(time):
    hours, minutes = map(int, time.split(":"))
    return datetime.time(hours, minutes)

if __name__ == "__main__":
    main()
