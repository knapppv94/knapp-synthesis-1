import nltk

f = open('franco_speeches.txt', encoding = 'utf-8')
ftxt = f.read()
f.close()

ftoks = nltk.word_tokenize(ftxt)

fText = nltk.Text(ftoks)

fText.dispersion_plot(['Spain', 'state', 'nation', 'authority', 'citizens', 'liberal', 'conservative', 'politics', 'immigration', 'race', 'economy'])
