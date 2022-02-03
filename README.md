CanAÏ
Projet porté par une équipe de 6 étudiants en dernière année à l'école d'ingénieur ECE Paris.
Avec ce projet CanAÏ, nous souhaitons proposer un appareil muni d’une caméra pouvant détecter et analyser la couleur des feux piétons. Il a pour but d'avertir les personnes malvoyantes et aveugles lors de leur déplacement en ville, de leur donner plus de sécurité et d'autonomie.
Un signal sonore indique aux utilisateurs la présence d'un feu piéton et sa couleur.
 
Comment reproduire

Connecter la Pi Caméra
Tutoriel : pj2-tutopicam-1585.pdf (gotronic.fr)
Entrainement d’un modèle de réseau de neurones sur Google Colab avec le dataset constitué préalablement
Réseau de neurones sur Google Colab : Entrainement TinyYoloV4 Feux Piétons - Colaboratory (google.com)
Tutoriel pour entraîner le modèle : AlexeyAB/darknet: YOLOv4 / Scaled-YOLOv4 / YOLO - Neural Networks for Object Detection (Windows and Linux version of Darknet ) (github.com)
Utilisez le modèle TinyYOLO pour réduire la durée de détection des images.
Amélioration de la durée et du taux de détection des images
Overclock de la carte Raspberry Pi pour augmenter son nombre d'action à la seconde
(How to Safely Overclock your Raspberry Pi 4 to 2.147GHz - Latest Open Tech From Seeed (seeedstudio.com))
Implémentation du code python sur la carte pour les différents cas d’usage
Connexion de l’enceinte Bluetooth pour transmettre le signal
Tutoriel : How to Set Up Bluetooth on a Raspberry Pi - Howchoo
