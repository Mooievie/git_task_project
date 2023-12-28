# Practical Task 1 - Award Outcomes
# Design programme to determine the award a person competing in the triathlon will receive

# Creating the variables & requesting user input
QUALIFYING_TIME = 100

swimming_time = int(input("Please enter your swimming time in minutes: "))
cycling_time = int(input("Please enter your cycling time in minutes: "))
running_time = int(input("Please enter your running time in minutes: "))

total_time = swimming_time + cycling_time + running_time
print(f"The total time you have taken to complete the triathlon is {total_time} minutes.")

# Setting the conditions for the award
if total_time <= QUALIFYING_TIME:
    print("Congratulations! You have been awarded with the provincial colours.")
elif total_time > QUALIFYING_TIME and total_time <= 105:
    print("Congratulations! You have been awarded with the provincial half colours.")
elif total_time > QUALIFYING_TIME and total_time <= 110:
    print("Congratulations! You have been awarded with the provincial scroll.")
else:
    print("You do not qualify for any awards, please try again next time.")