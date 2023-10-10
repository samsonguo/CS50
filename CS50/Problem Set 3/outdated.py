months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

"""while True:
    date = input("Date: ")
    try:
        if "/" in date:
            mm, dd, yyyy = date.split("/")
        elif "," in date:
            mmdd, yyyy = date.split(", ")
            mm, dd = mmdd.split(" ")
            # No need to check if mm in months. KeyError is handled separately.
            mm = (months.index(mm)) + 1
        if int(mm) > 12 or int(dd) > 31:
            raise ValueError
    except (AttributeError, ValueError, NameError, KeyError):
        pass
    else:
        print(f"{int(yyyy)}-{int(mm):02}-{int(dd):02}")
        break"""


while True:
    date = input("Date (mm/dd/year): ").title().strip()
    try:
        month, day, year = date.split("/")
        if 1 <= int(month) <= 12 and 1 <= int(day) <= 31:
            break

    except:
        try:
            old_month, old_day, year = date.split(" ")
            for i in range(len(months)):
                if old_month == months[i]:
                    month = i + 1
            day = old_day.replace(",", "")
            if 1 <= int(month) <= 12 and 1 <= int(day) <= 31:
                break
        except:
            pass

print(f"{year}-{int(month)}-{int(day)}")

