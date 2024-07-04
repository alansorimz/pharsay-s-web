

def get_sentence_spok(arr_asli, arr_gabungan, file1):
    for arr_a in range(len(arr_asli)):
        for i in range(len(arr_asli[arr_a])-1):
            tree_asli = arr_asli[arr_a][i]
            next_tree_asli = arr_asli[arr_a][i + 1]
            tree_g = arr_gabungan[arr_a][i]
            next_tree_g = arr_gabungan[arr_a][i + 1]

            if tree_asli == 's': 
                s=tree_g
            if tree_asli == 'klausa': 
                if (tree_asli == 'klausa' and arr_asli[arr_a][i-1]=='s'):
                    file1.append (f'{arr_gabungan[arr_a][0]} hasklausa {tree_g}') 
                    s=tree_g
                if (tree_asli == 'klausa' and arr_asli[arr_a][i-2]=='cc'):
                    file1.append (f'{arr_gabungan[arr_a][0]} hasklausa {tree_g}') 
                    file1.append (f'{tree_g} hascc {arr_asli[arr_a][i-1]}')
                    s=tree_g
                if (tree_asli == 'klausa' and arr_asli[arr_a][i-2]=='sc'):
                    file1.append (f'{arr_gabungan[arr_a][i-3]} hasklausa {tree_g}') 
                    file1.append (f'{arr_gabungan[arr_a][i-3]} hasasc {arr_asli[arr_a][i-1]}')
                    s=tree_g
                        
            if tree_asli == 'sub': 
                file1.append (f'{s} hasasub {tree_g}')   
                tag = (f'{tree_g}')
            if tree_asli == 'pre': 
                file1.append (f'{s} hasbpre {tree_g}')
                tag =(f'{tree_g}')
            if tree_asli == 'obj': 
                file1.append (f'{s} hascobj {tree_g}')
                tag =(f'{tree_g}')
            if tree_asli == 'pel': 
                file1.append (f'{s} hasdpel {tree_g}')
                tag =(f'{tree_g}')
            if tree_asli == 'ket': 
                file1.append (f'{s} haseket {tree_g}')
                tag =(f'{tree_g}')
            if tree_asli == 'pewatas': 
                file1.append (f'{tag} hasznext {tree_g}')
                tag=(f'{tree_g}')
            if tree_asli == 'fnom': 
                file1.append (f'{tag} hasznext {tree_g}')
                tag=(f'{tree_g}')
            if tree_asli == 'fnum': 
                file1.append (f'{tag} hasznext {tree_g}')
                tag=(f'{tree_g}')     
            if tree_asli == 'fverb': 
                file1.append (f'{tag} hasznext {tree_g}')
                tag=(f'{tree_g}')         
            if tree_asli == 'fprep': 
                file1.append (f'{tag} hasznext {tree_g}')
                tag=(f'{tree_g}')          
            if tree_asli == 'fadje': 
                file1.append (f'{tag} hasznext {tree_g}')
                tag=(f'{tree_g}')

    return arr_asli, arr_gabungan, file1

        