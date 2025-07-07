n=int(input("Enter mark : "))

if n >= 90:
	print("Grade A")
elif n >= 75 and n < 90:
	print("Grade B")
elif n >= 60 and n < 75:
	print("Grade C")
elif n >= 40 and n < 60:
	print("Grade D")
else:
	print("Fail")		
