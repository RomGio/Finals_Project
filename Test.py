number = eval(input("put The Amount"))

A = number // 1000
A_sukli = 1000 * (number - A) 
B = number // 500
B_sukli = (number - 1000)
print(f"{A} - 1000\n{B} - 500")