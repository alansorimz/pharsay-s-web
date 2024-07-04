import numpy as np

def parent_read_sentence(file):
    def kalimat(x, file):
        result = []
        for i in range(file.shape[0]):
            if(file[i,0] == x): 
                result.append(file[i,2])
                if(file[i,1] != 'hasbPre' and file[i,1] != 'hascObj' and 
                file[i,1] != 'hasdPel' and file[i,1] != 'haseKet' and 
                file[i,1] != 'hasFnom' and file[i,1] != 'hasFadje' and
                file[i,1] != 'hasFverb' and file[i,1] != 'hasFnum' and
                file[i,1] != 'hasPewatas' and file[i,1] != 'hasKlausa' and
                file[i,1] != 'hasFprep' and file[i,1] != 'hasZnext' and
                file[i,1] != 'hasaSub' and file[i,1] != 'hasNext'):
                    temp = [file[i,0], file[i,1], file[i,2]]
                    res_kalimat.append(temp)            
                
        result = np.array(result)

        for i in result:
            kalimat(i, file)
    
    res_kalimat = []
    temp_res_kalimat = []

    for i, f in enumerate(file):
        stc = f"s{i + 1}" 
        kalimat(stc, file)

        if len(res_kalimat) == 0: continue
        
        temp_res_kalimat.append(res_kalimat)
        res_kalimat = []
    
    return temp_res_kalimat
