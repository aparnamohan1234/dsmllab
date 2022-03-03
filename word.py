import nltk
from nltk.tokenize import
sent_tokenize,word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem.wordnet import
WordNetLemmatizer
nltk.download('punkt')
nltk.download('stopwords')
text="""Helo Mr.Smith,how are you doing today?The weather is great,and city is awesome.
The sky is pinkish-blue.You should not eat cardboard"""
tokenize_word=word_tokenize(text)
print(tokenize_word)
stop_word=set(stopwords.words("english"))
print(stop_word)
filtered_word=[]
for w in tokenize_word:
    if w not in stop_word:
        filtered_word.append(W)
        print("Tokenized Sentence:",tokenize_word)
        print("Filtered Sentence:",filtered_word)
        ps=PorterStemmer()
       