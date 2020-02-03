LA = input()
A = set(map(int,input().split()))

N = int(input())

for i in range(N):
	k = input().split()
	ktemp = set(map(int,input().split()))
	if k[0] == 'update':
		A.update(ktemp)
	elif k[0] == 'intersection_update':
		A.intersection_update(ktemp)
	elif k[0] == 'difference_update':
		A.difference_update(ktemp)
	elif k[0] == 'symmetric_difference_update':
		A.symmetric_difference_update(ktemp)
	else:
		print('Incorrect parameters')

print(sum(map(int, A)))
