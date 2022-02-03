# Code executé à l'allumage de la RAspberry Pie (pour changer le fichier, aller dans /etc/xdg/autostart/display.desktop)
import os,time
# Bibliothèque pour executer des commandes console et rajouter du temps entre les actions
import re
# Bibliothèque pour récupérer les résultats de l'algo TinyYoloV4
import numpy as np
#Commandes pour relier le programme à une sortie audio bluetooth
# os.system("rfkill block bluetooth")
# time.sleep(5)
os.system("rfkill unblock all")
time.sleep(2)
#os.system("bluetoothctl trust  B8:D5:0B:AF:A5:41")
#os.system("bluetoothctl trust  8F:B3:F2:E1:E5:E8")
time.sleep(2)
#os.system("bluetoothctl remove 8F:B3:F2:E1:E5:E8")
#os.system("bluetoothctl pair B8:D5:0B:AF:A5:41 && bluetoothctl connect B8:D5:0B:AF:A5:41")
#os.system("bluetoothctl pair 8F:B3:F2:E1:E5:E8 && bluetoothctl connect 8F:B3:F2:E1:E5:E8")
time.sleep(10)
#Execution du programme principal
exec(open("pfe.py").read())