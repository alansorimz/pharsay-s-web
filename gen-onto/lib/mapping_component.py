import csv
import numpy as np

s_tree = ['sub', 'pre', 'obj', 'pel', 'ket', 's']
cc_tree = ['cc']
sc_tree = ['sc']
klausa_tree = ['klausa']
sub_tree = ['prp', 'nn', 'nnp', 'fnum', 's', 'nn', 'pewatas']
pre_tree = ['vb', 'fverb', 'fnom', 'fprep', 'fadje']
obj_tree = ['nn', 'nnp', 'fnom', 'sc', 's']
pel_tree = ['nn', 'jj', 'fnom', 'fadje', 'in', 'nnp', 'kr', 'pre', 'fverb']
ket_tree = ['fprep', 'fket', 'fnom', 'fverb', 'sc', 's']
pewatas_tree = ['dt', 'fnom', 'dt', 'fverb']
fnum_tree = ['cd', 'nnd', 'cd', 'nn', 'fnum', 'prp']
fnom_tree = ['nn', 'nnp', 'pr', 'prp', 'jj', 'fnom']
fverb_tree = ['sc', 'vb', 'md', 'rb', 'jj', 'nnp', 'cc']
fadje_tree = ['jj', 'rb', 'nn', 'vb', 'neg']
bfprep_tree = ['in', 'fprep', 'nn', 'nnp', 'cd', 'fnom', 'fverb', 'fnum', 'sc']
fket_tree = ['ketn', 'pr']
ketn_tree = ['kemarin', 'siang', 'siang', 'sore', 'pagi', 'malam']

tree_dict = {
    's': s_tree,
    'klausa': klausa_tree,
    'sub': sub_tree,
    'pre': pre_tree,
    'obj': obj_tree,
    'pel': pel_tree,
    'ket': ket_tree,
    'cc': cc_tree,
    'sc': sc_tree,
    'pewatas': pewatas_tree,
    'fnum': fnum_tree,
    'fnom': fnom_tree,
    'fverb': fverb_tree,
    'fadje': fadje_tree,
    'fprep': bfprep_tree,
    'fket': fket_tree,
    'ketn': ketn_tree
}

counter_tree = {
    's': 0,
    'klausa': 0,
    'sub': 0,
    'pre': 0,
    'obj': 0,
    'pel': 0,
    'ket': 0,
    'cc' : 0,
    'sc' : 0,
    'pewatas': 0,
    'fnum': 0,
    'fnom': 0,
    'fverb': 0,
    'fadje': 0,
    'fprep': 0,
    'fket': 0,
    'ketn': 0
}

def mapping_component():
    return tree_dict, counter_tree