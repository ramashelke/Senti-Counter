# Senti-Counter

This python program accepts a path to the text file as a parameter. 
The text file contains one review per line. 
The code reads the list of positive words from the positive-words.txt file and creates a dictionary that includes one key for each positive word that appears in the input text file.
The dictionary then maps each of these positive words to the number of reviews that include it.
It includes only the  words that appear right after a negative word in the file.
