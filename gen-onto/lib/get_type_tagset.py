# #mendapatkan type dari Tagset

def get_type_tagset(arr_asli, arr_gabungan, file1):
    for arr_a in range(len(arr_asli)):
        for i in range(len(arr_asli[arr_a])-1):
            tree_asli = arr_asli[arr_a][i]
            next_tree_asli = arr_asli[arr_a][i + 1]
            tree_g = arr_gabungan[arr_a][i]
            next_tree_g = arr_gabungan[arr_a][i + 1]

            if tree_asli == 'nn': 
                file1.append(arr_gabungan[arr_a][i+1] + " type " + arr_asli[arr_a][i])
            if tree_asli == 'sc': 
                file1.append(arr_gabungan[arr_a][i+1] + " type " + arr_asli[arr_a][i])
            if tree_asli == 'vb': 
                file1.append(arr_gabungan[arr_a][i+1] + " type " + arr_asli[arr_a][i])
            if tree_asli == 'nnp': 
                file1.append(arr_gabungan[arr_a][i+1] + " type " + arr_asli[arr_a][i])
            if tree_asli == 'jj': 
                file1.append(arr_gabungan[arr_a][i+1] + " type " + arr_asli[arr_a][i])
            if tree_asli == 'rb': 
                file1.append(arr_gabungan[arr_a][i+1] + " type " + arr_asli[arr_a][i])
            if tree_asli == 'in': 
                file1.append(arr_gabungan[arr_a][i+1] + " type " + arr_asli[arr_a][i])
            if tree_asli == 'cd': 
                file1.append(arr_gabungan[arr_a][i+1] + " type " + arr_asli[arr_a][i])
            if tree_asli == 'cc': 
                file1.append(arr_gabungan[arr_a][i+1] + " type " + arr_asli[arr_a][i])
            if tree_asli == 'pr': 
                file1.append(arr_gabungan[arr_a][i+1] + " type " + arr_asli[arr_a][i])
            if tree_asli == 'prp': 
                file1.append(arr_gabungan[arr_a][i+1] + " type " + arr_asli[arr_a][i])
            if tree_asli == 'md': 
                file1.append(arr_gabungan[arr_a][i+1] + " type " + arr_asli[arr_a][i])
            if tree_asli == 'fw': 
                file1.append(arr_gabungan[arr_a][i+1] + " type " + arr_asli[arr_a][i])
            if tree_asli == 'neg': 
                file1.append(arr_gabungan[arr_a][i+1] + " type " + arr_asli[arr_a][i])
            if tree_asli == 'dt': 
                file1.append(arr_gabungan[arr_a][i+1] + " type " + arr_asli[arr_a][i])
            if tree_asli == 'nnd': 
                file1.append(arr_gabungan[arr_a][i+1] + " type " + arr_asli[arr_a][i])
            if tree_asli == 'sym': 
                file1.append(arr_gabungan[arr_a][i+1] + " type " + arr_asli[arr_a][i])
            if tree_asli == 'rp': 
                file1.append(arr_gabungan[arr_a][i+1] + " type " + arr_asli[arr_a][i])
            if tree_asli == 'OD': 
                file1.append(arr_gabungan[arr_a][i+1] + " type " + arr_asli[arr_a][i])
            if tree_asli == 'x': 
                file1.append(arr_gabungan[arr_a][i+1] + " type " + arr_asli[arr_a][i])
            if tree_asli == 'wh': 
                file1.append(arr_gabungan[arr_a][i+1] + " type " + arr_asli[arr_a][i])
            if tree_asli == 'uh': 
                file1.append(arr_gabungan[arr_a][i+1] + " type " + arr_asli[arr_a][i])

    return arr_asli, arr_gabungan, file1
