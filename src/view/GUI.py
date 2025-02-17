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
from controller import *
###########################################

class GUI(Tk):

    def __init__(self, mahjong:Mahjong):
        super().__init__()
        self.title("Mahjong")
        self.__mahjong = mahjong
        self.show_game()
        self.config(bg='#557788')

    def show_game(self):
        mouse_controller = MouseController(self.__mahjong)
        self.bind('<Button-1>', mouse_controller.mouse_clicked)

        menu = Frame(self)
        menu.grid(row=0, column=0)
        SaveMenuController(menu, self.__mahjong).grid(row=0, column=0)
        OptionsMenuController(menu, self.__mahjong).grid(row=0, column=1)

        grid_view = GridView(self, self.__mahjong)
        grid_view.grid(row=1, column=0, columnspan=10)

        frame = Frame(self, width=200, height=800)
        frame.grid(row=1, column=11)

        StatisticView(frame, self.__mahjong).grid(row=0, column=0, pady=100)
        HelpButtonController(frame, self.__mahjong, grid_view).grid(row=1, column=0, pady=100)

    def show_end(self):
        pass
