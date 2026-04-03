# 12. Population
# Write a program that predicts the approximate size of a population of organisms.
# The application should prompt the user to enter the starting number of organisms, the average daily population increase (as a percentage), and the number of days the organisms will be left to multiply.
# For example, assume the user enters the following values:
# Starting number of organisms: 2
# Average daily increase: 30%
# Number of days to multiply: 10


Starting_number_of_organisms = 2
Average_daily_increase = 0.3
Number_of_days_to_multiply = 10

final_number_of_organisms = Starting_number_of_organisms

print(f"Day 1: {final_number_of_organisms}")

for day in range(2,Number_of_days_to_multiply+1):
    final_number_of_organisms *= Average_daily_increase + 1
    print(f"Day {day}: {final_number_of_organisms:.4f}")

