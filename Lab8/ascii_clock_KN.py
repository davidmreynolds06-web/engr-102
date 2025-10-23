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
 
    if period:
        line_output.append(am_pm[period][line_num])
   
 print(' '.join(line_output))