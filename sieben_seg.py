#define 7 segment numbers
'''
  zero="1111110"
  one="0110000"
  two="1101101"
  three="1111001"
  four="0110011"
  five="1011011"
  six="1011111"
  sieben="1110010"
  eight="1111111"
  nine="1111011"
'''
sieb_seg=["1111110","0110000","1101101","1111001","0110011","1011011","1011111","1110010","1111111","1111011"]

#test leftN="0000110" #"1111011"
#test rightN="1101111" #"0110000"
leftN=input().split()
rightN=input().split()

leftN="".join(leftN)
rightN="".join(rightN)

def search_num(left_num,right_num):
    answer=[-1,-1]
    err=[-1,-1]
    for elem in sieb_seg:
        if left_num == elem:
            answer[0]=0
        else:
            err[0]=1
        if right_num == elem:
            answer[1]=0
        else:
            err[1]=1
    #confirm if no other hit exists
    if err[0] == 1 and answer[0] == -1:
        answer[0]=1
    if err[1] == 1 and answer[1] == -1:
        answer[1]=1
    
    if answer[0] == 0 and answer[1] == 0:
        print("Yes")
    else:
        print("No")

search_num(leftN,rightN)

LN,RN=[],[]
for num in rightN:
    RN.append(num)
for num in leftN:
    LN.append(num)

#symmetry of input   
def mirror_arr(vec):
    aux=vec[1]
    vec[1]=vec[5]
    vec[5]=aux
    aux=vec[2]
    vec[2]=vec[4]
    vec[4]=aux
    numStr=""
    for i in vec:
        numStr=numStr+i
    return numStr

#rotation of input
def rotate_arr(vec):
    aux=vec[0]
    vec[0]=vec[3]
    vec[3]=aux
    aux=vec[1]
    vec[1]=vec[2]
    vec[2]=aux
    aux=vec[4]
    vec[4]=vec[5]
    vec[5]=aux
    numStr=""
    for i in vec:
        numStr=numStr+i
    return numStr

#print(leftN,mirror_arr(LN))
#print(leftN,rotate_arr(LN))

mirrL=mirror_arr(LN)
mirrR=mirror_arr(RN)

rotL=rotate_arr(LN)
rotR=rotate_arr(RN)

search_num(mirrR,mirrL)
search_num(rotR,rotL)
