print("Welcome to the tip calculator")
total_bill = input("What was the total bill? $ ")
tip = input("How much tip would you like to give? 10,12 or 15? ")
num_people = input("how many people split the bill? ")

int_total_bill = float(total_bill)
int_tip = int(tip)
int_num_people = int(num_people)

percentage = int_tip / 100
total = (int_total_bill * percentage) + int_total_bill
split_total = total / int_num_people
rounded = round(split_total,2)
print(f"Each person should pay: ${rounded}")