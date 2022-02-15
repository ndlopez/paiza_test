#input array
#mines = [["#",".",".","."],[".",".",".","."],[".",".",".","."],[".",".",".","."]]

#Paiza's input format
input_h,input_w=input().split(" ")

mines=[]
for i in range(int(input_h)):
    vec=[]    
    #for j in range(int(input_w)):
    vec=input().split()
    mines.append(vec)

position= []
def print_arr():
    for i in range(len(mines)):
        for j in range(len(mines[i])):
            print(mines[i][j],end=" ")
        print()
#Search for "#" char, save position and count 
def find_char(myChar):
    kount=0
    for i in range(len(mines)):
        for j in range(len(mines[i])):
            if mines[i][j] == myChar:
                position.append(i)
                position.append(j)
                kount=kount+1
    return kount

#print_arr()
print("#s: ",find_char("#"))
print("# position:",position)
#Fill the row with "x"
for i in range(0,len(position),2):
    for j in range(len(mines[position[0]])):
        mines[position[i]][j] = "x"

#Fill the column with "x"
for j in range(1,len(position),2):
    for i in range(len(mines[position[1]])):
        mines[i][position[j]] = "x"

print_arr()

print("count",find_char("x"))
