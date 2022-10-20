# Experiment 8

# Aim : Apply reference resolution technique on the given text input.

import spacy
import neuralcoref

nlp = spacy.load('en_core_web_sm')  # load the model
neuralcoref.add_to_pipe(nlp)

text = "Joseph Robinette Biden Jr. is an American politician who is the 46th and\
current president of the United States. A member of the Democratic Party, \
he served as the 47th vice president from 2009 to 2017 under Barack Obama and\
represented Delaware in the United States Senate from 1973 to 2009."

doc = nlp(text)  # get the spaCy Doc (composed of Tokens)

print(doc._.coref_clusters)  # You can see cluster of similar mentions

# Output:
# [Joseph Robinette Biden Jr.: [Joseph Robinette Biden Jr., he]]

print(doc._.coref_resolved)

# Output:
# Joseph Robinette Biden Jr. is an American politician who is the 46th andcurrent president of the United States. A member of the Democratic Party, Joseph Robinette Biden Jr. served as the 47th vice president from 2009 to 2017 under Barack Obama andrepresented Delaware in the United States Senate from 1973 to 2009.

from allennlp.predictors.predictor import Predictor


model_url = "https://storage.googleapis.com/allennlp-public-models/coref-spanbert-large-2020.02.27.tar.gz"
predictor = Predictor.from_path(model_url)

text = "Joseph Robinette Biden Jr. is an American politician who is the 46th and\
current president of the United States. A member of the Democratic Party, \
he served as the 47th vice president from 2009 to 2017 under Barack Obama and\
represented Delaware in the United States Senate from 1973 to 2009."


prediction = predictor.predict(document=text)  # get prediction
print("Clusters:-")
for cluster in prediction['clusters']:
    print(cluster)  # list of clusters (the indices of spaCy tokens)
# Result: [[[0, 3], [26, 26]], [[34, 34], [50, 50]]]
print('\n\n') #Newline

print('Coref resolved: ',predictor.coref_resolved(text))  # resolved text
# Result: Joseph Robinette Biden Jr. is an American politician who is the 4

# Output:
# Clusters:-
# [[0, 3], [26, 26]]
# [[34, 34], [50, 50]]

print(prediction['document'])

# Output:
# ['Joseph', 'Robinette', 'Biden', 'Jr.', 'is', 'an', 'American', 'politician', 'who', 'is', 'the', '46th', 'andcurrent', 'president', 'of', 'the', 'United', 'States', '.', 'A', 'member', 'of', 'the', 'Democratic', 'Party', ',', 'he', 'served', 'as', 'the', '47th', 'vice', 'president', 'from', '2009', 'to', '2017', 'under', 'Barack', 'Obama', 'andrepresented', 'Delaware', 'in', 'the', 'United', 'States', 'Senate', 'from', '1973', 'to', '2009', '.']



