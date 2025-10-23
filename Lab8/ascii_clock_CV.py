valid_chars="abcdeghkmnopqrsuvwxyz@$&*="  # Validate char
while char and char not in valid_chars:
    char=input("Character not permitted! Try again: ")
time_parts=time_input.split(':')   
hour=int(time_parts[0])
minute=int(time_parts[1])
hour_str=str(hour) # Convert to strings
minute_str=str(minute).zfill(2)  # add zero if needed
time_display=hour_str+':'+minute_str  # Create the time string to display