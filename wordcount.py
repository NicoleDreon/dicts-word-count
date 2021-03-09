# put your code here.

# Write a program, wordcount.py, that opens a file and counts how many times each space-separated word occurs in that file. Your program should then print those counts to the screen.

# open file save as variable
# create empty dictionary save as variable
# loop through each line
# def - divide line by space .rstrip()-remove white space save list for each line 
# def - get count of words 
# put list of words and count into bucket

file = open('test.txt')
word_count = {}

# def split_lines(file):
# loop through each line in file
for line in file:
  # split each line at '' and save lists to variable words
  words = line.rsplit()
