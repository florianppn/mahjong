# -*- coding: utf-8 -*-

###########################################
#                libraries                #
###########################################
from tkinter import *
###########################################

###########################################
#                modules                  #
###########################################
from model.shape import *
from view.GUI import GUI
from model import Mahjong
###########################################

if __name__ == "__main__":

    mahjong = Mahjong(8, 8, 33, ClassicShape())
    gui = GUI(mahjong)
    gui.mainloop()