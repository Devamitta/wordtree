#!/usr/bin/env python3.10
# coding: utf-8

from nltk.tokenize import word_tokenize
from nltk.util import ngrams
from wordtree import search_and_draw
import pandas as pd

# open ebts.txt
with open ("input/ebts.txt", "r") as f:
	text = str(f.read())

# open ebt freq csv and make a list
ebt_freq_df = pd.read_csv("input/ebts.csv", header =None, sep="\t")
ebt_freq_list = ebt_freq_df[0].to_list()
# print(ebt_freq_list[:100])

# make ngrams
def get_ngrams(text, n):
    n_grams = ngrams(word_tokenize(text), n)
    return [ ' '.join(grams) for grams in n_grams]
ngrams_text = get_ngrams(text, 5)
# print(ngrams_text)

for row in range(100):
    word = ebt_freq_list[row]
    g = search_and_draw(corpus=ngrams_text, keyword=word, max_n=5)
    g.render(f"pics/{word}") 
