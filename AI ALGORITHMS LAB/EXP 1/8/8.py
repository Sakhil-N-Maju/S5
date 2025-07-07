x=float(input("Enter number 1 : "))
y=float(input("Enter number 2 : "))

while True:
	n=input("Enter the operation \n1) ADDITION \n2)SUBTRACTION\n3)MULTIPLICATION\n4)DIVISION\n5)EXIT\n")
	if n == "1":
		print(x+y)
	elif n == "2":
		print(x-y)
	elif n == "3":
		print(x*y)
	elif n == "4":
		print(x/y)
	elif n == "5":
		print("Exit")
		break
	else:
		print("invalid entry")	
		
