# Paiza coding test: Rank B projects

## Project: B096 爆弾の大爆発

Time to complete: 36min

File **fill_row_col.py**

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

## Project D04 Replace "at" by "@"

File **replace_val.py**

Given a string, search for "at" word and replace it by "@" char.

### solution

Working code available [here](https://replit.com/@ndzerglink/ReplaceValue#main.py)

	input=atpaizaattest
	['a', 't', 'p', 'a', 'i', 'z', 'a', 'a', 't', 't', 'e', 's', 't']
	['@', '', 'p', 'a', 'i', 'z', 'a', '@', '', 't', 'e', 's', 't']
	output:
	@paiza@test

---
Environment:

OS: Linux Fedora 24

Language: Python3

Editor: Emacs

