#ENGLISH LANGUAGE
import nltk as nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

example_sent = """This is a sample sentence,
				showing off the stop words filtration."""

stop_words = set(stopwords.words('english'))

word_tokens = word_tokenize(example_sent)

filtered_sentence = [w for w in word_tokens if not w.lower() in stop_words]

filtered_sentence = []

for w in word_tokens:
	if w not in stop_words:
		filtered_sentence.append(w)

print(word_tokens)
print(filtered_sentence)


#INDIAN LANGUAGE
import advertools as adv
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

example_sent = "आज हम संत तुकाराम महाराजजी की कथा सुनेंगे । संत तुकाराम महाराज जी की भगवान पांडुरंग के प्रति अनन्‍यसाधारण भक्‍ति थी । उनका जन्‍म महाराष्‍ट्र के देहू गांव में हुआ था और वे सदेह वैकुंठ गए थे । अर्थात वे देहत्‍याग किए बिना अपने स्‍थूल देह के साथ भगवान श्रीविष्‍णुजी के वैकुंठधाम गए थे ।"
stop_words = adv.stopwords['hindi']
words = word_tokenize(example_sent)

filtered_sentence = [w for w in words if not w.lower() in stop_words]
print(filtered_sentence)
