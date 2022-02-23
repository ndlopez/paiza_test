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
H,W=gets
thisArr=""
map=Array.new
$i=0
while $i < H.to_i
  map << gets
  $i+=1
end

#puts map
#print H,W
#=begin
for elem in map do
  arr=elem.split('')
  print arr
  #for jdx in arr do
    #if elem == "#" 
  #  puts "Found a #"
  #end
  #end
end
