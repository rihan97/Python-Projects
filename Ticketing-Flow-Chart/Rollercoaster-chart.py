print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))



if height >= 120:
    print("You are allowed on the rollercoaster")
    age = int(input("How old are you? "))
    if age < 12:
        print("You will be charged £5")
    elif age <= 18:
        print("You will be charged £7")
    else:
        print("You will be charged £12")
else:
    print("you do not meet the height requirements")

