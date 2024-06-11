#cari letak komponen tree
import numpy as np

cari = ['s','a_sub','b_pre','c_obj','d_pel','e_ket','cc','sc','fnom','fnum','fprep','fket','fverb','fadje','pewatas','konj','subord','klausa']
def find(arr):
  x = np.array(arr)
  ls = np.where(x == 's')
  lsub = np.where(x == 'a_sub')
  lpre = np.where(x == 'b_pre')
  lobj = np.where(x == 'c_obj')
  lpel = np.where(x == 'd_pel')
  lket = np.where(x == 'e_ket')
  lcc = np.where(x == 'cc')
  lsc = np.where(x == 'sc')
  lfnom = np.where(x == 'fnom')
  lfnum = np.where(x == 'fnum')
  lfprep = np.where(x == 'fprep')
  lfket = np.where(x == 'fket')
  lfverb = np.where(x == 'fverb')
  lfadje = np.where(x == 'fadje')
  lpewatas = np.where(x == 'pewatas')
  lkonj = np.where(x == 'konj')
  lsubord = np.where(x == 'subord')
  lklausa = np.where(x == 'klausa')

  ls_ = ls[0].tolist()
  lsub_ = lsub[0].tolist()
  lpre_ = lpre[0].tolist()
  lobj_ = lobj[0].tolist()
  lpel_ = lpel[0].tolist()
  lket_ = lket[0].tolist()
  lcc_ = lcc[0].tolist()
  lsc_ = lsc[0].tolist()
  lfnom_ = lfnom[0].tolist()
  lfnum_ = lfnum[0].tolist()
  lfprep_ = lfprep[0].tolist()
  lfket_ = lfket[0].tolist()
  lfverb_ = lfverb[0].tolist()
  lfadje_ = lfadje[0].tolist()
  lpewatas_ = lpewatas[0].tolist()
  lkonj_ = lkonj[0].tolist()
  lsubord_ = lsubord[0].tolist()
  lklausa_ = lklausa[0].tolist()

  return {
      's': ls_,
      'a_sub': lsub_,
      'b_pre': lpre_,
      'c_obj': lobj_,
      'd_pel': lpel_,
      'e_ket': lket_,
      'cc' : lcc_,
      'sc' : lsc_,
      'fnom': lfnom_,
      'fnum': lfnum_,
      'fprep': lfprep_,
      'fket': lfket_,
      'fverb': lfverb_,
      'fadje': lfadje_,
      'pewatas': lpewatas_,
      'konj': lkonj_,
      'subord': lsubord_,
      'klausa': lklausa_
  }
