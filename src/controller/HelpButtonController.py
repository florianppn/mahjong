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
from view.GridView import GridView
###########################################

class HelpButtonController(Frame):

    def __init__(self, tk:Tk, mahjong:Mahjong, grid_view:GridView):
        super().__init__(tk)
        self.__tk = tk
        self.__mahjong = mahjong
        self.__grid_view = grid_view

        Button(self, text="Montrer une carte", command=lambda:self.show_card()).pack(side=TOP)
        Button(self, text="Montrer une paire", command=lambda:self.show_card_couple()).pack(side=TOP)
        Button(self, text="Retour arrière", command=lambda:self.back()).pack(side=TOP)

    def show_card(self) -> None:
        move = self.__mahjong.one_move()
        self.__grid_view.show_card(move[0][0], move[0][1])

    def show_card_couple(self) -> None:
        move = self.__mahjong.one_move()
        self.__grid_view.show_card(move[0][0], move[0][1])
        self.__grid_view.show_card(move[1][0], move[1][1])

    def back(self) -> None:
        self.__mahjong.add()
