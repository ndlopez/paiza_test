#input array
bomb = [["#",".","#","."],[".",".",".","."],[".",".",".","."],[".",".","#","."]]
position= []
def print_arr():
    for i in range(len(bomb)):
        for j in range(len(bomb[i])):
            print(bomb[i][j],end=" ")
        print()

for i in range(len(bomb)):
    for j in range(len(bomb[i])):
        if bomb[i][j] == "#":
               position.append(i)
               position.append(j)

print("# position:",position)
count=0
#Fill the row with "x"
for i in range(0,len(position),2):
    for j in range(len(bomb[position[0]])):
        bomb[position[i]][j] = "x"
        count = count + 1
#Fill the column with "x"
for j in range(1,len(position),2):
    for i in range(len(bomb[position[1]])):
        bomb[i][position[j]] = "x"
        if i == position[j]:
            count = count - 1
        count = count + 1
print_arr()
print(count)
