#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print ("Welcome to the tip calculator\n")
bill_amt = input("What was the total bill?")
tip_amt = input("what percentage tip would you like to give? 10, 12, 15?")
person_amt = input ("How many people should split the bill?")

bill_amt = float(bill_amt)
tip_amt = float (tip_amt)
person_amt = float (person_amt)
total_Bill = bill_amt + (bill_amt * (tip_amt/100))
split_amt = (total_Bill / person_amt)
#split_amt = round(split_amt),2 
#did it this way in order to learn about round function 
#Angela showed this way to format a number that is rounded but only shows one decimal place ex. 36.6 instead of 36.60. 
split_amt = "{:.2f}".format (split_amt) # fstring formatting helps keep outputs consistent. 
print (f"Each person should pay: {split_amt}" )