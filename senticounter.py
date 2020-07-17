"""
Reads a list of reviews and decide if each review is positive or negative,
based on the occurences of positive and negative words.
"""

#function that loads a lexicon of positive words to a set and returns the set
def loadLexicon(fname):
    newLex=set()
    lex_conn=open(fname)
    #add every word in the file to the set
    for line in lex_conn:
        newLex.add(line.strip())# remember to strip to remove the lin-change character
    lex_conn.close()

    return newLex

#function that reads in a file with reviews and decides if each review is positive or negative
#The function returns a list of the input reviews and a list of the respective decisions
def run(path):
    negfreq={} 
    posfreq={} 
    negCounter=0
    posCounter=0
    reviews=[]
    #load the positive and negative lexicons
    negLex=loadLexicon('negative-words.txt')
    posLex=loadLexicon('positive-words.txt')
    fin=open(path)
    for line in fin: # for every line in the file (1 review per line)
        line=line.lower().strip() 
        reviews.append(line)
        words=line.split(' ') # slit on the space to get list of words
   
        for i in range(len(words)): #for every word in the review
            if words[i] in negLex: # if the word is in the negative lexicon
                negCounter=i+1
                if negCounter+1>len(words):
                    break
                else:
                    next_word=words[i+1]
                    negfreq[next_word]=negfreq.get(next_word,0)+1
            elif words[i] in posLex:
                posCounter=i+1
                if posCounter+1>len(words):
                    break
                else:
                    next_word=words[i+1]
                    posfreq[next_word]=posfreq.get(next_word,0)+1

            
            
   
    fin.close()
    return negfreq,posfreq


if __name__ == "__main__": 
    print(run('textfile'))
       





