# -*- coding: utf-8 -*-

###########################################
#                libraries                #
###########################################
from tkinter import *
###########################################

###########################################
#                modules                  #
###########################################
from model.Mahjong import Mahjong
###########################################

class ActionButtonController(Frame):

    def __init__(self, tk:Tk, mahjong:Mahjong):
        super().__init__(tk)
        self.__tk = tk
        self.__mahjong = mahjong

        Button(self, text="Quitter", command=lambda:(self.quit(), self.destroy())).pack(side=LEFT)
        Button(self, text="Sauvegarder", command=lambda:None).pack(side=LEFT)
