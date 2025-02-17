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

        card_button = Button(self, text="Une carte", command=lambda:self.show_card())
        card_button.config(borderwidth=2, relief=RAISED, bg='gray', activebackground='darkorange', cursor="hand2")
        card_button.grid(row=0, column=0, pady=10, padx=10)
        couple_button = Button(self, text="Une paire", command=lambda:self.show_card_couple())
        couple_button.config(borderwidth=2, relief=RAISED, bg='gray', activebackground='darkorange', cursor="hand2")
        couple_button.grid(row=0, column=1, pady=10, padx=10)
        back_button = Button(self, text="Retour arrière", command=lambda:self.back())
        back_button.config(borderwidth=2, relief=RAISED, bg='gray', activebackground='darkorange', cursor="hand2")
        back_button.grid(row=1, column=0, columnspan=2, pady=10)

    def show_card(self) -> None:
        move = self.__mahjong.one_move()
        self.__grid_view.show_card(move[0][0], move[0][1])

    def show_card_couple(self) -> None:
        move = self.__mahjong.one_move()
        self.__grid_view.show_card(move[0][0], move[0][1])
        self.__grid_view.show_card(move[1][0], move[1][1])

    def back(self) -> None:
        self.__mahjong.add()
