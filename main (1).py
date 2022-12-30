#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator")
bill=float(input("what was the total bill? $"))
tip = int(input("how much would you like to tip 10 , 12 , 15 ?"))
people = int(input ("How many people to pay?"))
tip_as_percentage = tip/100
total_tip_amount = bill * tip_as_percentage
total_bill = bill + total_tip_amount
bill_per_person = total_bill/people
final_amount = round(bill_per_person,2)
final_amount ="{:.2f}".format (bill_per_person)
print(f"each person should pay ${final_amount}")