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
        value= item.split(":")[1]
        keys.append(key)


        # rulee checking now
        # value and num has to be into a int to check range
        if key == "iyr":
            if not value.isdigit() or int(value) < 2015 or int(value) > 2025:
                return False
        elif key == "eyr":
            if not value.isdigit() or int(value) < 2025 or int(value) > 2035:
                return False
        elif key == "hgt":
            if value.endswith("cm"):
                num = value[:-2]
                if not num.isdigit() or int(num) < 150 or int(num) > 193:
                    return False
            elif value.endswith("in"):
                num = value[:-2]
                if not num.isdigit() or int(num) < 59 or int(num) > 76:
                    return False
            else:
                return False
           








        elif key == "hcl":
            if len(value) != 7 or value[0] != "#":
                return False
            for c in value[1:]:
                if not (c.isdigit() or ("a" <= c <= "f")):
                    return False
        elif key == "ecl":
            if value not in ["amb","blu","brn","gry","grn","hzl","oth"]:
                return False
        elif key == "pid":
            if not value.isdigit() or len(value) != 9:
                return False
        elif key == "cid":
            if not value.isdigit() or len(value) != 3 or value[0] == "0":
                return False
       


    for field in required:
        if field not in keys:
            return False
    return True














def writingtofile(passport_text):




    with open("valid_passports2.txt", "a") as output:    # change filename here
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
