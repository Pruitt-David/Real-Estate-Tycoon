import sys
import pygame
import random

width = 1000
height = 700

screenDim = (width, height)

screen = pygame.display.set_mode(screenDim)

pygame.display.set_caption("Random Grid")

grassTile = pygame.image.load("assets/img/grassTile.png").convert()

roomLeft = False
tileX = 3
tileY = 3

# Basic Tiles
blankTile = pygame.image.load("assets/img/grassTile.png").convert()
PoorLowTile = pygame.image.load("assets/img/LowAndPoor.png").convert()
PoorMedTile = pygame.image.load("assets/img/MedAndPoor.png").convert()
PoorHighTile = pygame.image.load("assets/img/HighAndPoor.png").convert()
MedLowTile = pygame.image.load("assets/img/LowAndMed.png").convert()
MedMedTile = pygame.image.load("assets/img/MedAndMed.png").convert()
MedHighTile = pygame.image.load("assets/img/HighAndMed.png").convert()
RichLowTile = pygame.image.load("assets/img/LowAndRich.png").convert()
RichMedTile = pygame.image.load("assets/img/MedAndRich.png").convert()
RichHighTile = pygame.image.load("assets/img/HighAndRich.png").convert()

# Player Tiles
PPoorLowTile = pygame.image.load("assets/img/LowAndPoorPlayer.png").convert()
PPoorMedTile = pygame.image.load("assets/img/MedAndPoorPlayer.png").convert()
PPoorHighTile = pygame.image.load("assets/img/HighAndPoorPlayer.png").convert()
PMedLowTile = pygame.image.load("assets/img/LowAndMedPlayer.png").convert()
PMedMedTile = pygame.image.load("assets/img/MedAndMedPlayer.png").convert()
PMedHighTile = pygame.image.load("assets/img/HighAndMedPlayer.png").convert()
PRichLowTile = pygame.image.load("assets/img/LowAndRichPlayer.png").convert()
PRichMedTile = pygame.image.load("assets/img/MedAndRichPlayer.png").convert()
PRichHighTile = pygame.image.load("assets/img/HighAndRichPlayer.png").convert()

# Computer Opponet Tiles
OPoorLowTile = pygame.image.load("assets/img/LowAndPoorComp.png").convert()
OPoorMedTile = pygame.image.load("assets/img/MedAndPoorComp.png").convert()
OPoorHighTile = pygame.image.load("assets/img/HighAndPoorComp.png").convert()
OMedLowTile = pygame.image.load("assets/img/LowAndMedComp.png").convert()
OMedMedTile = pygame.image.load("assets/img/MedAndMedComp.png").convert()
OMedHighTile = pygame.image.load("assets/img/HighAndMedComp.png").convert()
ORichLowTile = pygame.image.load("assets/img/LowAndRichComp.png").convert()
ORichMedTile = pygame.image.load("assets/img/MedAndRichComp.png").convert()
ORichHighTile = pygame.image.load("assets/img/HighAndRichComp.png").convert()


tileList = [blankTile,
            PoorLowTile, PoorMedTile, PoorHighTile,
            MedLowTile, MedMedTile, MedHighTile,
            RichLowTile, RichMedTile, RichHighTile,
            PPoorLowTile, PPoorMedTile, PPoorHighTile,
            PMedLowTile, PMedMedTile, PMedHighTile,
            PRichLowTile, PRichMedTile, PRichHighTile,
            OPoorLowTile, OPoorMedTile, OPoorHighTile,
            OMedLowTile, OMedMedTile, OMedHighTile,
            ORichLowTile, ORichMedTile, ORichHighTile           
            ]

while roomLeft == False:    
    
    screen.blit(tileList[random.randint(0,27)], (tileX,tileY))
    tileX += 45
    
    if tileX > 800:
        tileX = 3
        tileY += 35
        if tileY > 600:
            roomLeft = True

    

finished = False
while finished == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
            pygame.quit()
            sys.exit()

    pygame.display.flip()
