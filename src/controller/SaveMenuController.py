# -*- coding: utf-8 -*-

###########################################
#                libraries                #
###########################################
import pickle
from tkinter import *
###########################################

###########################################
#                modules                  #
###########################################
from model.shape import *
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
        try:
            backup = {
                "grid": self.__mahjong.get_grid(),
                "copy_grid": self.__mahjong.get_grid_copy(),
                "rows": self.__mahjong.get_rows(), 
                "columns": self.__mahjong.get_columns(),
                "cards": self.__mahjong.get_cards(),
                "move_history": self.__mahjong.get_move_history(),
                "shape": self.__mahjong.get_shape()
                }
            file = open("./save/save", "wb")
            pickle.dump(backup, file)
            file.close()
        except Exception as e:
            raise Exception(f"An unexpected error has occurred: {e}")

    def open_save(self) -> None:
        try:
            file = open("./save/save", "rb")
            save = pickle.load(file)
            file.close()
            self.__mahjong.set_grid(save["grid"])
            self.__mahjong.set_grid_copy(save["copy_grid"])
            self.__mahjong.set_rows(save["rows"])
            self.__mahjong.set_columns(save["columns"])
            self.__mahjong.set_cards(save["cards"])
            self.__mahjong.set_move_history(save["move_history"])
            self.__mahjong.set_shape(save["shape"])
        except:
            raise Exception("Something went wrong when opening the file")

