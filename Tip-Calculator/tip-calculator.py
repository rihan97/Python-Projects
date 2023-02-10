print("Welcome to the tip Calculator!")

bill = float(input("What was the total bill? £"))

percentage_tip = int(input("What percentage tip would  you like to give? (please dont enter any % sign) "))

people = int(input("How many people do you want to split the bill with? "))

# total_bill_wtih_tip = percentage_tip / 100 * bill + bill # Could do like this OR

tip_as_percent = percentage_tip / 100
total_tip_amount = bill * tip_as_percent
total_bill_with_tip = bill + total_tip_amount
bill_per_person = total_bill_with_tip / people
# final_amount = round(bill_per_person, 2)
final_amount = "{:.2f}".format(bill_per_person) # Fixes Python format issue to two decimal places


print(f" Each person should pay: £123{final_amount}")
