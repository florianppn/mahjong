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

class StatisticView(Text):

    def __init__(self, frame:Frame, mahjong:Mahjong):
        super().__init__(frame, height = 2, width = 25)
        self.__frame = frame
        self.__mahjong = mahjong
        self.insert(END, "Hello World !")

