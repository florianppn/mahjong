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
from utils import ModelObserver
###########################################

class StatisticView(Label, ModelObserver):

    def __init__(self, frame:Frame, mahjong:Mahjong):
        super().__init__(frame, text="Cartes : "+str(mahjong.get_remaining_cards()) + " | Mouvements : "+str(mahjong.get_shots()), bg='#557788')
        self.__frame = frame
        self.__mahjong = mahjong
        self.__mahjong.add_observer(self)

    def model_update(self, o:object) -> None:
        self['text'] = "Cartes : "+str(self.__mahjong.get_remaining_cards())+" | Mouvements : "+str(self.__mahjong.get_shots())

