import pickle
import textstats

#read in the source text
f = open('hitler_speeches.txt', encoding = 'utf-8')
htxt = f.read()
f.close()

#obtain new list of word tokens
htoks = textstats.getTokens(htxt)

#remove symbols

symbols = list("~!@#$%^&*()_+-=`{}[]|\\:;\"',./<>?")

htoks_nosym = [t for t in htoks if t not in symbols]

#open a pickled version of the xkcd simple word list
#see https://xkcd.com/simplewriter/
f = open('xkcd_simple_words.p', 'rb')
xkcd_simp = pickle.load(f)
f.close()

#create new list of toks not in the xkcd_simp list
hnotsimptoks = [t for t in htoks_nosym if t not in xkcd_simp]

f = open('hnotsimptoks.p', 'wb')
pickle.dump(hnotsimptoks, f, -1)
f.close()
