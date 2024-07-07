import numpy as np
import nltk
import pandas as pd
import re
from numpy import asarray
from numpy import savetxt
from flask import Flask, jsonify, make_response

#MEMBUAT PARSE TREE

# Function to concatenate sentences
def concatenate_sentences(sentences):
    def remove_punctuation_except_period(text):
        return re.sub(r'[^\w\s\.]', '', text)
    
    sentences = remove_punctuation_except_period(sentences).lower()
    sentence_list = [sentence.strip() for sentence in sentences.split('.') if sentence.strip()]

    if len(sentence_list) < 2:
        return sentences

    subjects = [sentence.split()[0] for sentence in sentence_list]
    
    if subjects[0] == subjects[1]:
        return subjects[0] + " " + " ".join(sentence_list[0].split()[1:]) + " " + " ".join(sentence_list[1].split()[1:])
    else:
        return "Subjects do not match"

def parse_tree(sentences):
    arr = sentences.split('\n')
    grammar1 = nltk.data.load('Grammar(ind).cfg')
    parser = nltk.ChartParser(grammar1)
    final = []

    # Function to remove punctuation
    def remove_punctuation(text):
        text = text.lower()
        return re.sub(r'[^\w\s]', '', text)

    for i in range(len(arr)):
        # x = arr[i].split()
        x = remove_punctuation(arr[i]).split()  # Remove punctuation and split into words
        x = np.array(x)
        output = ''
        parsed = False
        try:
            for j, tree in enumerate(parser.parse(x)):
                # Hanya untuk satu parse tree per kalimat
                if j == 0:
                    output += str(tree)
                    output += "\n"
                    parsed = True

                if not parsed:
                        raise ValueError(f"Grammar not found for the given sentence: {arr[i]}")
        except ValueError as e:
            raise ValueError(f"Error parsing sentence: {str(e)}")
        
        final.append(output.strip())

    return final