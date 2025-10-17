import random
import statistics

print("Welcome to Dice simulation.")
print("We are gonna roll 2 dice for 1000 times.")
print("Then show you the average outcome.")
choice = input("Do you want to try? (yes/no): ").lower()

dice1_values = []
dice2_values = []

if choice == 'yes':
    for i in range(1000):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)

        dice1_values.append(dice1)
        dice2_values.append(dice2)

    average_of_dice1 = statistics.mean(dice1_values)
    average_of_dice2 = statistics.mean(dice2_values)
    ovarall_average = statistics.mean(dice1_values + dice2_values) 

    print("\n---- Average Outcome ----")
    print(f"Average outcome of first dice: {average_of_dice1:.2f}")
    print(f"Avarage outcome of second dice: {average_of_dice2:.2f}")
    print(f"Overall average: {ovarall_average:.2f}")
else:
    print("Good bye!")
         

   


