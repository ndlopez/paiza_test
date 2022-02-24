#!/usr/bin/ruby
=begin
Find the Area and Perimeter of an island

input:
4 4
....
.#..
..#.
....
output:
1 4
1 4
=end
H,W=gets.split(' ')
map=Array.new
aStr=""
#to avoid problems with walls
#better to extend the size of the map
k=0
newW=W.to_i
#puts newW
newW+=2
#puts newW
while k < newW
  aStr += "."
  k+=1
end
#puts aStr
map << aStr
$i=0
while $i < H.to_i
  map << gets
  map[$i+1].insert(0,".") #add . @ begin
  map[$i+1].insert(newW-1,".") #add . @end
  $i+=1
end
map << aStr
#puts map
pos=Array.new
kount=0 #area

$i=0
for elem in map do
  elem=elem.delete("\n")
  arr=elem.split('')
  $j=0
  while $j < arr.length
    if arr[$j] == "#"
      kount+=1
      pos << $i
      pos << $j
    end
    $j+=1
  end
  $i+=1
end

print pos
puts ""
def calc_perim(data,row,col)
  #map[$i].delete("\n")
  count=0
    
  if data[row-1][col]  == "." #above
    count+=1
  end
  if data[row+1][col] == "." #down
    count+=1
  end
  if data[row][col-1] == "." #right
    count+=1
  end
  if data[row][col+1] == "." #left
    count+=1
  end
  
  puts count
end
oup=pos.length/2 -1
#puts oup
for i in 0..oup
  calc_perim(map,pos[i+i],pos[i+i+1])
end
