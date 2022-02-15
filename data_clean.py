#!/usr/bin/python3.9
#https://paiza.jp/challenges/513/show
#B104 Cleaning data
#started @ 17:20
people_num,questions=input().split()
data=[]
for i in range(int(people_num)):
    answers=[]
    myStr=input()
    #for j in range(int(questions)):
    answers=myStr.split(" ")
    data.append(answers)

def print_arr():
    for i in range(len(data)):
        for j in range(len(data[i])):
            print(data[i][j],end=" ")
        print()

#print_arr()

#Find elem in data <> number
#if elem <0 or elem = str: then ignore
posi=[]
for i in range(len(data)):
    for j in range(len(data[i])):
        if not data[i][j].isnumeric():
            data[i][j]="_"
            posi.append(i)
            posi.append(j)
        else:
            

print("Sort of cleaned array")
print_arr()
avg=[]
#Average remaning elements of column
for i in range(len):
