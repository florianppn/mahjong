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

class SaveMenuController(Menubutton):

    def __init__(self, tk:Tk, mahjong:Mahjong):
        super().__init__(tk, text="Fichier", width=20, borderwidth=2, relief=RAISED, bg='gray', activebackground='darkorange', cursor="hand2")
        self.__tk = tk
        self.__mahjong = mahjong

        menu = Menu(self, tearoff = 0)
        menu.add_command(label="Ouvrir", command=lambda:self.open_save())
        menu.add_command(label="Sauvegarder", command=lambda:self.save())
        menu.add_command(label="Quitter", command=lambda:(self.__tk.quit(), self.__tk.destroy()))
        self.configure(menu=menu)

    def save(self) -> None:
        pass

    def open_save(self) -> None:
        pass
