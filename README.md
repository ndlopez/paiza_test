# Paiza coding test: Rank B projects

## Project: B096 爆弾の大爆発

Given the position of a "#" char in the array, replace/delete the other elements in the column and row. Count the number of elements replaced/deleted in the array.

Challenge:

Input desired size of 2D array (H,W). Then, input elements of the array.

e.g.: if H=rows=4 and W=cols=5, then

      4 5
      #.#..
      .....
      ..#..
      .....

### solution

The code first searches for the "#" input and saves its position (i,j) in a new array. With that info, replace "#" and corresponding "."s by another char, say "x" in the column and row. Finally, count how many "x"s are in the modified 2D array.

Output:

	x x x x x 
	x . x . .
	x x x x x
	x . x . .
	14

File **fill_row_col.py**

## Project D04 Replace "at" by "@"

Given any word that contains "at", search for "at" word and replace it by "@" char.

### solution

Working code available [here](https://replit.com/@ndzerglink/ReplaceValue#main.py)

	atpaizaattest
	['a', 't', 'p', 'a', 'i', 'z', 'a', 'a', 't', 't', 'e', 's', 't']
	['@', '', 'p', 'a', 'i', 'z', 'a', '@', '', 't', 'e', 's', 't']
	
	@paiza@test

File **replace_val.py**

## Project B104:データのクレンジング

Given the input, output the average.

N M

|s_{1,1} |s_{1,2}| ... |s_{1,M}|
|s_{2,1} |s_{2,2}| ... |s_{2,M}|
|...|||
|s_{N,1} |s_{N,2}| ... |s_{N,M}|

Where: N= number of surveyed people, M = number of questions,
s_{i,j} answer (number, string). If s_{i,j} > 100 should be considered as string. The result should be the average of the input numbers.

e.g: Input

	5 3
	80 -50 30
	90 50 xxx
	120 40 50
	40 90 90
	50 1 80

Output:

	65
	45
	62

### solution

Identify whether the input is a number or not with Python's: _isnumeric()_ function, then count those that meet this requirement and store them in a 1D array, together with the accumulated sum. The result meets the requirements of paiza, all outputs are integers.

File: **data_clean.py**

## Project B015 7-segment display

Representation of a number in a 7-segment display.

	- 1 -
	1 - 1
	- 0 -	represents number "0"
	1 - 1
	- 1 -

index position:           

	- 1 -
	6 - 2
	- 7 -
	5 - 3
	- 4 -

The user will input as:
 
	1 1 1 1 1 1 0

Challenge

Given two user inputs return "Yes" or "No" for the following cases:

1. Both inputs must represent numbers in the 7-segment display.
2. By mirroring their positions they both must represent numbers.
3. By rotating their positions they both must represent numbers.

### Example
Input: 

	0 0 0 0 1 1 0
	1 1 0 1 1 1 1

Output:	
	No
	Yes
	No

### solution

First, list all the numbers (0~9), in text format, in an array. Then build a function to make string comparison and return "Yes"/"No" depending of the match. Next, mirror the positions and call the function that finds the match and return the answer. Finally, build another function to rotate the positions and return also the answer. 

File **sieben_seg.py**

### Result from paiza.jp

Click [here](https://prnt.sc/4aSQXTvrxXpb) to see score.

## B032:デジタル計算機

そろばんでの足し算をシミュレーションするプログラムを書

Based on the input (size of object) build a digital abaqus to add up two numbers.

Input:

	6
	**|***
	||*|||
	======
	*|*|*|
	****|*
	******
	**|***
	|*****
	**|***
	||*|||
	======
	||*|*|
	****|*
	******
	**|***
	******

Output:

	**|***
	||*|||
	======
	***|*|
	*||***
	****|*
	******
	|*****
## solution

Currently working on the algorithm. Since I have never used an abaqus, I don't know how this thing works. Better check [Wikipedia](https://ja.wikipedia.org/wiki/%E3%81%9D%E3%82%8D%E3%81%B0%E3%82%93).

---
Environment:

OS: Linux Fedora 24

Language: Python3

Editor: Emacs

