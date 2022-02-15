#input array
input_h=int(input())
input_w=int(input())
bomb=[]
for i in range(input_h):
    vec=[]    
    for j in range(input_w):
        elem=input()
        vec.append(elem)
    bomb.append(vec)

#bomb = [["#",".",".","."],[".",".",".","."],[".",".",".","."],[".",".",".","."]]
position= []
def print_arr():
    for i in range(len(bomb)):
        for j in range(len(bomb[i])):
            print(bomb[i][j],end=" ")
        print()
#Search for "#" char, save position and count 
def find_char(myChar):
    kount=0
    for i in range(len(bomb)):
        for j in range(len(bomb[i])):
            if bomb[i][j] == myChar:
                position.append(i)
                position.append(j)
                kount=kount+1
    return kount

print_arr()
print("#s: ",find_char("#"))
print("# position:",position)
#Fill the row with "x"
for i in range(0,len(position),2):
    for j in range(len(bomb[position[0]])):
        bomb[position[i]][j] = "x"

#Fill the column with "x"
for j in range(1,len(position),2):
    for i in range(len(bomb[position[1]])):
        bomb[i][position[j]] = "x"

print_arr()

print("count",find_char("x"))
