# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name:  Deep Patel
#        Chris Voelkel
#        Karl Nolte
#        David Reynolds
# Section: 412
# Assignment: Lab Topic 11
# Date: 5 November 2025


def check(passport_list):
    required = ['eyr', 'hcl', 'hgt', 'iyr', 'ecl', 'cid', 'pid']


    keys = []
    for item in passport_list:
        key = item.split(":")[0]
        keys.append(key)


    for field in required:
        if field not in keys:
            return False


    return True




def writingtofile(passport_text):


    with open("valid_passports.txt", "a") as output:
        for line in passport_text:
            output.write(line)
        output.write("\n")




def evaluate(filename):


    check_list = []
    passport_text = []
    valid = 0


    with open(filename, "r") as myfile:
        for line in myfile:


            if line.strip() == "":


                if check(check_list):
                    valid += 1
                    writingtofile(passport_text)  # style comment


                check_list = []
                passport_text = []


            else:
                passport_text.append(line)
                for item in line.split():
                    check_list.append(item)


        if check_list:
            if check(check_list):
                valid += 1
                writingtofile(passport_text)


    return valid




filename = input("Enter the name of the file: ")
print(f"There are {evaluate(filename)} valid passports")
