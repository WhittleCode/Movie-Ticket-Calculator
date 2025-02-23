print("Welcome to WhittleCode Movie Studio!")
q1 = input("Would you like to purchase a ticket? Y/N ").strip().upper()
if q1 == "Y":
    age = float(input("What is your age? "))
elif q1 == "N" :
     print("Thank you, please come again! ")
     exit()

if 0 <= age <= 12: 
    result = print("Price: $8.00")
elif 13 <= age < 17:
    result = print("Price: $10.00")
elif 18 <= age < 64:
    result = print("Price: $12.00")
elif 65 <= age < 150:
    result = print("Price: $6.00.")
else:
    print("Invalid age! Please enter a valid number. ")
    
print()

q2 = input("Would you like to pay cash or credit? ").strip().lower()
if q2 == "cash" :
    print("Thank you for your payment, enjoy the movie!")
if q2 == "credit" :
    print("Thank you for your payment, enjoy the movie!")