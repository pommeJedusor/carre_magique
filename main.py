import pygame
import random
from bot2_0 import bot
pygame.init()

NB_COL = 3
NB_LIGNE = 3
CELL_SIZE = 100
TABLE_COLOR = ['red', 'white']
TABLE_COLOR_INVERSE = [1, 0]
TABLE_COULEUR_GAGNANTE = [0, 0, 0, 0, 1, 0, 0, 0, 0]

pygame.display.set_caption('   CARRE MAGIQUE')

screen = pygame.display.set_mode(size=(NB_COL * CELL_SIZE,NB_LIGNE * CELL_SIZE))
timer = pygame.time.Clock()


def gagner(tableCouleur):
  if tableCouleur == TABLE_COULEUR_GAGNANTE:
    return True


def creaTableIndice(numCarre):
  if numCarre == 0:
    return [0, 1, 3, 4]
  elif numCarre == 1:
    return [0, 1, 2]
  elif numCarre == 2:
    return [1, 2, 4, 5]
  elif numCarre == 3:
    return [0, 3, 6]
  elif numCarre == 4:
    return [1, 3, 4, 5, 7]
  elif numCarre == 5:
    return [2, 5, 8]
  elif numCarre == 6:
    return [3, 4, 6, 7]
  elif numCarre == 7:
    return [6, 7, 8]
  elif numCarre == 8:
    return [4, 5, 7, 8]


def inverser(numCarre, tableCouleur):
  #récupère les cases à inverser
  tableIndice = creaTableIndice(numCarre)
  for i in tableIndice:
    tableCouleur[i] = TABLE_COLOR_INVERSE[tableCouleur[i]]


def init():
  tableCouleur = []
  for i in range(0, NB_COL * NB_LIGNE):
    couleur = random.randint(0, 1)
    tableCouleur.append(couleur)
  return tableCouleur

def get_squares():
  squares = []
  for i in range(0, NB_COL):
    for j in range(0, NB_LIGNE):
      square = pygame.Rect(j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE)
      squares.append(square)
  return squares

def showGrid(tableCoul):
  indexCouleur = 0
  for i in range(0, NB_COL):
    for j in range(0, NB_LIGNE):
      square = pygame.Rect(j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE)
      #récupère la couleur du carré
      index = tableCoul[indexCouleur]
      square_color = TABLE_COLOR[index]
      #couleur du centre du carré
      pygame.draw.rect(screen, pygame.Color(square_color), square)
      #contour noir du carré
      pygame.draw.rect(screen, pygame.Color('black'), square, width=20)
      indexCouleur += 1


def carreCliquer(argPos):
  squares = get_squares()
  for i in range(0, len(squares)):
    if squares[i].collidepoint(argPos):
      return i


continuer = True
tableCouleur = init()
while continuer:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      continuer = False

    #vérifie si click gauche
    if event.type == pygame.MOUSEBUTTONUP:
      pos = pygame.mouse.get_pos()
      numBouton = event.button
      if numBouton == 1:
        #inverse en fonction de la case
        inverser(carreCliquer(pos), tableCouleur)
        print(len(bot(tableCouleur)))

  #actualise la vue du jeu
  showGrid(tableCouleur)
  pygame.display.update()
  timer.tick(60)
  if gagner(tableCouleur):
    print('MAGNIFIQUE ! vous avez gagné')
    tableCouleur = init()
    pygame.time.delay(1000)
    

pygame.quit()