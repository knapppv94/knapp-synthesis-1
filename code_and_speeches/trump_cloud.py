import pickle
import numpy as np
import random
from PIL import Image
from wordcloud import WordCloud, STOPWORDS
from palettable.colorbrewer.sequential import Reds_9

def color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    return tuple(Reds_9.colors[random.randint(2,8)])

fa_path = "/Users/paigeknapp/Documents/"
font_path = "/Users/paigeknapp/Fonts/OpenSans-CondBold.ttf"

icon = "user"

f = open('trump_speeches.p', 'rb') ## need to fix this line
words_array = pickle.load(f)
f.close()


		 		
# http://stackoverflow.com/questions/7911451/pil-convert-png-or-gif-with-transparency-to-jpg-without
icon_path = fa_path + "%s.png" % icon
icon = Image.open(icon_path)
mask = Image.new("RGB", icon.size, (255,255,255))
mask.paste(icon,icon)
mask = np.array(mask)

wc = WordCloud(font_path=font_path, background_color="white", max_words=2000, mask=mask,
               max_font_size=300, random_state=42)
               
# generate word cloud
wc.generate_from_text(words_array)
wc.recolor(color_func=color_func, random_state=3)
wc.to_file("trump_cloud.png")
