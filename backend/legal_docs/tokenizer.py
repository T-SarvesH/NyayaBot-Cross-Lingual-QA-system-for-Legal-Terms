""" Preprocessing step 1: Tokenization and the docs used are Constitution of India and Maharashtra State Laws """

from nltk.tokenize import word_tokenize, sent_tokenize
import spacy
import nltk
import re
from typing import List, Dict, Set, Tuple
import fitz, pymupdf

nltk.download('punkt', quiet=True)

def word_tokenizer(input: List[str]):
    
    for sentence in input:
        block = word_tokenize(str(sentence))
        print(block)
    
    print()

def sentence_tokenizer(input: List[str]):

    for sentence in input:
        block = sent_tokenize(str(sentence))
        print(block)

    print()

def tokenize_main():
    pdf = fitz.open('Constitution.pdf')
    list = []

    for i, page in enumerate(pdf):
        if(i == 33):
            for tup in page.get_text("blocks"):
                list.append(tup[4])
                print(tup[4])

    for l in list:
        l.strip()
    
    
    word_tokenizer(list)
    sentence_tokenizer(list)
    
if __name__ == "__main__":
    tokenize_main()