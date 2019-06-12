#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame

SONG_END = 0

class Sons(object):
    """ lecteur de fichiers mp3"""
    """ les fichiers doivent être renommés : x.mp3 ou x entre 1 et 10"""
    def __init__(self, num =0):
        
        global fin
        START = 0
        fin = 0
        self.digit = num
#emplacement du dossier de sons
        if self.digit != 0 and self.digit < 11:
            chemin = "/home/pi/sons/xx.mp3"
            chemin = chemin.replace("xx", str(self.digit))
	#pygame.mixer.init(freq, bits, stéréo, buffer)
            pygame.mixer.init(44100, -16, 2, 4096)
            pygame.mixer.music.load(chemin)
            pygame.mixer.music.play()

    def StartSon(self):
        #renvoie 1 si la lecture démarre
       if START == 1:
           self.StartSonCallback()
           print("start", START)
       START = 0

