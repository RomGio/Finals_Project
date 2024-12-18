name = input("Enter Your Name")

am = eval(input("Enter the amount"))

am1 = am % 1000
onethou = am // 1000

am2 = am % 500
fivehun = am // 500

twohun = am // 200
am3 = am % 200
onehun = am // 100
am4 = am % 100
fifty = am // 50
am5 = am % 50
twenty = am // 20
am6 = am % 20
ten = am // 10
am7 = am % 10
five = am // 5
am8 = am % 5
two = am // 2
am9 = am % 2
one = am // 1
am10 = am % 1


print(onethou,"- 1000\n",fivehun,"- 500\n",twohun,"- 200\n",onehun,"- 100\n",fifty,"- 50\n",twenty,"- 20\n",ten,"- 10\n",five,"- 5\n",two,"- 2\n",one,"- 1\n")