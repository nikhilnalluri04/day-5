def minsqr(n):
	if n <= 3:
		return n;
	res = n
	for x in range(1, n+1):
		temp = x * x;
		if temp > n:
			break
		else:
			res = min(res, 1 + minsqr(n - temp))
	return res;

n = int(input("enter the number:"))
print("Minimum square :",minsqr(n))
