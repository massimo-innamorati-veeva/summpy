#!/usr/bin/env python
# -*- coding: utf-8 -*-

import nltk
from string import punctuation

stemmer = nltk.stem.PorterStemmer()
stopwords = set(list(nltk.corpus.stopwords.words("english")) + list(punctuation))
nltk.download('stopwords')
nltk.download('punkt')


def word_tokenize(text):
    """Custom word tokenizer removing punctuation and stopwords"""
    words = nltk.word_tokenize(text.lower())
    return [stemmer.stem(w) for w in words if w not in stopwords]


def tree_encode(obj, encoding='utf-8'):
    type_ = type(obj)
    if type_ == list or type_ == tuple:
        return [tree_encode(e, encoding) for e in obj]
    elif type_ == dict:
        new_obj = dict(
            (tree_encode(k, encoding), tree_encode(v, encoding))
            for k, v in obj.iteritems()
        )
        return new_obj
    else:
        return obj


if __name__ == '__main__':
    pass
