# Menambahkan Instance

from owlready2 import *

def add_instance(triplet):
    onto = get_ontology("Pharmacho.owl").load()

    for i in triplet:
        if(i[1] == 'type' and i[2] == 's'):
            onto.Kalimat(i[0])
        if(i[1] == 'type' and i[2] == 'klausa'):
            onto.Klausa(i[0])
        if(i[1] == 'type' and i[2] == 'sub'):
            onto.Subjek(i[0])
        if(i[1] == 'type' and i[2] == 'pre'):
            onto.Predikat(i[0])
        if(i[1] == 'type' and i[2] == 'obj'):
            onto.Objek(i[0])
        if(i[1] == 'type' and i[2] == 'pel'):
            onto.Pelengkap(i[0])
        if(i[1] == 'type' and i[2] == 'ket'):
            onto.Keterangan(i[0])
        if(i[1] == 'type' and i[2] == 'pewatas'):
            onto.Pewatas(i[0])
        if(i[1] == 'type' and i[2] == 'cc'):
            onto.CC(i[0])
        if(i[1] == 'type' and i[2] == 'cd'):
            onto.CD(i[0])
        if(i[1] == 'type' and i[2] == 'dt'):
            onto.DT(i[0])
        if(i[1] == 'type' and i[2] == 'fadje'):
            onto.FAdje(i[0])
        if(i[1] == 'type' and i[2] == 'fadv'):
            onto.FAdv(i[0])
        if(i[1] == 'type' and i[2] == 'fnom'):
            onto.FNom(i[0])
        if(i[1] == 'type' and i[2] == 'fnum'):
            onto.FNum(i[0])
        if(i[1] == 'type' and i[2] == 'fprep'):
            onto.FPrep(i[0])
        if(i[1] == 'type' and i[2] == 'fverb'):
            onto.FVerb(i[0])
        if(i[1] == 'type' and i[2] == 'fw'):
            onto.FW(i[0])    
        if(i[1] == 'type' and i[2] == 'in'):
            onto.IN(i[0])
        if(i[1] == 'type' and i[2] == 'jj'):
            onto.JJ(i[0])
        if(i[1] == 'type' and i[2] == 'md'):
            onto.MD(i[0])
        if(i[1] == 'type' and i[2] == 'neg'):
            onto.NEG(i[0])
        if(i[1] == 'type' and i[2] == 'nn'):
            onto.NN(i[0])
        if(i[1] == 'type' and i[2] == 'nnd'):
            onto.NND(i[0])
        if(i[1] == 'type' and i[2] == 'nnp'):
            onto.NNP(i[0])
        if(i[1] == 'type' and i[2] == 'od'):
            onto.OD(i[0])
        if(i[1] == 'type' and i[2] == 'pr'):
            onto.PR(i[0])
        if(i[1] == 'type' and i[2] == 'prp'):
            onto.PRP(i[0])
        if(i[1] == 'type' and i[2] == 'rb'):
            onto.RB(i[0])
        if(i[1] == 'type' and i[2] == 'rp'):
            onto.RP(i[0])
        if(i[1] == 'type' and i[2] == 'sc'):
            onto.SC(i[0])
        if(i[1] == 'type' and i[2] == 'sym'):
            onto.SYM(i[0])
        if(i[1] == 'type' and i[2] == 'uh'):
            onto.UH(i[0])
        if(i[1] == 'type' and i[2] == 'vb'):
            onto.VB(i[0])
        if(i[1] == 'type' and i[2] == 'wh'):
            onto.WH(i[0])  
    
    onto.save('Pharmacho.owl', format="rdfxml")