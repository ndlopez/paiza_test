# Paiza coding test: Rank B projects

## Project: B096 爆弾の大爆発

Time to complete: 36min

Input desired size of 2D array (H,W).

Then, input elements of the array.

e.g.: if H=rows=4 and W=cols=4, then

      4 4
      #.#.
      ....
      ..#.
      ....

### solution

The code searches for the "#" input and saves its position (i,j) in a new array.

With that info, replace "#" and corresponding "."s by another char, say "x" in the column and row. Finally, count how many "x"s are in the modified 2D array.

Output:

	x x x x 
	x . x . 
	x x x x 
	x . x . 
	count 12

File **fill_row_col.py**

## Project D04 Replace "at" by "@"

Given a string, search for "at" word and replace it by "@" char.

### solution

Working code available [here](https://replit.com/@ndzerglink/ReplaceValue#main.py)

	input=atpaizaattest
	['a', 't', 'p', 'a', 'i', 'z', 'a', 'a', 't', 't', 'e', 's', 't']
	['@', '', 'p', 'a', 'i', 'z', 'a', '@', '', 't', 'e', 's', 't']
	output:
	@paiza@test

File **replace_val.py**

## Project B104:データのクレンジング

Given the input, result of a survey, output the average.

      N M
      s_{1,1} s_{1,2} ... s_{1,M}
      s_{2,1} s_{2,2} ... s_{2,M}
      ...
      s_{N,1} s_{N,2} ... s_{N,M}

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

Identify whether the input is a number or not with _Python's: isnumeric()_ function, then count those that meet this req and store in an 1D array, together with the sum. The result has to meet the requirements of paiza, all outputs are integers.

File: **data_clean.py**
---
Environment:

OS: Linux Fedora 24

Language: Python3

Editor: Emacs

