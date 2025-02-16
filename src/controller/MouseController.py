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

class MouseController:

    def __init__(self, mahjong:Mahjong):
        self.__mahjong = mahjong

    def mouse_clicked(self, event):
        """Vérifie si une case de l'interface graphique du Mahjong est cliquable.
        Returns:
            Vrai si le clic a été effectué sur une carte sinon Faux.
        """
        x0, y0 = self.__mahjong.get_x0(), self.__mahjong.get_y0()
        cx, cy = self.__mahjong.get_cx(), self.__mahjong.get_cy()
        rows, columns = self.__mahjong.get_rows(), self.__mahjong.get_columns()
        i, j = (event.y-y0)//cy, (event.x-x0)//cx
        if i in range(rows) and j in range(columns):
            self.to_click(i, j, rows, columns)

    def to_click(self, i, j, rows, columns):
        """ """
        grid = self.__mahjong.get_grid()
        click1, click2 = self.__mahjong.get_click1(), self.__mahjong.get_click2()
        if grid[i][j] == []:
            self.__mahjong.set_click1(()), self.__mahjong.set_click2(())
        elif click1 == ():
            self.__mahjong.set_click1((i, j)), self.__mahjong.set_click2(())
        elif click2 == ():
            self.__mahjong.set_click2((i, j))
            self.__mahjong.remove()
            self.__mahjong.set_click1(()), self.__mahjong.set_click2(())
        elif click1 == click2:
            self.__mahjong.set_click1(()), self.__mahjong.set_click2(())
        else:
            self.__mahjong.set_click1(()), self.__mahjong.set_click2(())