import nltk

f = open('hitler_speeches.txt', encoding = 'utf-8')
htxt = f.read()
f.close()

htoks = nltk.word_tokenize(htxt)

hText = nltk.Text(htoks)

hText.dispersion_plot(['Germany', 'state', 'nation', 'authority', 'citizens', 'liberal', 'conservative', 'politics', 'immigration', 'race', 'economy'])
