'''Les règles du carré magique de Merlin :
   ---------------------------------------
• Lorsque vous appuyez sur un bouton d'angle (1, 3, 7 ou 9), il inverse les 4 boutons du carré d'angle 2x2 dans lequel il se trouve
• Lorsque vous appuyez sur un bouton latéral (2, 4, 6 ou 8), il inverse les 3 boutons de cette rangée de bordure
• Lorsque vous appuyez sur le bouton du milieu (5), il inverse les 5 boutons en forme de "+" du milieu
• ("Reverse" signifie que s'il est allumé, il s'éteint ; s'il est éteint, il s'allume.)
• L'état Résolu est lorsque tous les boutons sont allumés sauf celui du milieu (5) ; ceci est montré ci-dessus en bleu'''

import pygame, sys
import random
from bot2_0 import bot
'''from pygame.locals import QUIT'''
pygame.init()

NB_COL = 3
NB_LIGNE = 3
CELL_SIZE = 100
TABLE_COLOR = ['red', 'white']
TABLE_COLOR_INVERSE = [1, 0]
TABLE_COULEUR_GAGNANTE = [0, 0, 0, 0, 1, 0, 0, 0, 0]

pygame.display.set_caption('   CARRE MAGIQUE')

screen = pygame.display.set_mode(size=(NB_COL * CELL_SIZE,
                                       NB_LIGNE * CELL_SIZE))
timer = pygame.time.Clock()
continuer = True
tableCouleur = []
tableCoul = []
tableRectangle = []
resultats = []


def gagner(tableCouleur):
  if tableCouleur == TABLE_COULEUR_GAGNANTE:
    #print('MAGNIFIQUE : vous avez gagné')
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


def inverser(tableIndice):
  for i in tableIndice:
    tableCouleur[i] = TABLE_COLOR_INVERSE[tableCouleur[i]]


def init():
  for i in range(0, NB_COL * NB_LIGNE):
    indexInit = random.randint(0, 1)
    tableCouleur.append(indexInit)
  return tableCouleur


def showGrid(tableCoul):
  indexCouleur = 0
  for i in range(0, NB_COL):
    for j in range(0, NB_LIGNE):
      rect1 = pygame.Rect(j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE)
      tableRectangle.append(rect1)
      #pygame.draw.rect(screen, pygame.Color(TABLE_COLOR[index]), rect, width = 5)

      index = tableCoul[indexCouleur]
      pygame.draw.rect(screen, pygame.Color(TABLE_COLOR[index]), rect1)
      pygame.draw.rect(screen, pygame.Color('black'), rect1, width=20)
      indexCouleur += 1


def carreCliquer(argPos):
  for i in range(0, len(tableRectangle)):
    if tableRectangle[i].collidepoint(argPos):
      return i


tableCoul = init()
while continuer:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      continuer = False

    if event.type == pygame.MOUSEBUTTONUP:
      pos = pygame.mouse.get_pos()
      numBouton = event.button  # 1 = click gauche
      if numBouton == 1:
        caseClick = carreCliquer(pos)
        tableIndice1 = creaTableIndice(caseClick)
        inverser(tableIndice1)
        #gagner(tableCouleur)

  screen.fill(pygame.Color("white"))
  showGrid(tableCoul)
  pygame.display.update()
  timer.tick(60)
  if gagner(tableCouleur):
    print('MAGNIFIQUE ! vous avez gagné')
    continuer = False
    pygame.time.delay(1000)
  else:
    print(len(bot(tableCoul)))

pygame.quit()
#sys.exit()‌