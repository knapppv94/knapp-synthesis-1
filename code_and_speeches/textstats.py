# Paige Knapp, pvk8@pitt.edu, January 19 2017

rose = 'Rose is a rose is a rose is a rose.'

fox = """Through three cheese trees three free fleas flew.
While these fleas flew, freezy breeze blew.
Freezy breeze made these three trees freeze."""

tale = """It was the best of times, it was the worst of times,
it was the age of wisdom, it was the age of foolishness,
it was the epoch of belief, it was the epoch of incredulity,
it was the season of Light, it was the season of Darkness,
it was the spring of hope, it was the winter of despair,
we had everything before us, we had nothing before us,
we were all going direct to heaven, we were all going direct
the other way.""" 


def getTokens(txt):
    """Takes a piece of text (a single string) as the argument.
    Returns a list of tokenized words.
    Symbols are separated out, and upper case is lowered.
    """
    sym = "~!@#$%^&*()_+-=`{}[]|\\:;\"',./<>?"
    new = txt.lower()
    for s in sym :
        new = new.replace(s, " "+s+" ")
    return new.split()


def getTypeFreq(txt):
    """Takes a piece of text (a single string) as the argument.
    Returns a frequency count dictionary.
    KEY is a word, VALUE is its frequency count.
    """
    # [1] Complete this function. YOUR CODE BELOW.
    # Use getTokens().

    freq = {}
    for w in getTokens(txt):
        if w in freq:
            freq[w] += 1
        else:
            freq[w] = 1
    return freq


def getTypes(txt):
    """Takes a piece of text (a single string) as the argument.
    Returns an alphabetically sorted list of unique word types.
    """ 
    # [2] Complete this function. YOUR CODE BELOW. 
    # Use getTypeFreq().

    new = sorted(getTypeFreq(txt).keys())

    return new


def getXLengthWords(wtypes, x):
    """Takes a list of unique words (= word types) and integer x as
    arguments. Returns a sorted list of words whose length is at least x.
    """
    # [3] Complete this function. YOUR CODE BELOW.   

    xlenwords = []
    for w in wtypes:
        if len(w) >= x:
            xlenwords.append(w)
    
    return sorted(xlenwords)


def getXFreqWords(freqdi, x):
    """Takes a word frequency dictionary and integer x as arguments.
    Returns a sorted list of words that are at least x in frequency.
    """
    # [4] Complete this function. YOUR CODE BELOW.

    xFreqWords = []
    for (k,v) in freqdi.items():
        if v >= x:
            xFreqWords.append(k)
    
    return sorted(xFreqWords)


def foxDemo():
    "A void function that demonstrates how the functions are used."
    foxtoks = getTokens(fox)      # Function-internal objects:
    foxtypes = getTypes(fox)      #   not accessible from IDLE shell!
    foxfreq = getTypeFreq(fox)    # You can however retrace the steps 
                                  #   to re-create these objects. 
    print('There are', len(foxtoks), 'word tokens in fox.')
    print('There are', len(foxtypes), 'unique word types in fox.')
    print('The word "freezy" occurs', foxfreq['freezy'], 'times.')

    len6 = getXLengthWords(foxtypes, 6)
    freq3 = getXFreqWords(foxfreq, 3)

    print('Words that are at least 6-characters long: ')
    for w in len6 :
        print(' ', "'"+w+"'", 'has', len(w), 'chars.')

    print('Words with 3 or higher frequency: ')
    for w in freq3 :
        print(' ', "'"+w+"'", 'occurs', foxfreq[w], 'times.')



# [5] Have your script process tale and print out the following.
# How many word tokens it has,
# How many word types it has,
# How many times 'was' occurs in the text,
# Words that are at least 10 characters long,
# Words that occur at least 10 times,
# And finally, *EVERY WORD TYPE* in tale followed by its frequency count. 
# YOUR CODE BELOW.
def main():
    taletoks = getTokens(tale)
    taletypes = getTypes(tale)
    talefreq = getTypeFreq(tale)

    len10 = getXLengthWords(taletypes, 10)
    freq10 = getXFreqWords(talefreq, 10)

    print('There are', len(taletoks), 'word tokens in tale.')

    print('There are', len(taletypes), 'unique word types in tale.')

    print('The word "was" occurs', talefreq['was'], 'times.')

    print('Words that are at least 10-characters long: ')
    for w in len10:
        print(' ', "'"+w+"'", 'has', len(w), 'chars.')

    print('Words with 10 or higher frequency: ')
    for w in freq10:
        print(' ', "'"+w+"'", 'occurs', talefreq[w], 'times.')

    for (k, v) in talefreq.items():
        print('"'+k+'" has a frequency of', str(v)+".")

if __name__ == '__main__':
    main()


def getnGrams(txt, n):
    "Takes in a list of tokens and number for grams, returns list of tuples."
    ngrams = []
    for i in range(len(txt)-(n-1)):
        gram = txt[i:i+n]
        ngrams.append(tuple(gram))
    return ngrams

def getFreq(li):
    "Takes a list as input, returns a dictionary of frequency count."
    di = {}
    for x in li:
        if x not in di: di[x] = 1
        else: di[x] += 1
    return di
