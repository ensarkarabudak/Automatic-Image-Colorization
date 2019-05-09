import os

sayac=0
dir_path="Frames"
frame=[]
u=len(os.listdir(dir_path))
for i in os.listdir(dir_path):
    print("Islemin Bitmesine "+str(sayac)+"/"+str(u)+" Kaldi")
    os.system("th colorize.lua Frames/"+i+" FrameOut/"+i+".png") 
    sayac=sayac+1
    
print("Islem Bitti....")


