import pygame as pg
import time
 
from . import (
    prepare,
    cell,
    menu
)
cell_control = cell.CellController()
cell_control.create_cell([20,20], 0)
clock = pg.time.Clock()

running = False
paused = False
running = True

# font = pg.font.Font('freesansbold.ttf', 32)
# infoTx = font.render('Escape to Exit|Space to Pause/Unpause', True,  ,gray)

# pauseTx = font.render()

while running:

    cell_control.update_state()
    prepare.SCREEN.fill((0,0,0))
    cell_control.update(pg.mouse.get_pos())
    pg.display.update()
    time.sleep(0.001)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = not running
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                running = not running
            elif event.key == pg.K_SPACE:
                paused = not paused
            elif event.key == pg.K_r:
                cell_control.clear_cells()
        if pg.mouse.get_pressed()[0] and pg.mouse.get_pos()[0]//cell.TILE_SIZE <= cell_control.WIDTH-2 and pg.mouse.get_pos()[1]//cell.TILE_SIZE <= cell_control.HEIGHT-2:
            cell_control.create_cell(pg.mouse.get_pos(), 0)
        elif pg.mouse.get_pressed()[2]:
            pos = pg.mouse.get_pos()
            cell_control.delete_cell(pos)

    while paused:
        time.sleep(0.0001)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                paused = not paused
                running = not running
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    paused = not paused
                    running = not running
                elif event.key == pg.K_SPACE:
                    paused = not paused
                elif event.key == pg.K_r:
                    cell_control.clear_cells()
            if pg.mouse.get_pressed()[0] and pg.mouse.get_pos()[0]//cell.TILE_SIZE <= cell_control.WIDTH-2 and pg.mouse.get_pos()[1]//cell.TILE_SIZE <= cell_control.HEIGHT-2:
                cell_control.create_cell(pg.mouse.get_pos(), 0)
            elif pg.mouse.get_pressed()[2]:
                cell_control.delete_cell(g.mouse.get_pos())
            prepare.SCREEN.fill((0,0,0))
            cell_control.update(pg.mouse.get_pos())
            pg.display.update()
 
            


