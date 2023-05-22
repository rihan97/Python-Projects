



year = int(input("Please enter a year to check? "))

divisible_by_4 = year / 4
divisible_by_100 = year / 100
divisible_by_400 = year / 400

# So a year that is divisible by 4 is a leap year (meaning no remainders), 
# but except that it is also divisible by 100 and it is no longer a leap year. 
# but unless that year also happens to be divisible by 400 then it is a leap year. 


if divisible_by_4 == int(divisible_by_4) :
    # print(f"{year} / 4 = {divisible_by_4}")
    if divisible_by_100 == int(divisible_by_100):3
        # print(f"{year} / 100 = {divisible_by_100}")
    if divisible_by_100 != int(divisible_by_100):
        print(f"{year} is a Leap year")
        if divisible_by_400 == int(divisible_by_400):
            # print(f"{year} / 100 = {divisible_by_400}")
            print(f"{year} is a Leap year")
else :
    print(f"{year} is not a leap year")
                        
