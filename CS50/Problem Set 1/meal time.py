def main():
    time = input("What time is it? ")
    if 7 <= convert(time) <= 8:
        print("Breakfast Time")
    if 12 <= convert(time) <= 13:
        print("Lunch Time")
    if 18 <= convert(time) <= 19:
        print("Dinner Time")


def convert(time):
    hours, minutes = time.split(":")
    new_hours = float(hours)
    new_minutes = round(float(minutes)/60,2)
    time = (new_hours + new_minutes)
    return time

if __name__ == "__main__":
    main()


