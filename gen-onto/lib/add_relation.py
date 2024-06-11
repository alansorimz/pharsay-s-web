

def add_relation(triplet):
    file2 = []

    for i in triplet:   
        if(i[1] == 'hasrb'):
            file2.append ('onto.'+i[0]+'.hasRB.append(onto.RB("'+i[2]+'"))')
        if(i[1] == 'hasrp'):
            file2.append ('onto.'+i[0]+'.hasRP.append(onto.RP("'+i[2]+'"))')
        if(i[1] == 'hasasc'):
            file2.append ('onto.'+i[0]+'.hasaSC.append(onto.SC("'+i[2]+'"))')
        if(i[1] == 'hassym'):
            file2.append ('onto.'+i[0]+'.hasSYM.append(onto.SYM("'+i[2]+'"))')
        if(i[1] == 'hasuh'):
            file2.append ('onto.'+i[0]+'.hasUH.append(onto.UH("'+i[2]+'"))')
        if(i[1] == 'hasvb'):
            file2.append ('onto.'+i[0]+'.hasVB.append(onto.VB("'+i[2]+'"))')
        if(i[1] == 'haswh'):
            file2.append ('onto.'+i[0]+'.hasWH.append(onto.WH("'+i[2]+'"))')
        if(i[1] == 'hasmd'):
            file2.append ('onto.'+i[0]+'.hasMD.append(onto.MD("'+i[2]+'"))')
        if(i[1] == 'hascc'):
            file2.append ('onto.'+i[0]+'.hasCC.append(onto.CC("'+i[2]+'"))')
        if(i[1] == 'hascd'):
            file2.append ('onto.'+i[0]+'.hasCD.append(onto.CD("'+i[2]+'"))') 
        if(i[1] == 'hasdt'):
            file2.append ('onto.'+i[0]+'.hasDT.append(onto.DT("'+i[2]+'"))')
        if(i[1] == 'hasfw'):
            file2.append ('onto.'+i[0]+'.hasFW.append(onto.FW("'+i[2]+'"))')
        if(i[1] == 'hasin'):
            file2.append ('onto.'+i[0]+'.hasIN.append(onto.IN("'+i[2]+'"))')
        if(i[1] == 'hasjj'):
            file2.append ('onto.'+i[0]+'.hasJJ.append(onto.JJ("'+i[2]+'"))')
        if(i[1] == 'hasnn'):
            file2.append ('onto.'+i[0]+'.hasNN.append(onto.NN("'+i[2]+'"))')
        if(i[1] == 'hasnnd'):
            file2.append ('onto.'+i[0]+'.hasNND.append(onto.NND("'+i[2]+'"))')
        if(i[1] == 'hasnnp'):
            file2.append ('onto.'+i[0]+'.hasNNP.append(onto.NNP("'+i[2]+'"))')
        if(i[1] == 'hasneg'):
            file2.append ('onto.'+i[0]+'.hasNEG.append(onto.NEG("'+i[2]+'"))') 
        if(i[1] == 'hasod'):
            file2.append ('onto.'+i[0]+'.hasOD.append(onto.OD("'+i[2]+'"))') 
        if(i[1] == 'haspr'):
            file2.append ('onto.'+i[0]+'.hasPR.append(onto.PR("'+i[2]+'"))')
        if(i[1] == 'hasprp'):
            file2.append ('onto.'+i[0]+'.hasPRP.append(onto.PRP("'+i[2]+'"))')
            
        if(i[1] == 'hasnext'):
            file2.append ('onto.'+i[0]+'.hasNext.append(onto.S("'+i[2]+'"))')
        if(i[1] == 'hasprev'):
            file2.append ('onto.'+i[0]+'.hasPrev.append(onto.Prev("'+i[2]+'"))')
        if(i[1] == 'haspart'):
            file2.append ('onto.'+i[0]+'.hasPart.append(onto.Part("'+i[2]+'"))')
        if(i[1] == 'hasznext'):
            if ('pewatas' in i[2]):
                file2.append ('onto.'+i[0]+'.hasZnext.append(onto.Pewatas("'+i[2]+'"))')
            if ('fadje' in i[2]):
                file2.append ('onto.'+i[0]+'.hasZnext.append(onto.FAdje("'+i[2]+'"))')
            if ('fnom' in i[2]):
                file2.append ('onto.'+i[0]+'.hasZnext.append(onto.FNom("'+i[2]+'"))')
            if ('fnum' in i[2]):
                file2.append ('onto.'+i[0]+'.hasZnext.append(onto.FNum("'+i[2]+'"))')
            if ('fprep' in i[2]):
                file2.append ('onto.'+i[0]+'.hasZnext.append(onto.FPrep("'+i[2]+'"))')
            if ('fverb' in i[2]):
                file2.append ('onto.'+i[0]+'.hasZnext.append(onto.FVerb("'+i[2]+'"))')
            
        if(i[1] == 'hasfadje'):
            file2.append ('onto.'+i[0]+'.hasFadje.append(onto.FAdje("'+i[2]+'"))')
        if(i[1] == 'hasfnom'):
            file2.append ('onto.'+i[0]+'.hasFnom.append(onto.FNom("'+i[2]+'"))')
        if(i[1] == 'hasfnum'):
            file2.append ('onto.'+i[0]+'.hasFnum.append(onto.FNum("'+i[2]+'"))')
        if(i[1] == 'hasfprep'):
            file2.append ('onto.'+i[0]+'.hasFprep.append(onto.FPrep("'+i[2]+'"))')
        if(i[1] == 'hasfverb'):
            file2.append ('onto.'+i[0]+'.hasFverb.append(onto.FVerb("'+i[2]+'"))')
        
        if(i[1] == 'hasklausa'):
            file2.append ('onto.'+i[0]+'.hasKlausa.append(onto.Klausa("'+i[2]+'"))')
        if(i[1] == 'hasasub'):
            file2.append ('onto.'+i[0]+'.hasaSub.append(onto.Subjek("'+i[2]+'"))')
        if(i[1] == 'hasbpre'):
            file2.append ('onto.'+i[0]+'.hasbPre.append(onto.Predikat("'+i[2]+'"))')
        if(i[1] == 'hascobj'):
            file2.append ('onto.'+i[0]+'.hascObj.append(onto.Objek("'+i[2]+'"))')
        if(i[1] == 'hasdpel'):
            file2.append ('onto.'+i[0]+'.hasdPel.append(onto.Pelengkap("'+i[2]+'"))')
        if(i[1] == 'haseket'):
            file2.append ('onto.'+i[0]+'.haseKet.append(onto.Keterangan("'+i[2]+'"))')
        if(i[1] == 'haspewatas'):
            file2.append ('onto.'+i[0]+'.hasPewatas.append(onto.Pewatas("'+i[2]+'"))')

    return file2
