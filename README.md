# word_cloud
Library for word cloud visualization for data scientists. Use within Jupyter notebook, from a webapp, etc.

![alt text](word_cloud.gif)


## Quick Start

1. Install with pip

```
pip install git+ssh://git@github.com/kavgan/word_cloud.git
```

2. Instatiate WordCloud, get word cloud HTML code and display!

``` python
from word_cloud.word_cloud_generator import WordCloud
from IPython.core.display import HTML

ENGLISH_STOP_WORDS = frozenset([
    "a", "about", "above", "across", "after", "afterwards", "again", "against",
    "all", "almost", "alone", "along", "already", "also", "although", "always",
    "am", "among", "amongst", "amoungst", "amount", "an", "and", "another",
    "any", "anyhow", "anyone", "anything", "anyway", "anywhere", "are",
    "around", "as", "at", "back", "be", "became", "because", "become",
    "becomes", "becoming", "been", "before", "beforehand", "behind", "being",
    "below", "beside", "besides", "between", "beyond", "bill", "both",
    "bottom", "but", "by", "call", "can", "cannot", "cant", "co", "con",
    "could", "couldnt", "cry", "de", "describe", "detail", "do", "done",
    "down", "due", "during", "each", "eg", "eight", "either", "eleven", "else",
    "elsewhere", "empty", "enough", "etc", "even", "ever", "every", "everyone",
    "everything", "everywhere", "except", "few", "fifteen", "fifty", "fill",
    "find", "fire", "first", "five", "for", "former", "formerly", "forty",
    "found", "four", "from", "front", "full", "further", "get", "give", "go",
    "had", "has", "hasnt", "have", "he", "hence", "her", "here", "hereafter",
    "who", "whoever", "whole", "whom", "whose", "why", "will", "with",
    "within", "without", "would", "yet", "said","you", "your", "yours", "yourself",
    "yourselves"])

# list of documents
texts=['MEXICO CITY — Newly formed Hurricane Willa rapidly intensified off Mexico\'s Pacific coast','MEXICO CITY — Newly formed Hurricane Willa rapidly intensified off Mexico\'s Pacific coast Sunday and early Monday and became a major Category 5 storm, the U.S. National Hurricane Center said. As of 11 a.m. ET., Willa had maximum sustained winds of 160 mph -- just 3 mph over the threshold for a Category 5.    Willa was "potentially catastrophic," forecasters warned. The hurricane center said it could make landfall along Mexico\'s southwestern coast Tuesday afternoon or evening and bring with it a life-threatening storm surge -- especially near and to the south of where the center of Willa makes landfall.    Near the coast, the surge will be accompanied by large and destructive waves. Willa is also forecast to bring high winds and heavy rainfall.    "Slight weakening is forecast to begin on Tuesday, but Willa is expected to be an extremely dangerous major hurricane when it reaches the coast of Mexico," the center said.    A map made by the U.S. National Hurricane Center shows the projected path for Hurricane Willa as of 11 a.m. ET on Oct. 22, 2018.   A map made by the U.S. National Hurricane Center shows the projected path for Hurricane Willa as of 11 a.m. ET on Oct. 22, 2018. NATIONAL HURRICANE CENTER  The center said Willa was about 175 miles south-southwest of Las Islas Marias, Mexico, and some 135 miles southwest of Cabo Corrientes, Mexico, and was moving north at about 7 mph.    Hurricane-force winds extended outward up to 30 miles from the center and tropical-storm-force winds extended outward up to 105 miles.    A hurricane warning was posted for a stretch of shore between San Blas and Mazatlan. A tropical storm warning was in effect for Playa Perula to San Blas and north of Mazatlan to Bahia Tempehuaya.    Forecasters said Willa is expected to produce storm total rainfall accumulations of 6 to 12 inches, with local amounts up to 18 inches, across portions of western Jalisco, western Nayarit, and southern Sinaloa in Mexico. The rainfall could cause life-threatening flash flooding and landslides.    Farther inland, Willa is expected to produce rainfall amounts of 2 to 4 inches across portions of Zacateca, Durango, southeast Chihuahua, and Coahuila in Mexico, with local amounts up to 6 inches possible. That could cause life-threatening flash flooding.    After Willa makes its way across Mexico, it could drop between 1 and 3 inches of rain on central and southern Texas during the middle of the week, CBS News contributing meteorologist Jeff Berardelli reports. The additional rainfall could cause additional flooding in already saturated areas.','early Monday and became a major Category 5 storm, the U.S. National Hurricane Center said. As of 11 a.m. ET., Willa had maximum sustained winds of 160 mph -- just 3 mph over the threshold for a Category 5.    Willa was "potentially catastrophic," forecasters warned. The hurricane center said it could make landfall along Mexico\'s southwestern coast Tuesday afternoon or evening and bring with it a life-threatening storm surge -- especially near and to the south of where the center of Willa makes landfall.    Near the coast, the surge will be accompanied by large and destructive waves. Willa is also forecast to bring high winds and heavy rainfall.    "Slight weakening is forecast to begin on Tuesday, but Willa is expected to be an extremely dangerous major hurricane when it reaches the coast of Mexico," the center said.    A map made by the U.S. National Hurricane Center shows the projected path for Hurricane Willa as of 11 a.m. ET on Oct. 22, 2018.   A map made by the U.S. National Hurricane Center shows the projected path for Hurricane Willa as of 11 a.m. ET on Oct. 22, 2018. NATIONAL HURRICANE CENTER  The center said Willa was about 175 miles south-southwest of Las Islas Marias, Mexico, and some 135 miles southwest of Cabo Corrientes, Mexico, and was moving north at about 7 mph.    Hurricane-force winds extended outward up to 30 miles from the center and tropical-storm-force winds extended outward up to 105 miles.    A hurricane warning was posted for a stretch of shore between San Blas and Mazatlan. A tropical storm warning was in effect for Playa Perula to San Blas and north of Mazatlan to Bahia Tempehuaya.    Forecasters said Willa is expected to produce storm total rainfall accumulations of 6 to 12 inches, with local amounts up to 18 inches, across portions of western Jalisco, western Nayarit, and southern Sinaloa in Mexico. The rainfall could cause life-threatening flash flooding and landslides.    Farther inland, Willa is expected to produce rainfall amounts of 2 to 4 inches across portions of Zacateca, Durango, southeast Chihuahua, and Coahuila in Mexico, with local amounts up to 6 inches possible. That could cause life-threatening flash flooding.    After Willa makes its way across Mexico, it could drop between 1 and 3 inches of rain on central and southern Texas during the middle of the week, CBS News contributing meteorologist Jeff Berardelli reports. The additional rainfall could cause additional flooding in already saturated areas.']

# initialize WordCloud
wc=WordCloud(stopwords=ENGLISH_STOP_WORDS)

# get html code
embed_code=wc.get_embed_code(text=texts,random_color=True,topn=40)

# display
HTML(embed_code)

```

## More Examples
- [Checkout Jupyter Notebook from this Repo](https://github.com/kavgan/word_cloud/blob/master/Example%20word%20clouds.ipynb) (word cloud only renders if your server is running)
- [Jupyter Notebook on Google's Colaboratory](https://colab.research.google.com/drive/1AkdUKEFmaYom77r6KPh18jdQrplIQbKQ)
- [Article]()
