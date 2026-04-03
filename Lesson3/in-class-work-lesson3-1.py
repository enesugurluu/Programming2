# 1. Bug Collector
# A bug collector collects bugs every day for five days.
# Write a program that keeps a running total of the number of bugs collected during the five days.
# The loop should ask for the number of bugs collected for each day, and when the loop is finished, the program should display the total number of bugs collected.


total_bug = 0
for day in range(5):
    total_bug += int(input(f"Enter the bug count for {day+1}. day? "))

print(f"Total bug count: {total_bug}")
