# -*- coding: utf-8 -*-

###########################################
#                librairies               #
###########################################
from abc import ABC, abstractmethod
###########################################

class ShapeStrategy(ABC):

    @abstractmethod
    def generate_grid(self, rows:int, columns:int, cards:int):
        pass