# -*- coding: utf-8 -*-

###########################################
#                libraries                #
###########################################
from tkinter import *
###########################################

###########################################
#                modules                  #
###########################################
from controller.ControllerGame import ControllerGame
###########################################

if __name__ == "__main__":

    controller = ControllerGame()
    controller.run()