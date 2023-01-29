import jsonlines
import sys
import unicodedata

import numpy as np
# nltk.download('punkt')
# nltk.download('stopwords')
import pandas as pd
import pymorphy2
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer

raw_data = []

with jsonlines.open('parsing/spider/spider/spiders/my_spiders/my_items.json') as reader:
    for line in reader:
        raw_data.append(line['data'])

text_data = np.array(raw_data)
punctuation_digit = dict.fromkeys(
    i for i in range(sys.maxunicode)
    if unicodedata.category(chr(i)).startswith('P')
    or unicodedata.category(chr(i)).startswith('Nd')
)

stop_words = stopwords.words('russian')
stop_words.extend(['млн', 'млрд', 'руб', 'новость', 'тыс', 'кв', 'год', 'года', 'году', 'рбк', 'также',
                   'это', 'эта', 'эти', 'по', 'который', 'январь', 'февраль', 'март', 'апрель', 'май',
                   'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь', 'аиф', 'фото'
                   'редакция', 'газета', 'фгб', 'раздел', 'видео', 'почему'])

morph = pymorphy2.MorphAnalyzer()

new_text_data = []
for i, text in enumerate(text_data):
    # cast punctuation and digits to None
    new_text = ''.join([char.translate(punctuation_digit) for char in text])
    tokenized_words = [morph.parse(word)[0].normal_form for word in word_tokenize(new_text)]
    new_text_data.append(' '.join([word for word in tokenized_words if word not in stop_words]))
new_text_data = np.array(new_text_data)

tfidf = TfidfVectorizer(ngram_range=(4, 4))
feature_matrix = tfidf.fit_transform(new_text_data)
frame = pd.DataFrame(feature_matrix.todense(), columns=tfidf.get_feature_names_out())

print(frame.max().sort_values(ascending=False)[:20])
print(feature_matrix.max())
