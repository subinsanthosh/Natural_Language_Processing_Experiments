import nltk
nltk.download('punkt')
sentence_data = "The First sentence is about Python. The Second: about Django. You can learn Python,Django and Data Ananlysis here. "
nltk_tokens = nltk.sent_tokenize(sentence_data)
for i in nltk_tokens:
  words = nltk.word_tokenize(i)
  print (words)



#For Indian Language :

Code:

from inltk.inltk import tokenize

hindi_text = """प्राचीन काल में विक्रमादित्य नाम के एक आदर्श राजा हुआ करते थे।
अपने साहस, पराक्रम और शौर्य के लिए  राजा विक्रम मशहूर थे। 
ऐसा भी कहा जाता है कि राजा विक्रम अपनी प्राजा के जीवन के दुख दर्द जानने के लिए रात्री के पहर में भेष बदल कर नगर में घूमते थे।"""

tokenize(hindi_text, "hi")


