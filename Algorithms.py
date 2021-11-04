n = 0   # Initialisation de toutes les variables
m = 0
i = None
j = None
NbPlayer = 2
ListPlayer = []
Count = 0
Check = 0   # Tout les joueurs n'ont pas encore eu leur tour
Loose = False   # Personne n'a perdu
Win = False # Personne n'a gagné
Play = 1    # Boucle de jeu

for x in range(NbPlayer):   # On crée notre liste des joueurs présent
    ListPlayer.append(x+1)

while n <= 2 or n > 10 or m <= 2 or m > 15 : # Tant que le nombre de colonnes et de lignes de sont pas conforme
    n = int(input('Nombre de lignes : '))   # On demande n et m
    m = int(input('Nombre de colonnes : '))

def newBoard(n, m):
    Board = [[[0, 0] for i in range(n)] for k in range(m)]  # Création du Board
    return Board

def possible(gameBoard, n, m, i, j, player):
    if i >= 0 and i < n and j >= 0 and j < m:   # Si i et j représente une case du tableau de jeu
        if gameBoard[i][j][0] == 0 or gameBoard[i][j][0] == player: # Si le joueur en est le propriétaire ou si la case est vide
            return True

def put(gameBoard, n, m, i, j, player):
    Possible = False
    while Possible != True: # Tant que la case sélectionnée n'est pas valide
        i = int(input('i : '))  # On demande les coordonnées
        j = int(input('j : '))
        Possible = possible(gameBoard, n, m, i, j, player)  # On les vérifie
    if Possible == True:    # Si elles sont bonnes
        gameBoard[i][j][0] = player # On change le propriétaire de la case
        gameBoard[i][j][1] += 1 # On incrémente le nombre de pions dans la case
    if (gameBoard[0][0][1] >= 2) or (gameBoard[n-1][0][1] >= 2) or (gameBoard[0][m-1][1] >= 2) or (gameBoard[n-1][m-1][1] >= 2):
        # Si c'est dans un coin et que le nombre de pions est d'au moins 2
        if i == 0 and j == 0:   # Coin en haut à gauche
            gameBoard[0][1][1] += 1 # On incrémente le nombre de pions les cases adjacentes
            gameBoard[1][0][1] += 1
            gameBoard[0][1][0], gameBoard[1][0][0] = gameBoard[0][0][0], gameBoard[0][0][0]
        elif i == n-1 and j == 0:   # Coin en haut à droite
            gameBoard[n-2][0][1] += 1
            gameBoard[n-1][1][1] += 1
            gameBoard[n-1][1][0], gameBoard[n-2][0][0] = gameBoard[n-1][0][0], gameBoard[n-1][0][0]
        elif i == 0 and j == m-1:   # Coin en bas à gauche
            gameBoard[0][m-2][1] += 1
            gameBoard[1][m-1][1] += 1
            gameBoard[1][m-1][0], gameBoard[0][m-2][0] = gameBoard[0][m-1][0], gameBoard[0][m-1][0]
        elif i == n-1 and j == m-1: # Coin en bas à droite
            gameBoard[n-1][m-2][1] += 1
            gameBoard[n-2][m-1][1] += 1
            gameBoard[n-2][m-1][0], gameBoard[n-1][m-2][0] = gameBoard[n-1][m-1][0], gameBoard[n-1][m-1][0]
        gameBoard[i][j][1] = 0  # On supprime les pions de la case qui a "explosé"
    elif (i > 0 and i < n and j == 0) or (i > 0 and i < n and j == m) or (i == 0 and j > 0 and j < m) or (i == n and j > 0 and j < m):
        # Si c'est une extrémité autre que les coins
        if gameBoard[i][j][1] >= 3: # Si le nombre de pions est d'au moins 3
            if j == 0:  # Barre latérale gauche
                gameBoard[i-1][j][1] += 1
                gameBoard[i+1][j][1] += 1
                gameBoard[i][j+1][1] += 1
                gameBoard[i][j+1][0], gameBoard[i-1][j][0], gameBoard[i + 1][j][0] = gameBoard[i][j][0], gameBoard[i][j][0], gameBoard[i][j][0]
            elif j == m:    # Barre latérale droite
                gameBoard[i - 1][j][1] += 1
                gameBoard[i + 1][j][1] += 1
                gameBoard[i][j-1][1] += 1
                gameBoard[i][j-1][0], gameBoard[i - 1][j][0], gameBoard[i + 1][j][0] = gameBoard[i][j][0], gameBoard[i][j][0], gameBoard[i][j][0]
            elif i == 0:    # Barre latérale haute
                gameBoard[i][j-1][1] += 1
                gameBoard[i][j+1][1] += 1
                gameBoard[i + 1][j][1] += 1
                gameBoard[i + 1][j][0], gameBoard[i][j-1][0], gameBoard[i][j+1][0] = gameBoard[i][j][0], gameBoard[i][j][0], gameBoard[i][j][0]
            elif i == n:    # Barre latérale basse
                gameBoard[i][j-1][1] += 1
                gameBoard[i][j+1][1] += 1
                gameBoard[i-1][j][1] += 1
                gameBoard[i - 1][j][0], gameBoard[i][j-1][0], gameBoard[i][j+1][0] = gameBoard[i][j][0], gameBoard[i][j][0], gameBoard[i][j][0]
            gameBoard[i][j][1] = 0
    else:   # Si ce n'est pas une extrémité du tableau
        if gameBoard[i][j][1] >= 4: # Si il y a au moins 4 pions
            gameBoard[i-1][j][1] += 1
            gameBoard[i+1][j][1] += 1
            gameBoard[i][j-1][1] += 1
            gameBoard[i][j+1][1] += 1
            gameBoard[i][j+1][0], gameBoard[i-1][j][0], gameBoard[i+1][j][0], gameBoard[i][j-1][0] = gameBoard[i][j][0], gameBoard[i][j][0], gameBoard[i][j][0], gameBoard[i][j][0]
            gameBoard[i][j][1] = 0
    for k in range(n):  # On vérifie chaques cases
        for l in range(m):
            if gameBoard[k][l][1] == 0:
                gameBoard[k][l][0] = 0  # On supprime les propriétaires de cases vides

def loose(gameBoard, n, m, player):
    for k in range(n):  # On vérifie toute les cases
        for l in range(m):
            if gameBoard[k][l][0] == player:    # Si le joueur possède au moins un pion
                return False
    return True # Sinon retourn True

def win(gameBoard, n, m, player):
    for k in range(n):  # On vérifie toute les cases
        for l in range(m):
            if gameBoard[k][l][0] != player and gameBoard[k][l][0] != 0:    # Si une case n'appartient pas au joueur et n'est pas vide
                return False
    return True # Sinon on informe qu'il ne reste qu'un joueur sur le terrain


gameBoard = newBoard(n, m)  # On enregistre le gameBoard
while Play == 1 : # Tant que la partie se déroule
    if Check == 1:  # Si tout les joueurs on eu un tour
        Loose = loose(gameBoard, n, m, player)  # On vérifie si le joueur actuel a perdu
    if Loose == False:  # Si c'est le cas on passe sont tour
        if Check == 1:  # Si tout les joueurs on eu un tour
            Win = win(gameBoard, n, m, player)  # On vérifie si le joueur actuel a gagné
        if Win == False:    # Sinon on continue la partie
            print(gameBoard)  # On affiche le Board
            if Count == len(ListPlayer):  # Si le dernier joueur a eu son tour
                Count = 0  # C'est au tour du joueur 1
                Check = 1   # Tour les joueurs ont eu un tour
            player = ListPlayer[Count]  # On prend notre joueur dans la liste
            print('C\'est au tour du joueur : ', player)  # On affiche le tour du joueur
            put(gameBoard, n, m, i, j, player)  # On pose les pions
        else:
            print("Joueur", player, "a gagné !")    # On affiche le joueur gagnant
            Play = 0    # On stop la partie
    Count += 1  # On incrémente le joueur