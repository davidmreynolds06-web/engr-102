time_input = input("Enter the time: ")
clock_type = int(input("Choose the clock type (12 or 24): "))
char = input("Enter your preferred character: ")


# converting it to the 12 hour format if our input asked for it






is_Am_or_Pm= ""
if clock_type == 12:
    if hour == 0:
        hour = 12
        is_Am_or_Pm = "AM"
    elif hour < 12:
        is_Am_or_Pm = "AM"
    elif hour == 12:
        is_Am_or_Pm = "PM"
    else:
        hour = hour - 12
        is_Am_or_Pm = "PM"











