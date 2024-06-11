
def create_triplet(arr_asli, arr_gabungan, file1):
    for arr_a in range(len(arr_asli)):
        for i in range(len(arr_asli[arr_a])-1):
            tree_asli = arr_asli[arr_a][i]
            next_tree_asli = arr_asli[arr_a][i + 1]
            tree_g = arr_gabungan[arr_a][i]
            next_tree_g = arr_gabungan[arr_a][i + 1]
        
            try:
                if (tree_asli == 'sub'and next_tree_asli != 'fnom'):
                    if (next_tree_asli != 'fnum'):
                        file1.append(f'{tree_g} has{next_tree_asli} {arr_gabungan[arr_a][i+2]}') # sub has nnp
                if (tree_asli == 'pre'and next_tree_asli != 'fverb'):
                    file1.append (f'{tree_g} has{next_tree_asli} {arr_gabungan[arr_a][i+2]}') # pre has vb
                if (tree_asli == 'obj'and next_tree_asli != 'fnom'):
                    file1.append (f'{tree_g} has{next_tree_asli} {arr_gabungan[arr_a][i+2]}') # obj has nnp
                if (tree_asli == 'pel'and next_tree_asli != 'fnom'):
                    file1.append (f'{tree_g} has{next_tree_asli} {arr_gabungan[arr_a][i+2]}') # pel has nnp
                if (tree_asli == 'ket' and  arr_asli[arr_a][i + 1] == 'sc'):
                    file1.append (f'{tree_g} hasa{arr_asli[arr_a][i + 1]} {arr_asli[arr_a][i + 2]}') # ket hasSC x
                    if (arr_asli[arr_a][i + 3] == 'vb' or arr_asli[arr_a][i + 3] == 'nn' or arr_asli[arr_a][i + 3] == 'nnp'):
                        file1.append (f'{tree_g} has{arr_asli[arr_a][i + 3]} {arr_asli[arr_a][i + 4]}') # ket hasVB x
            except:
                file1.append('')
                    
            try:
                if  tree_asli == 'fnom':
                    
                    if (arr_asli[arr_a][i + 1] != 'fnom' and (arr_asli[arr_a][i + 3] == 'fprep' or arr_asli[arr_a][i + 3] == 'fnom')): 
                        file1.append (f'{tree_g} has{arr_asli[arr_a][i + 1]} {arr_gabungan[arr_a][i + 2]}')#fnom nn fnom
                    if (arr_asli[arr_a][i + 1] != 'fnom' and arr_asli[arr_a][i + 1] != 'fadje' and arr_asli[arr_a][i + 1] != 'fnum' and arr_asli[arr_a][i + 3] != 'fnom'):  #fnom normal
                        file1.append (f'{tree_g} hasfnom {tree_g}a ')
                        file1.append (f'{tree_g}a has{arr_asli[arr_a][i + 1]} {arr_gabungan[arr_a][i + 2]} ')
                        file1.append (f'{tree_g} hasfnom {tree_g}b ')
                        file1.append (f'{tree_g}b has{arr_asli[arr_a][i + 3]} {arr_gabungan[arr_a][i + 4]} ')
                        file1.append (f'{tree_g} type {tree_asli} ')
                        file1.append (f'{tree_g}a type {tree_asli} ')
                        file1.append (f'{tree_g}b type {tree_asli} ')
                    if (arr_asli[arr_a][i + 1] != 'fnom' and arr_asli[arr_a][i + 3] == 'cc'):  #fnom cc
                        file1.append (f'{tree_g} hasfnom {tree_g}a ')
                        file1.append (f'{tree_g}a has{arr_asli[arr_a][i + 1]} {arr_gabungan[arr_a][i + 2]} ')
                        file1.append (f'{tree_g} hasfnom {tree_g}b ')
                        file1.append (f'{tree_g}b has{arr_asli[arr_a][i + 3]} {arr_gabungan[arr_a][i + 4]} ')
                        file1.append (f'{tree_g} hasfnom {tree_g}c ')
                        file1.append (f'{tree_g}c has{arr_asli[arr_a][i + 5]} {arr_gabungan[arr_a][i + 6]} ')
                        file1.append (f'{tree_g}  type {tree_asli} ')
                        file1.append (f'{tree_g}a type {tree_asli} ')
                        file1.append (f'{tree_g}b type {tree_asli} ')   
                        file1.append (f'{tree_g}c type {tree_asli} ')
            except:
                file1.append('')
            
            try:
                if  tree_asli == 'fnum':
                    if (arr_asli[arr_a][i + 1] != 'fnum' and (arr_asli[arr_a][i + 3] == 'fprep' or 
                        arr_asli[arr_a][i + 3] == 'fnom')): 
                        file1.append (f'{tree_g} has{arr_asli[arr_a][i + 1]} {arr_gabungan[arr_a][i + 2]}')#fprep nn fprep
                    if (arr_asli[arr_a][i + 1] != 'fnom' and arr_asli[arr_a][i + 1] != 'fnum' and 
                        arr_asli[arr_a][i + 3] != 'fnom'  and arr_asli[arr_a][i + 3] != 'fprep'):  #fnum normal
                        file1.append (f'{tree_g} hasfnum {tree_g}a ')
                        file1.append (f'{tree_g}a has{arr_asli[arr_a][i + 1]} {arr_gabungan[arr_a][i + 2]} ')
                        file1.append (f'{tree_g} hasfnum {tree_g}b ')
                        file1.append (f'{tree_g}b has{arr_asli[arr_a][i + 3]} {arr_gabungan[arr_a][i + 4]} ')
                        file1.append (f'{tree_g} type {tree_asli} ')
                        file1.append (f'{tree_g}a type {tree_asli} ')
                        file1.append (f'{tree_g}b type {tree_asli} ') 
            except:
                file1.append('')
            
            try:
                if  tree_asli == 'fverb': #fverb normal
                        if arr_asli[arr_a][i + 3] == 'fverb':
                            file1.append (f'{tree_g} has{arr_asli[arr_a][i + 1]} {arr_gabungan[arr_a][i + 2]}')
                        if (arr_asli[arr_a][i + 1] != 'fverb' and arr_asli[arr_a][i + 3] == 'cc'):  #fnom cc
                            file1.append (f'{tree_g} hasfnom {tree_g}a ')
                            file1.append (f'{tree_g}a has{arr_asli[arr_a][i + 1]} {arr_gabungan[arr_a][i + 2]} ')
                            file1.append (f'{tree_g} hasfnom {tree_g}b ')
                            file1.append (f'{tree_g}b has{arr_asli[arr_a][i + 3]} {arr_gabungan[arr_a][i + 4]}')
                            file1.append (f'{tree_g} hasfnom {tree_g}c ')
                            file1.append (f'{tree_g}c has{arr_asli[arr_a][i + 5]} {arr_gabungan[arr_a][i + 6]} ')
                            file1.append (f'{tree_g}  type {tree_asli} ')
                            file1.append (f'{tree_g}a type {tree_asli} ')
                            file1.append (f'{tree_g}b type {tree_asli} ')   
                            file1.append (f'{tree_g}c type {tree_asli} ')
                        else:  
                            file1.append (f'{tree_g} type {tree_asli}')
                            file1.append (f'{tree_g}a type {tree_asli} ')
                            file1.append (f'{tree_g}b type {tree_asli} ')
                            file1.append (f'{tree_g} hasfverb {tree_g}a ')
                            file1.append (f'{tree_g}a has{arr_asli[arr_a][i + 1]} {arr_gabungan[arr_a][i + 2]} ')
                            file1.append (f'{tree_g} hasfverb {tree_g}b ')
                            file1.append (f'{tree_g}b has{arr_asli[arr_a][i + 3]} {arr_gabungan[arr_a][i + 4]} ')
            except:
                file1.append('')
                        
            try:
                if  tree_asli == 'fprep':
                    if (arr_asli[arr_a][i + 1] != 'fprep' and (arr_asli[arr_a][i + 3] == 'fprep' or 
                        arr_asli[arr_a][i + 3] == 'fnom')): 
                        file1.append (f'{tree_g} has{arr_asli[arr_a][i + 1]} {arr_gabungan[arr_a][i + 2]} ')#fprep nn fprep
                    if (arr_asli[arr_a][i + 1] != 'fprep' and arr_asli[arr_a][i + 1] != 'fnum' and 
                        arr_asli[arr_a][i + 3] != 'fnom'  and arr_asli[arr_a][i + 3] != 'fprep'):  #fadje normal
                        file1.append (f'{tree_g} hasfprep {tree_g}a ')
                        file1.append (f'{tree_g}a has{arr_asli[arr_a][i + 1]} {arr_gabungan[arr_a][i + 2]} ')
                        file1.append (f'{tree_g} hasfprep {tree_g}b ')
                        file1.append (f'{tree_g}b has{arr_asli[arr_a][i + 3]} {arr_gabungan[arr_a][i + 4]} ')
                        file1.append (f'{tree_g} type {tree_asli} ')
                        file1.append (f'{tree_g}a type {tree_asli} ')
                        file1.append (f'{tree_g}b type {tree_asli} ') 
            except:
                file1.append('')
            
            try:
                if  tree_asli == 'fadje':
                    if (arr_asli[arr_a][i + 1] != 'fadje' and (arr_asli[arr_a][i + 3] == 'fprep' or 
                        arr_asli[arr_a][i + 3] == 'fnom')): 
                        file1.append (f'{tree_g} has{arr_asli[arr_a][i + 1]} {arr_gabungan[arr_a][i + 2]} ')#fadje nn fadje
                    if (arr_asli[arr_a][i + 1] != 'fadje' and arr_asli[arr_a][i + 1] != 'fnum' and 
                        arr_asli[arr_a][i + 3] != 'fnom'):  #fadje normal
                        file1.append (f'{tree_g} hasfadje {tree_g}a ')
                        file1.append (f'{tree_g}a has{arr_asli[arr_a][i + 1]} {arr_gabungan[arr_a][i + 2]} ')
                        file1.append (f'{tree_g} hasfadje {tree_g}b  ')
                        file1.append (f'{tree_g}b has{arr_asli[arr_a][i + 3]} {arr_gabungan[arr_a][i + 4]} ')
                        file1.append (f'{tree_g} type {tree_asli} ')
                        file1.append (f'{tree_g}a type {tree_asli} ')
                        file1.append (f'{tree_g}b type {tree_asli} ') 
            except:
                file1.append('')
                    
            try:        
                if  tree_asli == 'pewatas':
                    if (arr_asli[arr_a][i + 3] == 'fnom' or arr_asli[arr_a][i + 3] == 'fprep' or arr_asli[arr_a][i + 3] == 'fverb'): #Pew nn Fnom
                        file1.append (f'{tree_g} has{arr_asli[arr_a][i + 1]} {arr_gabungan[arr_a][i + 2]} ')          
                    else:
                        file1.append (f'{tree_g}a type pewatas ')
                        file1.append (f'{tree_g}b type pewatas ')
                        file1.append (f'{tree_g}c type pewatas ')  
                        file1.append (f'{tree_g}a has{arr_asli[arr_a][i + 1]} {arr_gabungan[arr_a][i + 2]} ')
                        file1.append (f'{tree_g} haspewatas {tree_g}a ')
                        file1.append (f'{tree_g}b has{arr_asli[arr_a][i + 3]} {arr_gabungan[arr_a][i + 4]} ')
                        file1.append (f'{tree_g} haspewatas {tree_g}b ') 
                        file1.append (f'{tree_g}c has{arr_asli[arr_a][i + 5]} {arr_gabungan[arr_a][i + 6]} ')
                        file1.append (f'{tree_g} haspewatas {tree_g}c ') 
                        file1.append (f'{tree_g} type {tree_asli} ')        
            except:
                file1.append ('')

    return arr_asli, arr_gabungan, file1   