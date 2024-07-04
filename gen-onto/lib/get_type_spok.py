

def get_type_spok(arr_asli, arr_gabungan):
    file1 = []
    for arr_a in range(len(arr_asli)):
        for i in range(len(arr_asli[arr_a])-1):
            tree_asli = arr_asli[arr_a][i]
            next_tree_asli = arr_asli[arr_a][i + 1]
            tree_g = arr_gabungan[arr_a][i]
            next_tree_g = arr_gabungan[arr_a][i + 1]

            if tree_asli == 's': 
                file1.append(str(tree_g) + " type " + str(tree_asli))
            if tree_asli == 'sub': 
                file1.append(str(tree_g) + " type " + str(tree_asli)) 
            if tree_asli == 'pre': 
                file1.append(str(tree_g) + " type " + str(tree_asli))
            if tree_asli == 'obj': 
                file1.append(str(tree_g) + " type " + str(tree_asli))
            if tree_asli == 'pel': 
                file1.append(str(tree_g) + " type " + str(tree_asli)) 
            if tree_asli == 'ket': 
                file1.append(str(tree_g) + " type " + str(tree_asli)) 
            if tree_asli == 'fnom': 
                file1.append(str(tree_g) + " type " + str(tree_asli))
            if tree_asli == 'fprep': 
                file1.append(str(tree_g) + " type " + str(tree_asli))
            if tree_asli == 'fverb':
                file1.append(str(tree_g) + " type " + str(tree_asli))
            if tree_asli == 'pewatas':
                file1.append(str(tree_g) + " type " + str(tree_asli))
            if tree_asli == 'klausa':
                file1.append(str(tree_g) + " type " + str(tree_asli))
            if tree_asli == 'fnum':
                file1.append(str(tree_g) + " type " + str(tree_asli))
            if tree_asli == 'fadje':
                file1.append(str(tree_g) + " type " + str(tree_asli))
    
    return file1
