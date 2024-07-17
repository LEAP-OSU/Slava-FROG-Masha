import numpy as np
from PIL import Image
from PCGPA import *
import matplotlib.pyplot as plt


FROG_path=r"example\24.4.txtSpecScan"
#r"c:\Users\ichth\OneDrive\Desktop\Chini Lab\SHG-FROG\python frog\frog3\10psi_Kr_FullE_2W_3pairCMs_6mmCaF2_1.tif"
#frog=Image.open(FROG_path)
#frog=np.array(frog)

T, W, frog=load_frog(r"C:/Users/ichth/OneDrive/Desktop/Chini Lab/Slava-FROG/example/24.4.txtSpecScan")
T,W,frog=preprocess_frog(T,W,frog)

Nbin=4
#determine size
Int_t=np.sum(frog,axis=1)
Int_w=np.sum(frog,axis=0)
print(len(T),len(Int_t),len(Int_w))
plt.plot(T,Int_t)
plt.show()
plt.plot(Int_w)
plt.show()
E_part=0.9 #level to equalize size

Et=np.sum(Int_t)
It0=1
while np.sum(Int_t[:It0]) < Et*E_part : It0 += 1
It1=len(Int_t)
while np.sum(Int_t[It1:]) < Et*E_part : It1 -= 1
dt0=(T[It0]-T[It1-1])/Nbin
#    print(It0,It1)