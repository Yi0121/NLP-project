with open('my_news.txt', 'r') as f:
    text = f.read()
import nltk
words = nltk.word_tokenize(text)
print("/".join(words))