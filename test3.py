max = 1000
a = 3
b = 5

lcm = a * b
a_times = int(lcm / a)
b_times = int(lcm / b)

n = int(max / lcm)
list = []
for i in range(0,n):
	now = i * lcm
	for j in range(1,a_times + 1):
		list.append(now + j * a)
	for k in range(1,b_times):
		list.append(now + k * b)

for l in range(n * lcm+1, max):
	if l % a == 0 or l % b == 0:
		list.append(l)
print(list)


"""
list2 = []
for i in range(1,1000):
	if i % a == 0 or i % b == 0:
		list2.append(i)

print(list2)
"""