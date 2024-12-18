
#Looping Stuff
Name = input(f"Write Your Name ==>")

print(f"Your walking In the Park then you Came Across a Wallet \nWhat do you do? ==>")
energy = 0
Choices = input(f"Input The Your Choice Example:Choice1,Choice2,etc ==>")

if Choices == 'Choice1':
    print("You Pick Up the Wallet Then Kept It for now for safe keeping until you can find the owner")
elif Choices == 'Choice2':
    print(f'You Just kept it for yourself')
elif Choices == 'Choice3':
    print(f'You decided to take a break')
    energy = 5

else:
  print(f'you chose to ignore it entirely')
if energy == 0:
 print('your tired from all the walking')
else:
 print('Your not tired')
print('its almost night time')