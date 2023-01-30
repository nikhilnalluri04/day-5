def last(a):
	l = 0
	m = a.strip()
	for i in range(len(m)):
		if m[i] == " ":
			l = 0
		else:
			l=l+1
	return l
n=str(input("enter a string :"))
b=last(n)
print("length of last word is ",b)
