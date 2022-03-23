#A program to test for eligibility for a roller coaster ride and the right payement
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? \n"))
#testing of requirements
if height >= 120:
  print("Cool, you can ride on!")
  #asking for age with a nested if so that the user knows how much to pay
  age = int(input("Please enter your age\n"))
  if age < 12:
     print("Please pay 500francs for the ride")
  elif age < 18:
    print("Please pay 700francs for the ride")
  elif age > 18:
    print("Please pay a 1000francs for the ride")
else:
  print("Sorry, you can't have a ride")

