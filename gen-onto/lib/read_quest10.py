import numpy as np

def read_quest10(file):
    #10. Jawaban Singkat
    res_a = []
    def pertanyaan10a(x,file):
        result = []
        for i in range(file.shape[0]):
            if(file[i,0]==x): 
                result.append(file[i,2])
                if(file[i,1] != 'hasbPre' and file[i,1] != 'hascObj' and 
                    file[i,1] != 'hasdPel' and file[i,1] != 'haseKet' and 
                    file[i,1] != 'hasFnom' and file[i,1] != 'hasFadje' and
                    file[i,1] != 'hasFverb' and file[i,1] != 'hasFnum' and
                    file[i,1] != 'hasPewatas' and file[i,1] != 'hasKlausa' and
                    file[i,1] != 'hasFprep' and file[i,1] != 'hasZnext' and
                    file[i,1] != 'hasaSub'):
                        print(file[i,2],end=' ')
                        res_a.append(file[i,2])
                
            if("obj" in file[i,0]):  
                break;

        result = np.array(result)
    
        for i in result:
            pertanyaan10a(i, file)
        
    temp_res_soal = []

    def soal10 (x, file):
        pertanyaan10a(x,file)

    for i, f in enumerate(file):
        stc = f"s{i + 1}" 
        soal10(stc, file)

        # tempa = ''

        # if len(res_a) != 0:
        #     tempa = ' '.join(res_a).strip() + '....' + ' '
        #     temp_res_soal.append(tempa)
        
        # if len(res_a) == 0:
        #     continue
        if res_a:
            tempa = ' '.join(res_a).strip()
            # Hapus 'adalah' jika ada 'merupakan'
            if 'merupakan' in tempa and 'adalah' in tempa:
                tempa = tempa.replace('adalah', '').strip()
            tempa = tempa + '.....'
            temp_res_soal.append(tempa)
        
        res_a = []

    return temp_res_soal
