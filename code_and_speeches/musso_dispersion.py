import nltk

f = open('Mussolini_speeches.txt', encoding = 'utf-8')
mtxt = f.read()
f.close()

mtoks = nltk.word_tokenize(mtxt)

mText = nltk.Text(mtoks)

mText.dispersion_plot(['Italy', 'state', 'nation', 'authority', 'citizens', 'liberal', 'conservative', 'politics', 'immigration', 'race', 'economy'])
