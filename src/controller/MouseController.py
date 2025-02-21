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
from view import *
###########################################

class MouseController:
    """Représente les actions liées au click de la souris."""

    def __init__(self, gui, mahjong:Mahjong, grid_view:GridView):
        self.__gui = gui
        self.__mahjong = mahjong
        self.__grid_view = grid_view

    def mouse_clicked(self, event):
        """Traitement du click de la souris."""
        x0, y0 = self.__mahjong.get_x0(), self.__mahjong.get_y0()
        cx, cy = self.__mahjong.get_cx(), self.__mahjong.get_cy()
        rows, columns = self.__mahjong.get_rows(), self.__mahjong.get_columns()
        i, j = (event.y-y0)//cy, (event.x-x0)//cx
        if i in range(rows) and j in range(columns):
            self.to_click(i, j, rows, columns)

    def to_click(self, i, j, rows, columns):
        """Action lorsque le click a eu lieu sur une carte."""
        grid = self.__mahjong.get_grid()
        click1, click2 = self.__mahjong.get_click1(), self.__mahjong.get_click2()
        if grid[i][j] == []:
            self.__mahjong.set_click1(()), self.__mahjong.set_click2(())
        elif click1 == ():
            self.__mahjong.set_click1((i, j)), self.__mahjong.set_click2(())
        elif click2 == ():
            self.__mahjong.set_click2((i, j))
            self.__mahjong.remove()
            self.check_game_status()
            self.__mahjong.set_click1(()), self.__mahjong.set_click2(())
        else:
            self.__mahjong.set_click1(()), self.__mahjong.set_click2(())
            

    def check_game_status(self) -> None:
        """etat du jeu."""
        if (self.__mahjong.is_empty()):
            self.__gui.show(1)
        elif (self.__mahjong.is_blocked()):
            self.__gui.show(2)
