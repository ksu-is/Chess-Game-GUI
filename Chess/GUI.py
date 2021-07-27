import pygame as p
import os

# Load all resources
PSPRITE = p.image.load(os.path.join("images", "piecesprite.png"))
PIECES = ({}, {})
for i, ptype in enumerate(["k", "q", "b", "n", "r", "p"]):
    for side in range(2):
        PIECES[side][ptype] = PSPRITE.subsurface((i*50, side*50, 50, 50))

CHOOSE = p.image.load(os.path.join("images", "choose.jpg"))
CHECK = p.image.load(os.path.join("images", "check.jpg"))
STALEMATE = p.image.load(os.path.join("images", "stalemate.jpg"))
CHECKMATE = p.image.load(os.path.join("images", "checkmate.jpg"))

# Get user choice for pawn promotion
def getChoice(win, side):
    win.blit(CHOOSE, (100, 0))
    win.blit(PIECES[side]['q'], (200, 0))
    win.blit(PIECES[side]['b'], (250, 0))
    win.blit(PIECES[side]['r'], (300, 0))
    win.blit(PIECES[side]['n'], (350, 0))
    p.display.update((0, 0, 500, 50))
    while True:
        for e in p.event.get():
            if e.type == p.MOUSEBUTTONDOWN:
               if 0 < e.pos[1] < 50:
                    if 200 < e.pos[0] < 250:
                       return "q"
                    elif 250 < e.pos[0] < 300:
                        return "b"
                    elif 300 < e.pos[0] < 350:
                        return "r"
                    elif 350 < e.pos[0] < 400:
                        return "n"

# Draws the board
def drawBoard(win):
    win.fill((100, 200, 200))
    for y in range(1, 9):
        for x in range(1, 9):
            if (x+y) % 2 == 0:
                p.draw.rect(win, (220, 240, 240), (50*x, 50*y, 50, 50))

# Puts pieces onto the screen
def drawPieces(win, board):
    for side in range(2):
        for x, y, ptype in board[side]:
            win.blit(PIECES[side][ptype], (x*50, y*50))