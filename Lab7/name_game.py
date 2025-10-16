x = input("What is your name? ")
Vow = "AEIOUYaeiouy"

if x[0].upper() in Vow:
    y =x[0].lower() + x[1:]
    print(x + ", " + x + ", Bo-B" + y + "\nBanana-Fana Fo-F" + y + "\nMe-Mi-Mo-M" + y + "\n" + x + "!")
else:
    if x[1].lower() in Vow:
        y = x[1:].lower()
        print(x + ", " + x + ", Bo-B" + y + "\nBanana-Fana Fo-F" + y + "\nMe-Mi-Mo-M" + y + "\n" + x + "!")
    else:
        if x[2].lower() in Vow:
            y = x[2:].lower()
            print(x + ", " + x + ", Bo-B" + y + "\nBanana-Fana Fo-F" + y + "\nMe-Mi-Mo-M" + y + "\n" + x + "!")
        else:
            y = x[3:].lower()
            print(x + ", " + x + ", Bo-B" + y + "\nBanana-Fana Fo-F" + y + "\nMe-Mi-Mo-M" + y + "\n" + x + "!")
# Name Game
# Lab 7