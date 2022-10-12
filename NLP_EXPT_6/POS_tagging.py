import nltk
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

stop_words = set(stopwords.words('english'))
 
txt = "Sukanya, Rajib and Naba are my good friends. " \
    "Sukanya is getting married next year. " \
    "Marriage is a big step in one’s life." \
    "It is both exciting and frightening. " \
    "But friendship is a sacred bond between people." \
    "It is a special kind of love between us. " \
    "Many of you must have tried searching for a friend "\
    "but never found the right one."
 
# sent_tokenize is one of instances of
# PunktSentenceTokenizer from the nltk.tokenize.punkt module
 
tokenized = sent_tokenize(txt)
for i in tokenized:
     
    # Word tokenizers is used to find the words
    # and punctuation in a string
    wordsList = nltk.word_tokenize(i)
 
    # removing stop words from wordList
    wordsList = [w for w in wordsList if not w in stop_words]
 
    #  Using a Tagger. Which is part-of-speech
    # tagger or POS-tagger.
    tagged = nltk.pos_tag(wordsList)
 
    print(tagged)


import nltk
from nltk.corpus import indian
from nltk.tag import tnt
import string


nltk.download('punkt')
nltk.download('indian')


tagged_set = 'hindi.pos'
word_set = indian.sents(tagged_set)
count = 0
for sen in word_set:
    count = count + 1
    sen = "".join([" "+i if not i.startswith("'") and i not in string.punctuation else i for i in sen]).strip()
    #print (sen)
#print (count)

train_perc = .9

train_rows = int(train_perc*count)
test_rows = train_rows + 1

#print (train_rows, test_rows)

data = indian.tagged_sents(tagged_set)
train_data = data[:train_rows]
test_data = data[test_rows:]


pos_tagger = tnt.TnT()
pos_tagger.train(train_data)
pos_tagger.evaluate(test_data)

word_to_be_tagged = u"३९ गेंदों में दो चौकों और एक छक्के की मदद से ३४ रन बनाने वाले परोरे अंत तक आउट नहीं हुए ।"

tokenized = nltk.word_tokenize(word_to_be_tagged)


print(pos_tagger.tag(tokenized))