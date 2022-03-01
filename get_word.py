#!/usr/bin/python3.9
'''
Attempt to make "wordle" less funny.

List 5-letter words from the English dictionary.

Input only those letter marked in "grey" in <wordle>
If the last is marked as "green" can be input too.

If no input is provided, then output a random 5-letter word.
'''
import random
from english_words import english_words_set

#save only those that have 5 letters
five_letters=[]
for word in english_words_set:
  my_word=word.lower()
  if len(my_word) == 5:
    five_letters.append(my_word)

def rand_word():
  print(random.choice(five_letters))
  
def notInWordFn():
  good_words=[]
  # exclude these
  notInTheWord=input("Input letters not in the word: ").split(' ')
  for word in five_letters:
    #loop into word
    sum=0
    for item in notInTheWord:
      for letter in word:    
        if letter != item:
          sum=sum+1        
        #count = count + 1
    if sum == len(notInTheWord)*5:
      good_words.append(word)

  return good_words

def exclude_words():
  print(notInWordFn())

def endingWith():
  #it works only when good_words is not empty
  myArray=notInWordFn()
  #position and letter
  #also input letter at the end
  endWith=input("Position and letter: ").split()
  idx=0
  #print only those that end with...
  for word in myArray:
    if word[int(endWith[0])-1] == endWith[1]:
      print(word,end=" ")
      idx=idx+1
  
  print("all:",idx)

def invalid_option():
  print("Sorry, no such option")
  
menu = {"1":("Random 5-letter word",rand_word),
        "2":("Exclude these letters",exclude_words),
        "3":("List only words ending with",endingWith)
        #"4":("List words ending with but exclude these",notInWordEndsWith)
       }
for key in sorted(menu.keys()):
     print(key + " : " + menu[key][0])

ans = input("Option Number?: ")
menu.get(ans,[None,invalid_option])[1]()

#end
