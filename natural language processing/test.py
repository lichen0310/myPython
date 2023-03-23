import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# nltk.download("stopwords")
# nltk.download("punkt")

example_string = """
Muad'Dib learned rapidly because his first training was in how to learn.
And the first lesson of all was the basic trust that he could learn.
It's shocking to find how many people do not believe they can learn,
and how many more believe learning to be difficult."""

stemmer = PorterStemmer()

# sent_tokenize(example_string)
words = word_tokenize(example_string)

stop_words = set(stopwords.words("english"))
filtered_list = []

for word in words:
    if word.casefold() not in stop_words:
        filtered_list.append(word)

stemmed_words = [stemmer.stem(word) for word in words]

print(filtered_list)
print(stemmed_words)
