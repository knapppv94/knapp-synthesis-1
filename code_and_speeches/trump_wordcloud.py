from os import path
from scipy.misc import imread
import matplotlib.pyplot as plt

from wordcloud import WordCloud, STOPWORDS

d = path.dirname(__file__)

# Read the whole text.
f = open('trump_speeches.txt', encoding = 'utf-8')
text = path.join(f).read()

# read the mask image
# taken from
# http://www.stencilry.org/stencils/movies/alice%20in%20wonderland/255fk.jpg
user_mask = imread(path.join(d, "user.png"))

wc = WordCloud(background_color="white", max_words=2000, mask=user_mask,
               stopwords=STOPWORDS.add("said"))
# generate word cloud
wc.generate(text)

# store to file
wc.to_file(path.join(d, "user.png"))

# show
plt.imshow(wc)
plt.axis("off")
plt.figure()
plt.imshow(user_mask, cmap=plt.cm.gray)
plt.axis("off")
plt.show()
