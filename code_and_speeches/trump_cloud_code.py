import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
from os import path
from scipy.misc import imread
import pickle

f = open('tnotsimptoks.p', 'rb')
all_tokens = pickle.load(f)
f.close()

d = path.dirname(__file__)

bubble_mask = imread(path.join(d, "image.png"))

wordcloud = WordCloud(
                      #font_path='/Users/sebastian/Library/Fonts/CabinSketch-Bold.ttf',
                      stopwords=STOPWORDS,
                      background_color='white',
                      mask=bubble_mask,
                     ).generate(' '.join(all_tokens))

plt.imshow(wordcloud)
plt.axis('off')
plt.savefig('trump_cloud.png', dpi=300)
