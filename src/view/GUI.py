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

    def show_game(self):
        mouse_controller = MouseController(self.__mahjong)
        self.bind('<Button-1>', mouse_controller.mouse_clicked)
        left_frame = Frame(self, width=200, height=800)
        left_frame.pack(side=LEFT)
        StatisticView(left_frame, self.__mahjong).pack(side=TOP)

        grid_view = GridView(self, self.__mahjong)
        grid_view.pack(side=LEFT)

        right_frame = Frame(self, width=200, height=800)
        right_frame.pack(side=RIGHT)
        HelpButtonController(self, self.__mahjong, grid_view).pack(side=TOP)
        ActionButtonController(self, self.__mahjong).pack(side=TOP)

    def show_end(self):
        pass
