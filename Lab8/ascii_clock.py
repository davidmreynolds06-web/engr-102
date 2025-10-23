# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."


# Name:  Deep Patel
#        Chris Voelkel
#        Karl Nolte
#        David Reynolds
# Section: 412
# Assignment: Lab Topic 8 ascii clock
# Date: 22 October 2025




# Dictionary for digits (using * as placeholder)
digits = {
    '0': ["***", "* *", "* *", "* *", "***"],
    '1': [" * ", "** ", " * ", " * ", "***"],
    '2': ["***", "  *", "***", "*  ", "***"],
    '3': ["***", "  *", "***", "  *", "***"],
    '4': ["* *", "* *", "***", "  *", "  *"],
    '5': ["***", "*  ", "***", "  *", "***"],
    '6': ["***", "*  ", "***", "* *", "***"],
    '7': ["***", "  *", "  *", "  *", "  *"],
    '8': ["***", "* *", "***", "* *", "***"],
    '9': ["***", "* *", "***", "  *", "***"]
}
# Dictionary for colon
colon = [" ", ":", " ", ":", " "]
# Dictionary for AM/PM
am_pm = {
    'AM': [" A  M   M", "A A MM MM", "AAA M M M", "A A M   M", "A A M   M"],
    'PM': ["PPP M   M", "P P MM MM", "PPP M M M", "P   M   M", "P   M   M"]
}


time_input = input("Enter the time: ")
clock_type = int(input("Choose the clock type (12 or 24): "))
char = input("Enter your preferred character: ")


valid_chars="abcdeghkmnopqrsuvwxyz@$&*="  # Validate char
while char and char not in valid_chars:
    char=input("Character not permitted! Try again: ")




valid_chars="abcdeghkmnopqrsuvwxyz@$&*="  # Validate char
while char and char not in valid_chars:
    char=input("Character not permitted! Try again: ")


time_parts=time_input.split(':')  
hour=int(time_parts[0])
minute=int(time_parts[1])


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




hour_str=str(hour) # Convert to strings
minute_str=str(minute).zfill(2)  # add zero if needed
time_display=hour_str+':'+minute_str  # Create the time string to display


for line_num in range(5):
    line_output = []
   
    for char_in_time in time_display:
        if char_in_time == ':':
            line_output.append(colon[line_num])
        else:
            digit_pattern = digits[char_in_time][line_num]
           
            if char:
                digit_pattern = digit_pattern.replace('*', char)
            else:
                digit_pattern = digit_pattern.replace('*', char_in_time)
           
            line_output.append(digit_pattern) # style comment
 
    if is_Am_or_Pm:
        line_output.append(am_pm[is_Am_or_Pm][line_num])
   
    print(' '.join(line_output))
