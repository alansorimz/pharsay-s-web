import numpy as np

# def read_quest8(file):
#     #8. VALIDASI
#     res_a = []
#     def pertanyaan8a(x, file):
#         result = []
#         for i in range(file.shape[0]):
#             if(file[i,0] == x): 
#                 result.append(file[i,2])
#                 if(file[i,1] != 'hasbPre' and file[i,1] != 'hascObj' and 
#                 file[i,1] != 'hasdPel' and file[i,1] != 'haseKet' and 
#                 file[i,1] != 'hasFnom' and file[i,1] != 'hasFadje' and
#                 file[i,1] != 'hasFverb' and file[i,1] != 'hasFnum' and
#                 file[i,1] != 'hasPewatas' and file[i,1] != 'hasKlausa' and
#                 file[i,1] != 'hasFprep' and file[i,1] != 'hasZnext' and
#                 file[i,1] != 'hasaSub'):
#                     print(file[i,2],end=' ')
#                     res_a.append(file[i,2])
                
#         result = np.array(result)
        
#         for i in result:
#             pertanyaan8a(i, file)
    
#     # res_b = []
#     # def pertanyaan8b(x, file):
#     #     result = []
#     #     for i in range(file.shape[0]):
#     #         if(file[i,0] == x): 
#     #             result.append(file[i,2])
#     #             if(file[i,1] != 'hasbPre' and file[i,1] != 'hascObj' and 
#     #             file[i,1] != 'hasdPel' and file[i,1] != 'haseKet' and 
#     #             file[i,1] != 'hasFnom' and file[i,1] != 'hasFadje' and
#     #             file[i,1] != 'hasFverb' and file[i,1] != 'hasFnum' and
#     #             file[i,1] != 'hasPewatas' and file[i,1] != 'hasKlausa' and
#     #             file[i,1] != 'hasFprep' and file[i,1] != 'hasZnext' and
#     #             file[i,1] != 'hasaSub'):
#     #                 print(file[i,2],end=' ')
#     #                 res_b.append(file[i,2])
                
#     #     result = np.array(result)
        
#     #     for i in result:
#     #         pertanyaan8b(i, file)


#     temp_res_soal = []
    
#     def soal8(x, file):
#         pertanyaan8a (x,file)

#         # pertanyaan8b (x,file)
        
#     for i, f in enumerate(file):
#         stc = f"s{i + 1}" 
#         soal8(stc, file)

#         tempa = ''
#         # tempb = ''

#         if len(res_a) != 0:
#             tempa = "Apakah "+ ' '.join(res_a).strip() + '?' + ' '
#             temp_res_soal.append(tempa)
#         # if len(res_b) != 0:
#         #     tempb = "Apakah "+ ' '.join(res_b).strip() + '?' + ' '
#         #     temp_res_soal.append(tempb)

#         if len(res_a) == 0:
#             continue
        
#         res_a = []
#         # res_b = []
    
#     return temp_res_soal


def read_quest8(file):
    # 8. VALIDASI
    temp_res_soal = []
    
    def pertanyaan8a(x, file, res_a):
        result = []
        for i in range(file.shape[0]):
            if file[i,0] == x: 
                result.append(file[i,2])
                if file[i,1] not in ['hasbPre', 'hascObj', 'hasdPel', 'haseKet', 
                                     'hasFnom', 'hasFadje', 'hasFverb', 'hasFnum', 
                                     'hasPewatas', 'hasKlausa', 'hasFprep', 
                                     'hasZnext', 'hasaSub']:
                    if file[i,2] not in res_a:  # Avoid redundancy
                        res_a.append(file[i,2])
        
        result = np.array(result)
        
        for i in result:
            pertanyaan8a(i, file, res_a)
    
    def soal8(x, file):
        res_a = []
        pertanyaan8a(x, file, res_a)
        
        if res_a:
            # Gabungkan hasil dan hapus "adalah" jika ada "merupakan"
            res_a_str = ' '.join(res_a).strip()
            if "merupakan" in res_a_str and "adalah" in res_a_str:
                res_a_str = res_a_str.replace("adalah", "").strip()
            tempa = "Apakah " + res_a_str + "?"
            temp_res_soal.append(tempa)
    
    for i, f in enumerate(file):
        stc = f"s{i + 1}" 
        soal8(stc, file)
    
    return temp_res_soal