#!/usr/bin/python3.9
'''
https://plus.maths.org/content/defying-gravity-uphill-roller

B032 Build Digital Abaqus
そろばんでの足し算をシミュレーションする
プログラムを書いてみましょう
Define numbers as columns
From Wikipedia:
0 1 2 3 4 5 6 7 8 9

1 1 1 1 1 0 0 0 0 0
0 0 0 0 0 1 1 1 1 1
= = = = = = = = = =
0 1 1 1 1 0 1 1 1 1
1 0 1 1 1 1 0 1 1 1
1 1 0 1 1 1 1 0 1 1
1 1 1 0 1 1 1 1 0 1
1 1 1 1 0 1 1 1 1 0
'''
num=["10=01111","10=10111","10=11011","10=11101","10=11110","01=01111","01=10111","01=11011","01=11101","01=11110"]
w=6 #int(input()) #width of abaqus, 6 digits
eight=8
auxNum=[]
for k in range(2):#2 sets of numbers
    newArr=[]
    for i in range(w):
        newArr.append("")

    for j in range(eight):
        inStr=input() #"110111"
        for i in range(w):
            aux=newArr[i]
            newArr[i]=aux+inStr[i]

    buildNum=[]
    for j in range(len(newArr)):
        for i in range(len(num)):
            if newArr[j] == num[i]:
                buildNum.append(i)

    auxNum.append(buildNum)

print(auxNum)
newStrArr=[]
jdx=0
for item in auxNum:
    for i in item:
        aux=i
        newStrArr[jdx]=aux
    jdx=jdx+1

print(newStrArr)
