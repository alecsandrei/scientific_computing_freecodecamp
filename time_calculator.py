def add_time(start, duration, day=False):
    calendar = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    calendar_capital = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    start = start.split(" ")
    duration = duration.split(":")
    new_time = start[0].split(":")
    meridian = start[1]
    number_of_days = 0
    new_time[0] = int(new_time[0]) + int(duration[0])
    new_time[1] = int(new_time[1]) + int(duration[1])
    if new_time[1] >= 60:
        new_time[1] = new_time[1] % 60
        new_time[0] += 1
    if new_time[0] >= 12:
        if meridian == "AM":
            number_of_days = int(new_time[0] / 24)
            meridian = "AM" if int(new_time[0] / 12) % 2 == 0 else "PM"
        else:
            number_of_days = int((new_time[0] + 12) / 24)
            meridian = "PM" if int(new_time[0] / 12) % 2 == 0 else "AM"
        new_time[0] = new_time[0] % 12 if new_time[0] % 12 != 0 else 12
    if day is not False:
        if day.lower() not in calendar:
            print("Error: The day is considered a typo. Please try again.")
        else:
            day = day.lower()
            index = (calendar.index(day) + number_of_days) % 7
            day_of_week = calendar_capital[index]
    new_time = str(new_time[0]) + ":" + ("0" if new_time[1] < 10 else "") + str(new_time[1]) + " " + \
               meridian + \
               (f", {day_of_week}" if day else "") + \
               ((" (next day)" if number_of_days == 1 else f" ({number_of_days} days later)") if number_of_days != 0 else "")
    return new_time


print(add_time("8:16 PM", "50:25", "sunday"))
