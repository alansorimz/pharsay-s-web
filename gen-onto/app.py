import numpy as np
import pandas as pd
from numpy import asarray
from numpy import savetxt
from owlready2 import *

from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import nltk
from nltk import CFG
nltk.download('punkt')

from lib.clear_pharmacho import delete_individual
from lib.parse_tree import parse_tree
from lib.preprocess import preprocess
from lib.mapping_component import mapping_component
from lib.preprocess_csv import preprocess_csv
from lib.find import find
from lib.get_type_spok import get_type_spok
from lib.get_type_tagset import get_type_tagset
from lib.create_triplet import create_triplet
from lib.get_sentence_spok import get_sentence_spok 
from lib.read_triplet import read_triplet
from lib.add_relation import add_relation
from lib.add_instance import add_instance
from lib.insert_relation import insert_relation

from lib.parent_recursion import parent_recursion
from lib.create_fs2 import create_fs2
from lib.generate_sentence import generate_sentence
from lib.read_template import read_template


app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

grammar1 = nltk.data.load('Grammar(ind).cfg')
parser = nltk.ChartParser(grammar1)

@app.route('/parse-tree', methods=['GET','POST'])
def get_parse_tree():
    try:
        sentence = request.json['sentence']

        tokens = nltk.word_tokenize(sentence)

        parse_trees = []
        for tree in parser.parse(tokens):
            parse_trees.append(str(tree))
        return jsonify({'parseTrees': parse_trees})
    except Exception as e:
        return jsonify({'error': str(e)})
    
@app.route('/')
def home():
    return jsonify({'message': 'PA ALAN'})

@app.route('/test', methods=['GET','POST'])
def test():
    delete_individual()
    sentences = request.json['sentences']
    parse_trees = parse_tree(sentences)
    preprocess_sentences = preprocess(parse_trees)
    tree_dict, counter_tree = mapping_component()

    arr_asli, arr_gabungan, tree_dict, counter_tree = preprocess_csv(preprocess_sentences, counter_tree, tree_dict)

    K5 = get_type_spok(arr_asli, arr_gabungan)

    arr_asli, arr_gabungan, K5 = get_type_tagset(arr_asli, arr_gabungan, K5)

    arr_asli, arr_gabungan, K5 = create_triplet(arr_asli, arr_gabungan, K5)

    arr_asli, arr_gabungan, K5 = get_sentence_spok(arr_asli, arr_gabungan, K5)

    triplet = read_triplet(K5)

    add_instance(triplet)

    new_onto = add_relation(triplet)

    insert_relation(new_onto)

    onto = get_ontology("Pharmacho.owl").load()

    res_recursion = parent_recursion(onto) #FS1

    FS2 = create_fs2(res_recursion) #FS2

    file = read_triplet(FS2)

    template = read_template("QGOT2.txt")

    sentences = generate_sentence(file, template)

    return jsonify({
        "result": sentences
    })

if __name__ == '__main__':
    app.run(debug=True)