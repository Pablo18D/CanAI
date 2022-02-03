#8F:B3:F2:E1:E5:E8
import os,time
import re
import numpy as np
#Bibliothèque pour mettre les images au même format que le réseau (416x416)
import cv2
#Bibliothèque pour jouer les fichiers audio
from pygame import mixer
os.chdir("/home/pi/EntrainerTiny2/darknet")
#Variable du nombre de tours de détection, chaque detection prend 5 secondes en moyenne. Donc 720 itérations pour 1h de fonctionnement
xixi=1
#Variable pour éviter la répétition audio de l'absence de feu
calm=0
mixer.init()
#Import de tous les sons utiles
sound_notsure=mixer.Sound('all_sound/je_ne_suis_pas_sur.wav')
sound_begin=mixer.Sound('all_sound/harry.wav')
sound_begin.set_volume(0.25)
sound_demarrage = mixer.Sound('all_sound/dem.wav')
sound_rouge = mixer.Sound('all_sound/feu_rouge_pieton.wav')
sound_bell = mixer.Sound('all_sound/bell.wav')
sound_vert = mixer.Sound('all_sound/feu_vert_pieton.wav')
no_sound = mixer.Sound('all_sound/pas_feu.wav')
#Son de démarrage 
sound_begin.play()
time.sleep(1)
sound_demarrage.play()
time.sleep(1)
#While de l'algo
while xixi<360 :
    #libcamera-still -o  /home/pi/EntrainerTiny/captures/test%d.jpg -t 1 --timelapse 10000 --vflip --hflip --tuning-file /usr/share/libcamera/ipa/raspberrypi/imx219_noir.json
#Caméra avec flip vertical et horizontal, correction des couleurs de l'image,     
    os.system("libcamera-jpeg -o  /home/pi/EntrainerTiny2/captures/test"+str(xixi)+".jpg -t 1 --vflip --hflip --tuning-file /usr/share/libcamera/ipa/raspberrypi/imx219_noir.json --heigh 1900 --width 1080")
# Resizing de l'image caméra pour rentrer dans le réseau de neurones    
    img=cv2.imread("/home/pi/EntrainerTiny2/captures/test"+str(xixi)+".jpg",1)
    img2=cv2.resize(img,(416,416))
    cv2.imwrite("/home/pi/EntrainerTiny2/captures/test"+str(xixi)+".jpg",img2)
    
    #os.system("./darknet detect cfg/custom-yolov4-tiny-detector.cfg custom-yolov4-tiny-detector_best.weights /home/pi/EntrainerTiny/captures/test1.jpg")
# Algo de détection avec darknet sous tinyyolov4 
    os.system("./darknet detector test data/obj.data  cfg/custom-yolov4-tiny-detector.cfg custom-yolov4-tiny-detector_best.weights /home/pi/EntrainerTiny2/captures/test"+str(xixi)+".jpg -ext_output < data/train.txt > resultat/result"+str(xixi)+".txt")
    #os.system("./darknet detect cfg/custom-yolov4-tiny-detector.cfg custom-yolov4-tiny-detector_best.weights /home/pi/EntrainerTiny/captures/test1.jpg -ext_output < data/train.txt > result.txt")
    
   # darknet.exe detector test data/voc.data yolo-voc.cfg yolo-voc.weights -dont_show -ext_output < data/train.txt > result.tx   
#Lecture du fichier de résultats pour la rpise de décision    
    file = open("resultat/result"+str(xixi)+".txt", "r") 
    x=file.readlines()
# Cas où aucun feu n'est détecté
    if len(x)<8:
      print("nada")
      if calm==0:
          no_sound.play()
          time.sleep(1)
          calm=1
# Cas où seul 1 feu est détecté sur l'image avec une probabilité suffisante
    elif len(x)==8:
      v1=re.split("[xy_\b\W\b]+", x[7],flags=re.IGNORECASE)
      if int(v1[2])>50 and v1[1]=="rouge":
        sound_rouge.play()
        time.sleep(1)
        print("rouge")
        calm=0
      elif int(v1[2])>50 and v1[1]=="vert":
        sound_bell.play()
        time.sleep(0.15)
        sound_vert.play()
        time.sleep(1)
        print("vert")
        calm=0
      else :
        print("précision insuffisante")
        if calm==0:
            sound_notsure.play()
            time.sleep(1)
            calm=0
# Cas où plusieurs feux sont détectés, on selectionne un écart suffisant et des boundings box différentes          
    elif len(x)>8: 
      lstclass = [];lstpercent=[];lstleft = [];lstright=[];lstwidth = [];lstdepth=[]
      for i in range( len(x)-7) :
        v1=re.split("[xy_\b\W\b]+", x[i+7],flags=re.IGNORECASE)
        if(v1[1])=="rouge":
          lstclass.append(0);lstpercent.append(int(v1[2]));lstleft.append (int(v1[4]));lstright.append(int(v1[6]));lstwidth.append(int(v1[8]));lstdepth.append(int(v1[10]))
        else:
          lstclass.append(1);lstpercent.append(int(v1[2]));lstleft.append (int(v1[4]));lstright.append(int(v1[6]));lstwidth.append(int(v1[8]));lstdepth.append(int(v1[10]))
                 
      indexmax=lstpercent.index(max(lstpercent))
      lstpercent.sort()
      
      compare= all(element == lstleft[indexmax]for element in lstleft)
      if lstpercent[-1]>40 and lstclass[indexmax]==0 and lstpercent[-1]-lstpercent[-2]>10 and compare == False :
          sound_rouge.play()
          time.sleep(1)
          print("rouge")
          calm=0
      elif lstpercent[-1]>50 and lstclass[indexmax]==1 and lstpercent[-1] - lstpercent[-2] >10 and compare == False :
          sound_bell.play()
          time.sleep(0.15)
          sound_vert.play()
          time.sleep(1)
          print("vert")
          calm=0
      else:
          print("données complexes")
          sound_notsure.play()
          time.sleep(1)
          calm=0
            
    os.system("cp predictions.jpg prediction/prediction"+str(xixi))
    xixi=xixi+1


