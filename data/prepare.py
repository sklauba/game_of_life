#intialization
import pygame as pg
import os
pg.init()
pcInfo = pg.display.Info()
CAPTION = "GameOfLife"
WINSIZE = (pcInfo.current_w,pcInfo.current_h)
SCREEN = pg.display.set_mode(WINSIZE)
pg.display.set_mode(WINSIZE,pg.FULLSCREEN)
pg.display.flip()
pg.display.update()

#SCREEN_RECT = SCREEN.get_rect()