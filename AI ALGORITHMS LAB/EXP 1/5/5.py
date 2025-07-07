n=input("Enter a sentence : ")
m=n.split()
c=0
for i in m:
	for  j in i:
		c+=1
print("count of cahracters =  ",c)			

print("uppercase = ", n.upper())
print("lowercase = ",n.lower()) 
 
print(n.replace(" ","_"))

for i in m:
	if i.lower() == "python":
		print("python is present")
		 
