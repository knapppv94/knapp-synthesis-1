import pickle
import textstats

#open my pickled file of Trump tokens -- for original code, see other speech writers
f = open('ttoks_nosym.p', 'rb')
ttoks_nosym = pickle.load(f)
f.close()


#open a pickled version of the xkcd simple word list
#see https://xkcd.com/simplewriter/
f = open('xkcd_simple_words.p', 'rb')
xkcd_simp = pickle.load(f)
f.close()

#create new list of toks not in the xkcd_simp list
tnotsimptoks = [t for t in ttoks_nosym if t not in xkcd_simp]

f = open('tnotsimptoks.p', 'wb')
pickle.dump(tnotsimptoks, f, -1)
f.close()
