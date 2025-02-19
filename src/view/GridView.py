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

class GridView(Canvas, ModelObserver):

    def __init__(self, tk:Tk, mahjong:Mahjong):
        super().__init__(tk, width=650, height=800, bg="light grey", highlightthickness=2, highlightbackground="black")
        self.__tk = tk
        self.__mahjong = mahjong
        self.__mahjong.add_observer(self)
        self.__cards = [PhotoImage(file = f"./resources/assets/c{str(i)}.gif") for i in range(34)]
        self._paint_component()

    def _paint_component(self):
        """Dessine la grille de jeu."""
        self.delete(ALL)
        x0, y0 = self.__mahjong.get_x0(), self.__mahjong.get_y0()
        cx, cy = self.__mahjong.get_cx(), self.__mahjong.get_cy()
        click1, click2 = self.__mahjong.get_click1(), self.__mahjong.get_click2()
        grid = self.__mahjong.get_grid()
        rows, columns = self.__mahjong.get_rows(), self.__mahjong.get_columns()
        color = "yellow"
        for i in range(rows):  
            for j in range(columns):
                if grid[i][j] != []:
                    if i%2 == 0 and j%2 == 0:
                        color = "pink"
                    elif i%2 == 1 and j%2 == 1:
                        color = "brown"
                    else:
                        color = "orange"
                    self.create_rectangle(x0+cx*j+5, y0+cy*i+5, x0+cx*j+cx-5, y0+cy*i+cy-5, outline = color, width = 3) 
                    self.create_image(x0+cx*j+cx/2+1, y0+cy*i+cy/2, image = self.__cards[grid[i][j][0]])
        if(click1 != () and len(grid[click1[0]][click1[1]]) != 0):
            i, j = click1
            self.create_rectangle(x0+cx*j+5, y0+cy*i+5, x0+cx*j+cx-5, y0+cy*i+cy-5, outline = "black", width = 3)
        if(click2 != () and len(grid[click2[0]][click2[1]]) != 0):
            i, j = click2
            self.create_rectangle(x0+cx*j+5, y0+cy*i+5, x0+cx*j+cx-5, y0+cy*i+cy-5, outline = "black", width = 3)

    def show_card(self, i:int, j:int) -> None:
        x0, y0 = self.__mahjong.get_x0(), self.__mahjong.get_y0()
        cx, cy = self.__mahjong.get_cx(), self.__mahjong.get_cy()
        self.create_rectangle(x0+cx*j+5, y0+cy*i+5, x0+cx*j+cx-5, y0+cy*i+cy-5, outline = "yellow", width = 3)

    def model_update(self, o:object) -> None:
        self._paint_component()

    

