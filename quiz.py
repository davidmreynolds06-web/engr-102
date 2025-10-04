#Promt for a four digit number
usr_in = int(input("Please enter a four digit integer: "))
#separate each digit
first_dig = usr_in // 1000
sec_dig = ((usr_in -(first_dig * 1000)) // 100)
third_dig = ((usr_in -(first_dig * 1000) - (sec_dig * 100)) // 10)
fourth_dig = (usr_in - ((first_dig * 1000) - (sec_dig * 100) - (third_dig * 10)) // 1)
if (((first_dig ** 4) + (sec_dig ** 4) + (third_dig ** 4) + (fourth_dig ** 4)) == usr_in):
    print(f"{usr_in} is an Perfect plus number")
else:
    print(f"{usr_in} is not an Perfect plus number")