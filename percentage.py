#You have a record of  students. Each record contains the student's name, and their percent marks in Maths, Physics and Chemistry. 
#The marks can be floating values. The user enters some integer  followed by the names and marks for  students. 
#The user then enters a student's name. Output the average percentage marks obtained by that student, correct to two decimal places.
#You are required to save the record in a dictionary data type. 

N = int(input())
ans = {}
for i in range(N):
    g = input().split(' ')
    ans[g[0]] = [float(x) for x in g[1:]]
student = input()
print "%.2f" %(sum(ans[student])/len(ans[student]))
