import numpy as np
import pandas as pd
from numpy import asarray
from numpy import savetxt
from owlready2 import *

# to build in hosting
from flask import Flask, send_from_directory

from flask import Flask, request, jsonify, render_template, make_response
from flask_cors import CORS
import nltk
from nltk import CFG
nltk.download('punkt')

from lib.clear_pharmacho import delete_individual
from lib.parse_tree import parse_tree
from lib.parse_tree import concatenate_sentences
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
from lib.read_sentence import parent_read_sentence
from lib.create_q1 import create_q1

from lib.read_quest import read_quest
from lib.read_quest1 import read_quest1
from lib.read_quest2 import read_quest2
from lib.read_quest3 import read_quest3
from lib.read_quest4 import read_quest4
from lib.read_quest5 import read_quest5
from lib.read_quest6 import read_quest6
from lib.read_quest7 import read_quest7
from lib.read_quest8 import read_quest8
from lib.read_quest9 import read_quest9
from lib.read_quest10 import read_quest10
from lib.read_quest11 import read_quest11
from lib.read_quest_all import read_quest_all

# to build in hosting
app = Flask(__name__, static_folder='static', static_url_path='')

# app = Flask(__name__)
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

# to build in hosting
@app.route('/')
def serve():
    return send_from_directory(app.static_folder, 'index.html')

# to build in hosting
@app.errorhandler(404)
def not_found(e):
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/test', methods=['GET','POST'])
def test():
    try:
        delete_individual()
        sentences = request.json['sentences']
        concatenateSentences = concatenate_sentences(sentences)
        print(f"Iki babi {concatenateSentences}")
        parse_trees = parse_tree(concatenateSentences)
        # print(f'iki ptree {parse_trees}')
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

        rtriplet = read_triplet(FS2)

        file = np.array(rtriplet)
        print(f'iki opo {file}')

        get_quest = read_quest_all(file)

        # res_kalimat = parent_read_sentence(file)
        
        # q1 = create_q1(res_kalimat)

        # template = read_template("QGOT2.txt")

        # sentences = generate_sentence(q1, template)

        return make_response(jsonify({
            # "result": parse_trees,
            # "result": arr_gabungan,
            # "result": new_onto,
            # "result": rtriplet,
            # "result": FS2,
            "result": get_quest,
            # "result": res_kalimat,
            # "result": q1,
            # "resulte": template,
            # "result": sentences
        }), 200)
    except Exception as e:
        return make_response(jsonify(error=str(e)), 500)

if __name__ == '__main__':
    app.run(debug=True)




