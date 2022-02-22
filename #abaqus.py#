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
NUM=["*|=|****","*|=*|***","*|=**|**","*|=***|*","*|=****|","|*=|****","|*=*|***","|*=**|**","|*=***|*","|*=****|"]
w=int(input()) #abaqus width, figure size
EIGHT=8
auxNum=[]
for k in range(2):#2 sets of numbers
    newArr=[]
    for i in range(w):
        newArr.append("")

    for j in range(EIGHT):
        inStr=input() # **|***
        for i in range(w):
            aux=newArr[i]
            newArr[i]=aux+inStr[i]

    buildNum=""
    for j in range(len(newArr)):
        for i in range(len(NUM)):
            if newArr[j] == NUM[i]:
                buildNum = buildNum + str(i)

    auxNum.append(buildNum)

#add up elements
sum=0
for number in auxNum:
    sum = sum + int(number)

auxNum=[]
for i in str(sum):
    auxNum.append(i)
#print("Sum: ",auxNum)
newArr=[]
for number in auxNum:
    myStr=NUM[int(number)]
    newArr.append(myStr)

#format result
for i in range(eight):
    auxStr=""
    for elem in newArr:
        auxStr=auxStr + elem[i]
        
    print(auxStr)
