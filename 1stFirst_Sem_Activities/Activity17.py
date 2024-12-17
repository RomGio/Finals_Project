column = eval(input("enter the number of columns"))

for x in range(1,11):
    for y in range(1,column):
        print(f"{x} x {y} = {x * y}",end="\t")
    print()