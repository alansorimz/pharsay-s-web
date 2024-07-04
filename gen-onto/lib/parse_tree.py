import numpy as np
import nltk
import pandas as pd
import re
from numpy import asarray
from numpy import savetxt
from flask import Flask, jsonify, make_response

#MEMBUAT PARSE TREE

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
        x = remove_punctuation(arr[i]).split()  # Remove punctuation and split into words
        x = np.array(x)
        output = ''
        parsed = False
        try:
            for j, tree in enumerate(parser.parse(x)):
                # Hanya untuk satu kalimat
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