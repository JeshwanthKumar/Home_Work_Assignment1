# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple
N = int(input())
column = input().split()
total = 0
for i in range(N):
    Students = namedtuple('student', column) 
    ID, MARKS, NAME, CLASS= input().split()
    student = Students(ID, MARKS, NAME, CLASS)
    total += int(student.MARKS)
print(total/N)
