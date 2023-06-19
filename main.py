#****************************************************************
#Name: Wing Lok LO
#Link: https://replit.com/join/eeznxchhin-lowinglokjason
#****************************************************************

#import packages
from random import randint
import statistics 
import datetime

#############
#Question #1
#############

# Create a class called Die with one attribute called sides, which defaults to 6 sides

class Die:
  def __init__(self, sides=6):
    self.sides = sides

  # Write a method inside the class called roll_die() that prints a random number between 1 and the number of sides the die has
  def roll_die(self):
    print(randint(1, self.sides))

  # write an additional method called roll_dice() which takes an input (the number of rolls) and generates the sum of the dice rolled
  def roll_dice(self, num_rolls):
    total = 0
    for i in range(num_rolls):
      total += randint(1, self.sides)
    return total

# Roll each die 10 times and save the results to a list
d6_results = [Die(6).roll_dice(1) for i in range(10)]
d10_results = [Die(10).roll_dice(1) for i in range(10)]
d20_results = [Die(20).roll_dice(1) for i in range(10)]

# Display the results for rolling each die 10 times
print("Results for rolling a 6-sided die 10 times:")
print(d6_results)
print("Results for rolling a 10-sided die 10 times:")
print(d10_results)
print("Results for rolling a 20-sided die 10 times:")
print(d20_results)

#############
#Question #2
#############

# Roll two dice 30 times and save the results to a list
d6_results_2 = [Die(6).roll_dice(2) for i in range(30)]
d8_results_2 = [Die(8).roll_dice(2) for i in range(30)]
d20_results_2 = [Die(20).roll_dice(2) for i in range(30)]

# Display the results for rolling two dice 30 times
print("Results for rolling two 6-sided dice 30 times:")
print(d6_results_2)
print("Results for rolling two 8-sided dice 30 times:")
print(d8_results_2)
print("Results for rolling two 20-sided dice 30 times:")
print(d20_results_2)

#############
#Question #3
#############
# calculate and display statistics
total_results = d6_results + d10_results + d20_results + d6_results_2 + d8_results_2 + d20_results_2
# Minimum
print("Minimum:", min(total_results))
# Maximum
print("Maximum:", max(total_results))
# Mean
print("Mean:", statistics.mean(total_results))
# Standard deviation
print("Standard deviation:", statistics.stdev(total_results))

#############
#Question #4
#############

## The datetime() class requires three parameters to create a date: year, month, and day.

# My date of birth
date_of_birth = datetime.datetime(1998, 9, 27, 0, 0, 0)

# Current time
now = datetime.datetime.now()

# Time difference between dob and now
age = now - date_of_birth

# Print out the time difference
print(f"The data time difference between my date of birth and now is {age.days} days, {age.seconds//3600} hours, and {(age.seconds//60)%60} minutes.")

#############
#Question #5
#############

# a. Write a class called InterestCalculator
class InterestCalculator:
    def __init__(self, principal, date_of_investment, annual_rate, compounding_periods):
      self.principal = principal
      self.date_of_investment = date_of_investment
      self.annual_rate = annual_rate
      self.compounding_periods = compounding_periods
  
    # b. Add a method to the class that takes a datetime object and predicts the future value at that next time
    def future_value(self, future_date):
      time_elapsed = (future_date - self.date_of_investment).days / 365
      future_value = self.principal * (1 + (self.annual_rate / self.compounding_periods))**(time_elapsed * self.compounding_periods)
      return future_value

# c. Make 2 instances of the class for two different investments
# Create two investments
investment_1 = InterestCalculator(10000, datetime.date(2022, 3, 29), 0.04, 1)
investment_2 = InterestCalculator(5000, datetime.date(2022, 3, 29), 0.023, 2)

# Calculate the future values of each investments
futureValue_1 = investment_1.future_value(datetime.date(2023, 3, 29))
futureValue_2 = investment_2.future_value(datetime.date(2023, 3, 29))

# Print each investments and current values
print(f"Investment 1:\n initial investment: ${investment_1.principal}\n date of investment: {investment_1.date_of_investment}\n annual interest rate: {investment_1.annual_rate * 100}%\n compounded once per year")
print("Current value: ${:.2f}".format(futureValue_1))

print(f"Investment 2:\n initial investment: ${investment_2.principal}\n date of investment: {investment_2.date_of_investment}\n annual interest rate: {investment_2.annual_rate * 100}%\n compounded once per year")
print("Current value: ${:.2f}".format(futureValue_2))

# Print the total investments
totalValue = futureValue_1 + futureValue_2
print("Total investments: ${:.2f}".format(totalValue))