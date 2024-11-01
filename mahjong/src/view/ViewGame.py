# -*- coding: utf-8 -*-

###########################################
#                libraries                #
###########################################
from tkinter import *
###########################################

###########################################
#                modules                  #
###########################################
from model.ModelObserver import ModelObserver
###########################################

class ViewGame(Frame, ModelObserver):
    """Représente la vue d'une partie de Mahjong.
    Args:
        tk: Interface mère du jeu.
        controller: Contrôleur du jeu.
        cx: Dimension d'une case en largeur si on utilise les images (adapté pour les images fournies).
        cy: Dimension d'une case en hauteur si on utilise les images (adapté pour les images fournies).
        x0: Coordonnée x du point en haut à gauche.
        y0: Coordonnée y du point en haut à gauche.
        cards_pictures: Liste des images de cartes pour le jeu.
        new_grid: Bouton pour faire une nouvelle partie.
        retry_grid: Bouton pour recommencer une partie.
        sub_container: frame contenant les boutons de contrôle (quitter et menu).
        buttons: Liste des boutons actions/recommencer.
        canvas: canvas de la vue (la grille de jeu à gauche).
        container: frame principale de la vue (le menu à droite).
    """
    
    def __init__(self, tk:Tk, controller):
        super().__init__(tk)
        ModelObserver().__init__()
        self.forget()
        self.__tk = tk
        self.__controller = controller

        self.__cx = 64
        self.__cy = 84
        self.__x0 = 55
        self.__y0 = 40
        self.__cards_pictures = [PhotoImage(file = f"../assets/c{str(i)}.gif") for i in range(1, 35)]
        
        self.__new_grid = None
        self.__retry_grid = None
        self.__sub_container = None
        self.__buttons = []
        self.__canvas = Canvas(self, height = 810, width = 610)
        self.__canvas.pack(side = LEFT)
        self.__container = self.configure_menu()

    def configure_menu(self) -> Frame:
        """Création de la frame principale.
        Returns:
            La frame principale.
        Notes:
            - la frame principale contient le menu d'interaction avec la grille.
        """
        frame = Frame(self)
        frame.pack(side = RIGHT)
        self.configure_again_buttons(frame)
        self.__end_game_text = self.configure_text_event(frame)
        self.__card_counter = self.configure_text_event(frame)
        self.configure_action_buttons(frame)
        self.__sub_container = self.configure_control_buttons(frame)
        return frame

    def configure_again_buttons(self, frame:Frame) -> None:
        """Création des boutons pour recommencer une partie.
        Args:
            frame: la frame principale du jeu.
        """
        data = [("Play again", lambda : self.__controller.play_again()),
                ("Try again", lambda : self.__controller.try_again())]
        for text, command in data:
            button = Button(frame, text = text, state = DISABLED, command = command)
            button.config(font = ("comic", 10, "bold"))
            button.pack(side = TOP, pady = 10)
            self.__buttons.append(button)
            if text == "Play again":
                self.__new_grid = button
            else:
                self.__retry_grid = button

    def configure_text_event(self, frame:Frame) -> Text:
        """Création d'un élément text pour afficher des évènements liés au déroulement du jeu.
        Args:
            frame: la frame principale du jeu.
        Returns:
            le Text.
        """
        text = Text(frame, height = 2, width = 25)
        text.pack(side = TOP, padx = 10, pady = 40)
        return text

    def configure_action_buttons(self, frame:Frame) -> None:
        """Création des différents boutons d'actions.
        Args:
            frame: La frame principale du jeu.
        Notes:
            - 4 actions possibles dans le jeu : montrer une carte, montrer deux cartes, retour en arrière et sauvegarder la partie.
        """
        data = [("Show card", lambda : self.__controller.find_playable_card()),
                ("Show pair of card", lambda : self.__controller.find_playable_card_couple()),
                ("Go back !", lambda : self.__controller.backspace()),
                ("Save here", lambda : self.__controller.back_up())]
        for text, command in data:
            button = Button(frame, text = text, command = command)
            button.config(font = ("comic", 10, "bold"))
            button.pack(side = TOP, pady = 30)
            self.__buttons.append(button)

    def configure_control_buttons(self, frame:Frame) -> Frame:
        """Création des boutons de contrôle pour la vue.
        Args:
            frame: frame principale du jeu.
        Returns:
            sous frame contenant les boutons de contrôle.
        Notes:
            - Création du bouton quitter avec une fonction associée.
            - Création du bouton menu avec une fonction associée.
        """
        sub_frame = Frame(frame)
        sub_frame.pack(side = BOTTOM)
        data = [("Quit", lambda: (self.quit(), self.destroy()), "red3", LEFT), ("Menu", lambda : self.__controller.show_menu("game"), "dodger blue", RIGHT)]
        for text, command, activecolor, side in data:
            button = Button(sub_frame, text=text, command=command)
            button.config(font=("comic", 10, "bold"), bg="white", activebackground=activecolor)
            button.pack(side=side, padx=20, pady=10)
        return sub_frame

    def get_y0(self) -> int:
        return self.__y0
    
    def get_x0(self) -> int:
        return self.__x0

    def get_cx(self) -> int:
        return self.__cx
    
    def get_cy(self) -> int:
        return self.__cy

    def model_update(self, source:object) -> None:
        """Mise à jour de la grille.
        Args:
            source: l'instance de la classe Grid.
        Notes:
            - à lieu lors d'une modification de la grille.
        """
        self.draw_grid(source.get_grid())

    def model_update_theme(self, theme:str):
        """Mise à jour de la couleur de l'arrière plan par le modèle.
        Args:
            theme: nouvelle couleur de l'arrière plan.
        Notes:
            - à lieu lors d'un changement de couleur.
        """
        self.config(bg=theme)
        self.__container.config(bg=theme)
        self.__sub_container.config(bg=theme)

    def model_update_colors(self, theme:str, bg:str, fg:str, activebackground:str, activeforeground:str) -> None:
        """Mise à jour pour la vue par le modèle.
        Args:
            theme: couleur de l'arrière plan.
            bg: couleur de fond d'un bouton.
            fg: couleur du texte d'un bouton.
            activebackground: couleur du fond d'un bouton lors du passage de la souris.
            activeforeground: couleur du texte d'un bouton lors du passage de la souris.
        Notes:
            - à lieu lors de la mise en route du jeu.
        """
        self.config(bg=theme)
        self.__container.config(bg=theme)
        self.__sub_container.config(bg=theme)
        for button in self.__buttons:
            button.config(bg=bg, fg=fg, activebackground=activebackground, activeforeground=activeforeground)

    def active_bind(self) -> None:
        """Activer le clic souris sur l'interface mère.
        Notes:
            - Utile pour l'interaction avec la grille de jeu.
        """
        self.__tk.bind('<Button-1>', self.__controller.is_clickable)

    def deactivate_bind(self) -> None:
        """Désactiver le clic souris sur l'interface mère.
        Notes:
            - Utile lorsqu'il n'y a pas lieu d'avoir une interaction avec la grille.
        """
        self.__tk.unbind('<Button-1>')

    def end_text(self, status:str=None) -> None:
        """Affiche le texte de fin de partie dans le cas où la partie est terminée.
        Args:
            status: contient le texte de fin si c'est la fin de la partie sinon ne contient rien.
        """
        if status == None:
            self.__end_game_text.config(state = NORMAL)
            self.__end_game_text.delete("0.0", END)
            self.__end_game_text.config(state = DISABLED)
        else:
            self.__end_game_text.config(state = NORMAL)
            self.__end_game_text.delete("0.0", END)
            self.__end_game_text.insert(END, status)
            self.__end_game_text.config(state = DISABLED)

    def buttons_state(self, status:bool=True) -> None:
        """Active/Désactive les boutons d'actions sur la grille en fonction de l'état de la partie (terminée/en cours).
        Args:
            status: True si la partie est en cours sinon False.
        """
        if status:
            self.__show_card.config(state = NORMAL)
            self.__show_pair_cards.config(state = NORMAL)
            self.__go_back.config(state = NORMAL)
            self.__new_grid.config(state = DISABLED)
            self.__retry_grid.config(state = DISABLED)
        else:
            self.__show_card.config(state = DISABLED)
            self.__show_pair_cards.config(state = DISABLED)
            self.__go_back.config(state = DISABLED)
            self.__new_grid.config(state = NORMAL)
            self.__retry_grid.config(state = NORMAL)

    def show_card(self, i:int, j:int, grid:[[[int]]]) -> None:
        """Dessine un rectangle autour d'une carte quand le joueur demande à voir une carte jouable.
        Args:
            i: ligne où se situe la carte.
            j: colonne où se situe la carte.
            grid: grille de jeu.
        """
        self.__canvas.create_rectangle(self.__x0+self.__cx*j+5, self.__y0+self.__cy*i+5, self.__x0+self.__cx*j+self.__cx-5, self.__y0+self.__cy*i+self.__cy-5, outline = "black", width = 3)

    def show_card_couple(self, i:int, j:int, k:int, m:int, grid:[[[int]]]) -> None:
        """Dessine un rectangle autour d'un couple de cartes quand le joueur demande à voir un couple de cartes jouables.
        Args:
            i: ligne où se situe la première carte.
            j: colonne où se situe la première carte.
            k: ligne où se situe la deuxième carte.
            m: colonne où se situe la deuxième carte.
            grid: grille de jeu.
        """
        self.__canvas.create_rectangle(self.__x0+self.__cx*j+5, self.__y0+self.__cy*i+5, self.__x0+self.__cx*j+self.__cx-5, self.__y0+self.__cy*i+self.__cy-5, outline = "black", width = 3)
        self.__canvas.create_rectangle(self.__x0+self.__cx*m+5, self.__y0+self.__cy*k+5, self.__x0+self.__cx*m+self.__cx-5, self.__y0+self.__cy*k+self.__cy-5, outline = "black", width = 3)

    def show_number_cards(self, grid:[[[int]]]) -> None:
        """Afficher le nombre de cartes restantes dans la grille.
        Args:
            grid: grille de jeu.
        """
        self.__controller.ending()
        self.__card_counter.config(state = NORMAL)
        self.__card_counter.delete("0.0", END)
        rows, columns = len(grid), len(grid[0])
        cnt = 0
        for i in range(rows):
            for j in range(columns):
                for c in grid[i][j]:
                    cnt += 1
        if cnt == 0 :
            self.__card_counter.insert(END, f"{str(cnt)} card left")
        else:
            self.__card_counter.insert(END, f"{str(cnt)} cards left")
        self.__card_counter.config(state = DISABLED)

    def draw_grid(self, grid:[list]) -> None:
        """Dessine la grille de jeu.
        Args:
            grid: grille de jeu.
        """
        self.__canvas.delete(ALL)
        self.show_number_cards(grid)
        rows, columns = len(grid), len(grid[0])
        for i in range(rows):  
            for j in range(columns):
                if grid[i][j] != []:
                    if i%2 == 0 and j%2 == 0:
                        self.__canvas.create_rectangle(self.__x0+self.__cx*j+5, self.__y0+self.__cy*i+5, self.__x0+self.__cx*j+self.__cx-5, self.__y0+self.__cy*i+self.__cy-5, outline = "red", width = 3)
                    elif i%2 == 1 and j%2 == 1:
                        self.__canvas.create_rectangle(self.__x0+self.__cx*j+5, self.__y0+self.__cy*i+5, self.__x0+self.__cx*j+self.__cx-5, self.__y0+self.__cy*i+self.__cy-5, outline = "blue", width = 3)
                    else:
                        self.__canvas.create_rectangle(self.__x0+self.__cx*j+5, self.__y0+self.__cy*i+5, self.__x0+self.__cx*j+self.__cx-5, self.__y0+self.__cy*i+self.__cy-5, outline = "yellow", width = 3) 
                tmp = grid[i][j]
                try :
                    if tmp != []:
                        self.__canvas.create_image(self.__x0+self.__cx*j+self.__cx/2+1, self.__y0+self.__cy*i+self.__cy/2, image = self.__cards_pictures[tmp[0]-1])
                except IndexError:
                    raise Exception("Index Error")

    def to_click(self, i, j, rows, columns, grid, click1, click2) -> (tuple, tuple):
        """Clic sur un endroit dans la grille.
        Args:
            i: ligne où se situe le clic.
            j: colonne où se situe le clic.
            rows: nombre de lignes dans la grille.
            columns: nombre de colonnes dans la grille.
            grid: grille de jeu.
            click1: mémoire tempon du premier clic.
            click2: mémoire tempon du deuxième clic.
        Returns:
            le tempon du click1 et du click2.
        """
        if grid[i][j] == []:
            return (), ()
        elif click1 == () and grid[i][j] != []:
            self.__canvas.create_rectangle(self.__x0+self.__cx*j+5, self.__y0+self.__cy*i+5, self.__x0+self.__cx*j+self.__cx-5, self.__y0+self.__cy*i+self.__cy-5, outline = "navy", width = 3)
            return (i, j), ()
        else:
            click2 = (i, j)
            self.__canvas.create_rectangle(self.__x0+self.__cx*j+5, self.__y0+self.__cy*i+5, self.__x0+self.__cx*j+self.__cx-5, self.__y0+self.__cy*i+self.__cy-5, outline = "navy", width = 3)
            if click1 == click2:
                self.draw_grid(grid)
                return (), ()
            else: 
                if grid[click1[0]][click1[1]][0] == grid[click2[0]][click2[1]][0]:
                    self.__controller.make_move(click1, click2)
                    return (), ()
                else:
                    self.draw_grid(grid)
                    return (), ()