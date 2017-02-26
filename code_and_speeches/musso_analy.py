import pickle
import textstats

#read in the source text
f = open('mussolini_speeches.txt', encoding = 'utf-8')
mtxt = f.read()
f.close()

#obtain new list of word tokens
mtoks = textstats.getTokens(mtxt)

#remove symbols

symbols = list("~!@#$%^&*()_+-=`{}[]|\\:;\"',./<>?")

mtoks_nosym = [t for t in mtoks if t not in symbols]

#open a pickled version of the xkcd simple word list
#see https://xkcd.com/simplewriter/
f = open('xkcd_simple_words.p', 'rb')
xkcd_simp = pickle.load(f)
f.close()

#create new list of toks not in the xkcd_simp list
mnotsimptoks = [t for t in mtoks_nosym if t not in xkcd_simp]

f = open('mnotsimptoks.p', 'wb')
pickle.dump(mnotsimptoks, f, -1)
f.close()
