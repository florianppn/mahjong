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

class OptionsMenuController(Menubutton):

    def __init__(self, gui, menu:Menu, mahjong:Mahjong):
        super().__init__(menu, text="Options", width=20, borderwidth=2, relief=RAISED, bg='gray', activebackground='darkorange', cursor="hand2")
        self.__gui = gui
        self.__menu = menu
        self.__mahjong = mahjong

        menu_options = Menu(self, tearoff = 0)
        menu_shape = Menu(menu_options, tearoff = 0)
        self.configure(menu=menu_options)
        menu_options.add_command(label="Nouvelle partie", command=lambda:(self.__mahjong.replay(), self.__gui.show(0)))
        menu_options.add_command(label="Réessayer", command=lambda:(self.__mahjong.retry(), self.__gui.show(0)))
        menu_options.add_cascade(label="Forme de la grille", menu=menu_shape)
        menu_shape.add_command(label="Classique", command=lambda:self.set_shape(ClassicShape()))
        menu_shape.add_command(label="Rectangle", command=lambda:self.set_shape(RectangleShape()))
        menu_shape.add_command(label="Donut", command=lambda:self.set_shape(DonutShape()))
        menu_shape.add_command(label="Double", command=lambda:self.set_shape(DoubleShape()))
        menu_shape.add_command(label="Losange", command=lambda:self.set_shape(DiamondShape()))
        menu_shape.add_command(label="Croix", command=lambda:self.set_shape(CrossShape()))

    def set_shape(self, shape:ShapeStrategy) -> None:
        self.__mahjong.set_shape(shape)
        self.__mahjong.replay()
        self.__gui.show(0)
