# Replace "at" chars of a string with "@" symbol
inStr = "atpaizaattest"
newArr = []
for elem in inStr:
  newArr.append(elem)

print(newArr)
for idx in range(len(newArr) - 1):
  if newArr[idx] == "a":
    if newArr[idx + 1] == "t":
      newArr[idx] = "@"
      newArr[idx + 1] = ""
print(newArr)
myStr=""
for elem in newArr:
  myStr = myStr + elem
print(myStr)
