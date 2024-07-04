import numpy as np
# belum berhasil
def read_quest9(file):
    #9. KLASIFIKASI
    res_a = []
    def pertanyaan9(file):
        result = []
        for i in range(file.shape[0]):
            print(file[i,2],end=' ')
            res_a.append(file[i,2])
            break;
                
        result = np.array(result)
        
        for i in result:
            pertanyaan9(file)

    temp_res_soal = []
    
    def soal9(x, file):
        pertanyaan9 (file)
        
    for i, f in enumerate(file):
        stc = f"s{i + 1}" 
        soal9(stc, file)

        tempa = ''

        if len(res_a) != 0:
            tempa = "Klasifikasikan "+ ' '.join(res_a).strip() + ' berdasarkan jenisnya!' + ' '
            temp_res_soal.append(tempa)

        if len(res_a) == 0:
            continue
        
        res_a = []
    
    return temp_res_soal
