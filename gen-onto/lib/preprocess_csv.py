

def preprocess_csv(arr, counter_tree, tree_dict):
    arr_asli = []

    for i in arr:
        arr_asli.append(i.split())

    return save_arr_with_number(arr_asli, counter_tree, tree_dict)
    

def save_arr_with_number(arr_asli, counter_tree, tree_dict):
    arr_gabungan = []
    for i in arr_asli:
        temp = []
        for j in range(len(i)):
            if i[j] in tree_dict:
                curr = i[j]
                counter_tree[curr] += 1
                temp.append(curr+str(counter_tree[curr]))
            else:
                temp.append(i[j])
        arr_gabungan.append(temp)
    
    return arr_asli, arr_gabungan, counter_tree, tree_dict