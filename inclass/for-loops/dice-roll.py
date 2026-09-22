import random
one = 0
two = 0
three = 0
four = 0 
five = 0
six = 0
for i in range(100):
	i = random.randint(1,6)
	if i == 1:
		print("1")
		one = one + 1
	if i == 2:
		print("2")
		two = two + 1
	if i == 3:
		print("3")
		three = three + 1
	if i == 4:
		print("4")
		four = four + 1
	if i == 5:
		print("5")
		five = five + 1
	if i == 6:
		print("6")
		six = six + 1
print("amount of 1's",one)
print("amount of 2's",two)
print("amount of 3's",three)
print("amount of 4's",four)
print("amount of 5's",five)
print("amount of 6's",six)

	