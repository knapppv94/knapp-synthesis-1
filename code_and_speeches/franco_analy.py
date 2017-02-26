import pickle
import textstats

#read in the source text
f = open('franco_speeches.txt', encoding = 'utf-8')
ftxt = f.read()
f.close()

#obtain new list of word tokens
ftoks = textstats.getTokens(ftxt)

#remove symbols

symbols = list("~!@#$%^&*()_+-=`{}[]|\\:;\"',./<>?")

ftoks_nosym = [t for t in ftoks if t not in symbols]

#open a pickled version of the xkcd simple word list
#see https://xkcd.com/simplewriter/
f = open('xkcd_simple_words.p', 'rb')
xkcd_simp = pickle.load(f)
f.close()

#create new list of toks not in the xkcd_simp list
fnotsimptoks = [t for t in ftoks_nosym if t not in xkcd_simp]

f = open('fnotsimptoks.p', 'wb')
pickle.dump(fnotsimptoks, f, -1)
f.close()
