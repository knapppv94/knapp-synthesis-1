import nltk

f = open('trump_speeches.txt', encoding = 'utf-8')
ttxt = f.read()
f.close()

ttoks = nltk.word_tokenize(ttxt)

tText = nltk.Text(ttoks)

tText.dispersion_plot(['America', 'state', 'nation', 'authority', 'citizens', 'liberal', 'conservative', 'politics', 'immigration', 'race', 'economy'])
