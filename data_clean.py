#!/usr/bin/python3.9
#https://paiza.jp/challenges/513/show
#B104 Cleaning data
#started @ 17:20
num_people,num_questions=input().split()
data=[]
#data=[[20,15],[19,"foo"],[-20,30]]
for i in range(int(num_people)):
    answers=[]
    myStr=input()
    #for j in range(int(num_questions)):
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
sum,aux,vec=[],[],[]
for i in range(int(num_questions)):
    sum.append(0)
    aux.append(0)
    vec.append(0)
kount=[]
#print(sum,aux)
for i in range(len(data)):
    for j in range(len(data[i])):
        if not data[i][j].isnumeric():
            data[i][j]="_"
            kount.append(j)
            
        else:
            sum[j]=aux[j]+int(data[i][j])
            aux[j]=sum[j]
                        
#print("Sort of cleaned array")
print(kount)
count=0
for i in range(len(kount)):
    for j in range(len(sum)):
        aux[j],count=0,0
        if kount[i] == j:
            count=count+1
            vec[j]=aux[j]+count
            aux[j]=vec[j]
        
#print_arr()
for j in range(len(sum)):
    if kount[j] == j:
        print(sum[j]/(int(num_people)-kount[0]))
    else:
        print(sum[j]/int(num_people))
#Average remaning elements of column
