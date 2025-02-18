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
from model.shape import *
from view.GridView import GridView
###########################################

class HelpMenuController(Menubutton):

    def __init__(self, tk:Tk, mahjong:Mahjong, grid_view:GridView):
        super().__init__(tk, text="Aide", width=20, borderwidth=2, relief=RAISED, bg='gray', activebackground='darkorange', cursor="hand2")
        self.__tk = tk
        self.__mahjong = mahjong
        self.__grid_view = grid_view

        menu_options = Menu(self, tearoff = 0)
        menu_shape = Menu(menu_options, tearoff = 0)
        self.configure(menu=menu_options)
        menu_options.add_command(label="Montrer une carte", command=lambda:self.show_card())
        menu_options.add_command(label="Montrer un couple", command=lambda:self.show_card_couple())
        menu_options.add_command(label="Retour en arrière", command=lambda:self.back())

    def show_card(self) -> None:
        move = self.__mahjong.one_move()
        self.__grid_view.show_card(move[0][0], move[0][1])

    def show_card_couple(self) -> None:
        move = self.__mahjong.one_move()
        self.__grid_view.show_card(move[0][0], move[0][1])
        self.__grid_view.show_card(move[1][0], move[1][1])

    def back(self) -> None:
        self.__mahjong.add()