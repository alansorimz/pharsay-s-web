import numpy as np
import nltk
import pandas as pd
import re
from numpy import asarray
from numpy import savetxt

#MEMBUAT PARSE TREE

def parse_tree(sentences):
    arr = sentences.split('\n')
    grammar1 = nltk.data.load('Grammar(ind).cfg')
    parser = nltk.ChartParser(grammar1)
    final = []

    # Function to remove punctuation
    def remove_punctuation(text):
        return re.sub(r'[^\w\s]', '', text)

    for i in range(len(arr)):
        x = remove_punctuation(arr[i]).split()  # Remove punctuation and split into words
        x = np.array(x)
        output = ''
        for j, tree in enumerate(parser.parse(x)):
            output += str(tree)
            output += "\n"
        final.append(output.strip())

    return final
