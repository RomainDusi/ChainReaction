import pygame, sys              # On importe toutes les dépendances.
from pygame.locals import *
import random
from Variables import *

pygame.init()

def newgameBoard(Init):
    gameBoard = [[[0, 0] for i in range(Init[1])] for k in range(Init[2])]      # Création de la liste de jeu gameBoard
    return gameBoard

def initGame(MySurface):
    NbPlayer = 2    # Les valeurs initiales pour la partie.
    n = 3
    m = 3
    while True:     # On ne quitte pas la page tant que l'utilisateur ne le souhaite pas
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                poseX, poseY = event.pos
                if poseX >= 610 and poseX <= 650:   # On vérifie toutes les flèches de gauche
                    if poseY >= 100 and poseY <= 130 and NbPlayer > 1: # Diminution du nombre de joueurs
                        NbPlayer -= 1
                    if poseY >= 200 and poseY <= 230 and n > 3: # Diminution de n
                        n -= 1
                    if poseY >= 300 and poseY <= 330 and m > 3: # Diminution de m
                        m -= 1
                if poseX >= 765 and poseX <= 805:   # On vérifie toutes les flèches de droite
                    if poseY >= 100 and poseY <= 130 and NbPlayer < 8: # Augmentation du nombre de joueurs
                        NbPlayer += 1
                    if poseY >= 200 and poseY <= 230 and n < 10: # Augmentation de n
                        n += 1
                    if poseY >= 300 and poseY <= 330 and m < 15: # Augmentation de m
                        m += 1
                if poseX >= 575 and poseX <= 845 and poseY >= 445 and poseY <= 490: # Démarrer la partie
                    if NbPlayer == 1: # Implémentation du mode solo vs ordinateur ( si on choisit mode un joueur )
                        NbPlayer = 2
                        Solo = 1
                    else:   # Sinon pas de solo
                        Solo = 0
                    init = (NbPlayer, n, m, Solo)
                    return init
                if poseX >= 160 and poseX <= 510 and poseY >= 445 and poseY <= 490: # Charger une sauvegarde
                    return True
            if event.type == QUIT:
                pygame.quit()
        MySurface.fill(BLACK)   # Font noir
        Sauvegarde = font.render("Charger sauvegarde", 1, WHITE)    # On affiche aux bonnes positions les phrases
        SelectPlayers = font.render("Select number of player :             <               >", 1, WHITE)
        SelectRows = font.render("Select number of rows :                <               >", 1, WHITE)
        SelectColumns = font.render("Select number of columns :         <               >", 1, WHITE)
        Start = font.render("Start the game !", 1, WHITE)
        MySurface.blit(Sauvegarde, (170, 450))
        MySurface.blit(SelectPlayers, (100, 100))
        MySurface.blit(SelectRows, (100, 200))
        MySurface.blit(SelectColumns, (100, 300))
        MySurface.blit(Start, (585, 450))
        SelectNbPlayer = font.render(str(NbPlayer), 1, WHITE)
        MySurface.blit(SelectNbPlayer, (700, 100))
        Selectn = font.render(str(n), 1, WHITE)
        MySurface.blit(Selectn, (700, 200))
        Selectm = font.render(str(m), 1, WHITE)
        MySurface.blit(Selectm, (700, 300))
        pygame.display.flip()   # Refresh de l'écran


def drawgameBoard(MySurface, gameBoard, n, m, player):
    Colors = ((255,0,0),(0,255,0),(0,0,255),(255,255,0),(238,130,238),(255,255,255),(255,127,80),(119,136,153))   # Les couleurs des 8 joueurs
    SizeRows = 800 / n  # Tailles des colonnes et lignes par rapport au à la taille de l'écran et de n et m
    SizeCol = 580 / m
    MySurface.fill(BLACK)   # Fond noir
    CurrentPlayer = Sfont.render("Joueur :", 1, WHITE)  # On affiche le joueur actuel
    MySurface.blit(CurrentPlayer, (830, 80))
    CurrentPlayer = Sfont.render(str(player), 1, WHITE)
    MySurface.blit(CurrentPlayer, (960, 80))
    Sauvegarde = Sfont.render("Sauvegarder", 1, WHITE)  # Bouton de sauvegarde
    MySurface.blit(Sauvegarde, (818, 280))
    for i in range(m):  # Pour chaque lignes et colonnes
        for j in range(n):
            pygame.draw.rect(MySurface, Colors[player-1], (10+j*SizeRows, 10+i*SizeCol, SizeRows, SizeCol), 2)  # On affiche un rectangle de la bonne taille selon n et m
            drawCell(MySurface, gameBoard, n, m, i, j, Colors)  # On affiche les pions présents dans les cases
            pygame.display.flip()   # Refresh

def drawCell(MySurface, gameBoard, n, m, i, j, Colors):
    SizeRows = 800 / n  # Tailles des colonnes et lignes par rapport au à la taille de l'écran et de n et m
    SizeCol = 580 / m
    if gameBoard[i][j][1] >= 1: # Si il y a 1 pion
        pygame.draw.circle(MySurface, Colors[(gameBoard[i][j][0])-1], (round((10+j*SizeRows)+SizeRows/2), round((10+i*SizeCol)+SizeCol/2)), 7)
        # Affiche un pion au centre de la case
    if gameBoard[i][j][1] >= 2: # Si il y a 2 pions
        pygame.draw.circle(MySurface, Colors[(gameBoard[i][j][0])-1], (round((10 + j * SizeRows) + SizeRows *0.25), round((10 + i * SizeCol) + SizeCol *0.25)), 7)
        # Affiche un pion en haut à gauche de la case
    if gameBoard[i][j][1] == 3: # Si il y a 3 pions
        pygame.draw.circle(MySurface, Colors[(gameBoard[i][j][0])-1], (round((10 + j * SizeRows) + SizeRows *0.75), round((10 + i * SizeCol) + SizeCol *0.75)), 7)
        #Affiche un pion en bas à droite de la case

def select(MySurface, gameBoard, n, m, player, NbPlayer, Solo):
    SizeRows = 800 / n  # Tailles des colonnes et lignes par rapport au à la taille de l'écran et de n et m
    SizeCol = 580 / m
    Possible = False
    while Possible != True: # Tant que la case sélectionnée n'est pas valide
        for event in pygame.event.get():
            for j in range(n):  # On check toutes les cases
                for i in range(m):
                    if event.type == MOUSEBUTTONDOWN:
                        poseX, poseY = event.pos
                        if poseX >= 810 and poseX <= 1000 and poseY >= 270 and poseY <= 320:  # Si on sauvegarde
                            Sauvegarde = open("Sauvegarde.txt", "w+")  # Ouvre le fichier de sauvegarde
                            for a in range(m):  # Pour chaque case de gameBoard
                                for b in range(n):
                                    Sauvegarde.writelines(str(gameBoard[a][b][0]) + str(gameBoard[a][b][1]))
                                    # On enregistre le gameBoard en une suite de chiffre car python ne sais pas nativement enregistrer les listes
                            Sauvegarde.writelines("\n" + str(n) + "\n" + str(m) + "\n" + str(NbPlayer) + "\n" + str(player) + "\n" + str(Solo))
                            # On enregistre sur les lignes en dessous les autres variables nécessaire
                            Sauvegarde.close()
                        if poseX >= 10 + SizeRows * j and poseX <= 10 + SizeRows * (j+1):   # On vérifie si le joueur a cliqué sur une case
                            if poseY >= 10 + SizeCol * i and poseY <= 10 + SizeCol * (i+1):
                                Possible = possible(gameBoard, n, m, i, j, player)  # On vérifie si la position donnée est valide pour le joueur actuel
                                if Possible == True:
                                    return (i, j)   # Si c'est le cas on retourne les valeurs de la case choisie
            if event.type == QUIT:
                pygame.quit()

def possible(gameBoard, n, m, i, j, player):
    if i >= 0 and i < m and j >= 0 and j < n:   # Si i et j sont sur le gameBoard
        if gameBoard[i][j][0] == 0 or gameBoard[i][j][0] == player: # Si la case appartient au joueur ou si elle est vide
            return True

def loose(gameBoard, n, m, player):
    for k in range(m):  # On vérifie toute les cases
        for l in range(n):
            if gameBoard[k][l][0] == player:    # Si sur une des cases le joueur existe
                return False
    return True # Sinon on informe que le joueur n'est plus présent

def win(gameBoard, n, m, player):
    for k in range(m):  # On vérifie toute les cases
        for l in range(n):
            if gameBoard[k][l][0] != player and gameBoard[k][l][0] != 0:    # Si une case n'appartient pas au joueur et n'est pas vide
                return False
    return True # Sinon on informe qu'il ne reste qu'un joueur sur le terrain

def put(gameBoard, n, m, i, j, player):
    gameBoard[i][j][0] = player # La case choisi appartient au joueur actuel
    gameBoard[i][j][1] += 1 # On rajoute un pion sur celle ci
    for u in range(5):  # Simplement histoire de faire plusieurs boucles de vérifications des réactions en chaine sur le gameBoard
        ChainReaction = 1
        while ChainReaction == 1:   # Si il y a eu une réaction / explosion d'une case
            for i in range(m):  # On vérifie toute les cases
                for j in range(n):
                    if i == 0 or j == 0 or i == m-1 or j == n-1:    # On vérifie les bandes latérales et les bandes du haut et bas
                        if gameBoard[i][j][1] >= 2 and ( (i == 0 and j == 0) or ( i == m - 1 and j == 0 ) or ( i == 0 and j == n - 1 ) or ( i == m - 1 and j == n - 1 )):
                            # Si c'est dans un coin et que le nombre de pions est au moins de 2
                            if i == 0 and j == 0:   # Coin en haut à gauche
                                gameBoard[0][1][1] += 1 # On rajoute un pion sur les cases adjacentes
                                gameBoard[1][0][1] += 1
                                gameBoard[0][1][0], gameBoard[1][0][0] = gameBoard[0][0][0], gameBoard[0][0][0] # On change le propriétaire des cases adjacentes
                                gameBoard[i][j][1] = 0  # On supprime les pions de la case ayant "explosée"
                            elif i == m - 1 and j == 0: # Coin en bas à gauche
                                gameBoard[m - 2][0][1] += 1
                                gameBoard[m - 1][1][1] += 1
                                gameBoard[m - 1][1][0], gameBoard[m - 2][0][0] = gameBoard[m - 1][0][0], gameBoard[m - 1][0][0]
                                gameBoard[i][j][1] = 0
                            elif i == 0 and j == n - 1: # Coin en haut à droite
                                gameBoard[0][n - 2][1] += 1
                                gameBoard[1][n - 1][1] += 1
                                gameBoard[1][n - 1][0], gameBoard[0][n - 2][0] = gameBoard[0][n - 1][0], gameBoard[0][n - 1][0]
                                gameBoard[i][j][1] = 0
                            elif i == m - 1 and j == n - 1: # Coin en bas à droite
                                gameBoard[m - 1][n - 2][1] += 1
                                gameBoard[m - 2][n - 1][1] += 1
                                gameBoard[m - 2][n - 1][0], gameBoard[m - 1][n - 2][0] = gameBoard[m - 1][n - 1][0], \
                                                                                 gameBoard[m - 1][n - 1][0]
                                gameBoard[i][j][1] = 0
                        elif gameBoard[i][j][1] >= 3: # Si il y a au moins 3 pions dans la case
                            if j == 0: # Bande latérale gauche
                                gameBoard[i - 1][j][1] += 1
                                gameBoard[i + 1][j][1] += 1
                                gameBoard[i][j + 1][1] += 1
                                gameBoard[i][j + 1][0], gameBoard[i - 1][j][0], gameBoard[i + 1][j][0] = gameBoard[i][j][0], \
                                                                                             gameBoard[i][j][0], \
                                                                                             gameBoard[i][j][0]
                                gameBoard[i][j][1] = 0
                            elif j == n - 1:    # Bande latérale droite
                                gameBoard[i - 1][j][1] += 1
                                gameBoard[i + 1][j][1] += 1
                                gameBoard[i][j - 1][1] += 1
                                gameBoard[i][j - 1][0], gameBoard[i - 1][j][0], gameBoard[i + 1][j][0] = gameBoard[i][j][0], \
                                                                                             gameBoard[i][j][0], \
                                                                                             gameBoard[i][j][0]
                                gameBoard[i][j][1] = 0
                            elif i == 0:    # Bande du haut
                                gameBoard[i][j - 1][1] += 1
                                gameBoard[i][j + 1][1] += 1
                                gameBoard[i + 1][j][1] += 1
                                gameBoard[i + 1][j][0], gameBoard[i][j - 1][0], gameBoard[i][j + 1][0] = gameBoard[i][j][0], \
                                                                                             gameBoard[i][j][0], \
                                                                                             gameBoard[i][j][0]
                                gameBoard[i][j][1] = 0
                            elif i == m - 1:    # Bande du bas
                                gameBoard[i][j - 1][1] += 1
                                gameBoard[i][j + 1][1] += 1
                                gameBoard[i - 1][j][1] += 1
                                gameBoard[i - 1][j][0], gameBoard[i][j - 1][0], gameBoard[i][j + 1][0] = gameBoard[i][j][0], \
                                                                                             gameBoard[i][j][0], \
                                                                                             gameBoard[i][j][0]
                                gameBoard[i][j][1] = 0
                    elif gameBoard[i][j][1] >= 4:   # Si il y a au moins 4 pions dans la case ( et par suite avec le if au dessus, que la case ne soit pas sur une extrémitée )
                        gameBoard[i - 1][j][1] += 1
                        gameBoard[i + 1][j][1] += 1
                        gameBoard[i][j - 1][1] += 1
                        gameBoard[i][j + 1][1] += 1
                        gameBoard[i][j + 1][0], gameBoard[i - 1][j][0], gameBoard[i + 1][j][0], gameBoard[i][j - 1][0] = gameBoard[i][j][0], \
                                                                                                         gameBoard[i][j][0], \
                                                                                                         gameBoard[i][j][0], \
                                                                                                         gameBoard[i][j][0]
                        gameBoard[i][j][1] = 0
                    else:
                        ChainReaction = 0   # Si il n'y à pas eu de réaction
                    for k in range(m):  # On vérifie toute les cases
                        for l in range(n):
                            if gameBoard[k][l][1] == 0: # Si il n'y a plus de pions sur une case
                                gameBoard[k][l][0] = 0  # On supprime le propriétaire de cette case

def gamePlay(MySurface, gameBoard, n, m, NbPlayer, player, Solo):
    Looser = False
    Winner = False
    Check = 0
    while True: # Boucle de jeu
        i = 50
        if Check == 1:  # Si tout les joueurs on eu au moins un tour
            Looser = loose(gameBoard, n, m, player) # On vérifie si le joueur actuel à perdu, sinon on passe son tour
        if Looser == False: # Si le joueur n'a pas perdu
            if Check == 1:  # Si tout les joueurs on eu au moins un tour
                Winner = win(gameBoard, n, m, player)   # On vérifie si le joueur actuel est le dernier restant
            if Winner == False: # Si il n'a pas gagné
                drawgameBoard(MySurface, gameBoard, n, m, player)   # On affiche l'espace de jeu
                while i > m-1 : # Tant que
                    if Solo == 1 and player == 2:   # Si on est en mode 1 vs ordinateur
                        Possible = False
                        while Possible != True: # Tant que les coordonnées aléatoire de l'ordinateur ne sont pas bonnes
                            i = random.randint(0, n)    # Random n et m
                            j = random.randint(0, m)
                            Possible = possible(gameBoard, n, m, i, j, player)  # On vérifie si elles sont correte
                    else:
                        i, j = select(MySurface, gameBoard, n, m, player, NbPlayer, Solo)   # On attend le clique du prochain joueur
                    put(gameBoard, n, m, i, j, player)  # On place le pion sur le gameBoard et on vérifie si il y a une réaction
            else:   # Si un joueur a gagné
                MySurface.fill(BLACK)   # Fond noir
                Feux = pygame.image.load('Feux.png')    # On affiche les phrases et l'image de victoire
                Winner = Bfont.render("Joueur    a gagné !", 1, WHITE)
                CurrentPlayer = Bfont.render(str(player), 1, WHITE)
                Recommencer = Bfont.render("Recommencer ?", 1, WHITE)
                MySurface.blit(Feux, (0,0))
                MySurface.blit(Winner, (260, 50))
                MySurface.blit(CurrentPlayer, (468, 50))
                MySurface.blit(Recommencer, (300, 500))
                pygame.display.flip()   # Refresh
                for event in pygame.event.get():
                    if event.type == MOUSEBUTTONDOWN:
                        poseX, poseY = event.pos
                        if poseX >= 290 and poseX <= 750 and poseY >= 500 and poseY <= 580: # Si on clique sur recommencer
                            gameBoard = gameBoard = newgameBoard((NbPlayer, n, m, Solo))    # On recrée le gameBoard vide
                            player = 1  # On recommence au premier joueur
                            gamePlay(MySurface, gameBoard, n, m, NbPlayer, player, Solo)    # On relance la partie
                    if event.type == QUIT:
                        pygame.quit()
        if player == NbPlayer:  # Si c'était le tour du dernier joueur
            player = 1  # On repasse au premier
            Check = 1   # On dit que tout les joueurs ont eu leur tour
        else:   # Sinon on incrémente le joueur actuel
            player += 1


def chainReaction():
    MySurface = pygame.display.set_mode((1000, 600))    # On crée la page
    pygame.display.set_caption('Chain Reactions')   # Nom du jeu
    Init = initGame(MySurface)  # Affichage de l'écran du choix des paramètres de partie
    if Init != True:    # Si on ne charge pas une partie
        n = Init[1] # On récupère les infos dans la variable Init
        m = Init[2]
        NbPlayer = Init[0]
        Solo = Init[3]
        player = 1  # Tour du joueur 1
        gameBoard = newgameBoard(Init)  # On crée le Board
    else:   # Si on charge une sauvegarde
        Save = open('Sauvegarde.txt', 'r')  # Ouverture du fichier de sauvegarde
        Fichier = Save.readlines()  # On enregistre le fichier dans la variable Fichier
        n = int(Fichier[1]) # On récupère les informations présente dans la liste Fichier
        m = int(Fichier[2])
        NbPlayer = int(Fichier[3])
        player = int(Fichier[4])
        Solo = int(Fichier[5])
        Init = (NbPlayer, n, m, Solo)   # On recrée la variable Init avec les informations récupérées
        SavegameBoard = list(Fichier[0])    # On récupère la ligne du gameBoard
        gameBoard = newgameBoard(Init)  # On recrée un gameBoard vide
        compt = 0
        for a in range(m):  # Pour chaques cases
            for b in range(n):
                gameBoard[a][b][0] = int(SavegameBoard[compt])  # On replace le propriétaire et le pion sur la bonne case
                gameBoard[a][b][1] = int(SavegameBoard[compt+1])
                compt += 2  # Le gameBoard est sauvegardé sous la forme d'une suite de chiffre Propriétaire -> Nombre de pions -> Propriétaire -> ...
    gamePlay(MySurface, gameBoard, n, m, NbPlayer, player, Solo)    # On lance la partie


chainReaction()
pygame.quit()
