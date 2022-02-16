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
sum,aux=[],[]
kount,count=[],[]
for i in range(int(num_questions)):
    sum.append(0)
    aux.append(0)
    kount.append(0)
    count.append(0)
#kount=[]
#print(sum,aux)
for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j].isnumeric():
            if int(data[i][j]) < 101:
                sum[j]=aux[j]+int(data[i][j])
                aux[j]=sum[j]
                count[j]=count[j]+1
                kount[j]=count[j]
        #else:
        #    data[i][j]="_"
                        
#print("Sort of cleaned array")
print(kount)

#Average remaning elements of column
for j in range(len(sum)):
    print(int(sum[j]/kount[j]))
