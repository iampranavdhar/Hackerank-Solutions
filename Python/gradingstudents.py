# testcases=int(input())
# finalresults=[]
# lists=[5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100]
# for i in range(testcases):
#     grade=int(input())
#     if grade<38:
#         finalresults.append(grade)
#     elif grade>=38:
#         for j in range(20):
#             if abs(lists[j]-grade)<3 and lists[j]>grade:
#                 finalresults.append(lists[j])
#                 break
# print(*finalresults,sep='\n')
# 

def gradingStudents(grades):
    for i in range(len(grades)):
        if(grades[i]>37):
            if((grades[i]%5)!=0):
                if(5-(grades[i]%5)<3):
                    grades[i]+=5-(grades[i]%5)
    return (grades)
n=int(input())
grades = []
for _ in range(n):
    grades_item = int(input())
    grades.append(grades_item)
result = gradingStudents(grades)
print(result)
