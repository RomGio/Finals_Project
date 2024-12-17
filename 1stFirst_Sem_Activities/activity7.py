#introduction to conditional statements

gold = 0
miner = input("Hi, what is the name : ")

isGold = input("is the mineral gold ? ")

# if yes is not in lower case the program will then proceed with the else statement

if isGold.lower() == "yes":
	gold += 1
	print(f"Hi {miner}, your total of gold is {gold}")

else:
	print(f"Hi {miner}, your total of gold is {gold}")

