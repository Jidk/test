def anonymous(x):
	return x ** 2 + 1

def integrate(fun, start, end):
	step = 0.1
	intercept = start
	area = 0
	while intercept < end:
		intercept += step
		area += intercept ** 0.5 * step 
		#area += (intercept - step) ** 0.5 * step
	return area

print(integrate(anonymous, 0, 10))