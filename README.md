# TelS63
lecteur de mp3 piloté par un téléphone à cadran socotel s63 à l'aide d'un raspberry pi0

1. connecter le fil rouge du cadran au pin gpio4 du raspberry pi et le fil rouge/blanc sur un pin GND(voir le schéma)
2. créer le dossier s63 dans le dossier pi du raspberry, y copier les fichiers Rotarydial.py Sons.py et __init__.py
3. copier le Fichier TelS63-1.py dans /home/pi
4. dans le terminal faire : 
```
chmod +x /home/pi/TelS63-1.py
```

5. Installer supervisor pour que le programme démarre automatiquement au boot : 
```
sudo apt install supervisor
```
6. Ajouter les lignes suivantes à la fin du fichier /etc/supervisor/supervisord.conf : 


```
 ; TelS63
 [program:TelS63]
 command= python /home/pi/TelS63-1.py
 autostart=true
 autorestart=true
```


7. Créer un dossier sons dans /home/pi et y copier les fichiers mp3 que l'on souhaite, les fichiers doivent être renommés en 1.mp3, 2.mp3... jusqu'à 10.mp3

## Liens qui m'ont aidé:

* pour le cablage : https://github.com/revolunet/s63
* pour le code : https://github.com/hnesland/aselektriskbureau
* pour rajouter une sortie audio jack au raspberry pi0 : https://wiki.mchobby.be/index.php?title=RASP-PIZERO-Audio
* et ici (option 1) pour activer la sortie audio : https://learn.adafruit.com/adding-basic-audio-ouput-to-raspberry-pi-zero/pi-zero-pwm-audio

On peut aussi acheter un petit adaptateur HDMI-Jack ou prendre un raspberry pi B qui a déjà une sortie audio (mais un peu difficile à caser dans le boitier du téléphone).
