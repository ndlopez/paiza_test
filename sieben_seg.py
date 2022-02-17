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

leftN="1111011"
rightN="0110000"

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

#symmetry rotation of input
#leftN[2] <-> leftN[6], leftN[3] <-> leftN[5]
#rightN <-> leftN
#convert str to arrays
LN,RN=[],[]
for num in rightN:
    RN.append(num)
for num in leftN:
    LN.append(num)
    
aux=RN[1]
RN[1]=RN[5]
RN[5]=aux
aux=RN[2]
RN[2]=RN[4]
RN[4]=aux
print(rightN,RN)
