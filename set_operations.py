#SET UNION

eng_num = int(input())
eng_set = set(map(int, input().split()))
fren_num = int(input())
fren_set = set(map(int, input().split()))

print(len(eng_set.union(fren_set)))


#SET DIFFERENCE

eng_num = int(input())
eng_set = set(map(int, input().split()))
fren_num = int(input())
fren_set = set(map(int, input().split()))

print(len(eng_set.difference(fren_set)))

#SET INTERSECTION

eng_num = int(input())
eng_set = set(map(int, input().split()))
fren_num = int(input())
fren_set = set(map(int, input().split()))

print(len(eng_set.intersection(fren_set)))

#SYMMETRIC DIFFERENCE

eng_num = int(input())
eng_set = set(map(int, input().split()))
fren_num = int(input())
fren_set = set(map(int, input().split()))

print(len(eng_set.symmetric_difference(fren_set)))
