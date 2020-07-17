# Senti-Counter

This python program accepts a path to the text file as a parameter. 
The text file contains one review per line. 
The code reads the list of positive and negative words from the positive-words.txt and negative-words.txt files and creates 2 dictionaries that includes one key for each positive and negative word that appears in the input text file.
The dictionaries then map each of these positive and negative words to the number of reviews that include it.
It includes only the words that appear right after a positive and negative word in the file.
