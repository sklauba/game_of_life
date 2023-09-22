import pygame as pg
import numpy as np
from . import prepare
import math
import os

TILE_SIZE = 20

class CellController:
    def __init__(self):
        #self.cells = [ ]
        self.WIDTH = (prepare.WINSIZE[0]//TILE_SIZE)+1
        self.HEIGHT = (prepare.WINSIZE[1]//TILE_SIZE)+1    
        self.cells = np.empty((self.WIDTH,self.HEIGHT), dtype=Cell)
        self.cells_future=self.cells.copy()
        self.cell_image = self.cell_image_load(False)
        self.cell_image_highlighted = self.cell_image_load(True)
        self.highlighted_cell = Cell(self.cell_image_highlighted, (0,0), 0)

    def cell_image_load(self, highlighted_type):
        if highlighted_type == False:
            image = pg.Surface((TILE_SIZE-(TILE_SIZE//10),TILE_SIZE-(TILE_SIZE//10)))
            image.fill('green')
        else:
            image = pg.Surface((TILE_SIZE-(TILE_SIZE//10),TILE_SIZE-(TILE_SIZE//10)))
            image.fill('grey')
        return (image)
    def clear_cells(self):
        self.cells = np.empty((self.WIDTH,self.HEIGHT), dtype=Cell)
        self.cells_future=self.cells.copy()
    
    def neighbor_check_function(self, pos):
        neighbors=0
        for i in range(8):
            match i:
                case 0:
                    if pos[0] != 0 and self.cells[pos[0]-1,pos[1]+1] is not None:
                        neighbors += 1
                case 1:
                    if self.cells[pos[0],pos[1]+1] is not None:
                        neighbors += 1
                case 2:
                    if self.cells[pos[0]+1,pos[1]+1] is not None:
                        neighbors += 1
                case 3:
                    if self.cells[pos[0]+1,pos[1]] is not None:
                        neighbors += 1
                case 4:
                    if pos[1] != 0 and self.cells[pos[0]+1,pos[1]-1] is not None:
                        neighbors += 1
                case 5:
                    if pos[1] != 0 and self.cells[pos[0],pos[1]-1] is not None:
                        neighbors += 1
                case 6:
                    if pos[0] != 0 and pos[1] != 0 and self.cells[pos[0]-1,pos[1]-1] is not None:
                        neighbors += 1
                case 7:
                    if pos[0] != 0 and self.cells[pos[0]-1,pos[1]] is not None:
                        neighbors += 1
        return neighbors

    def neighbor_check(self, location_x, location_y):
        neighbors = 0
        x = int(location_x)
        y = int(location_y)
        return self.neighbor_check_function((x,y))

    def update_cells(self, each_cell):
        x = int(each_cell.location[0])
        y = int(each_cell.location[1])
        for i in range(9):
            match i:
                case 0:
                    if x != 0 and y < self.HEIGHT-2 and self.neighbor_check(x-1,y+1) == 3:
                        self.create_cell([x-1,y+1],1)
                case 1:
                    if y < self.HEIGHT-2 and self.neighbor_check(x,y+1) == 3:
                        self.create_cell([x,y+1], 1)
                case 2:
                    if x < self.WIDTH-2 and y < self.HEIGHT-2 and self.neighbor_check(x+1,y+1) == 3:
                        self.create_cell([x+1,y+1], 1)
                case 3:
                    if x < self.WIDTH-2 and self.neighbor_check(x+1,y) == 3:
                        self.create_cell([x+1,y], 1)
                case 4:
                    if x < self.WIDTH-2 and y != 0 and self.neighbor_check(x+1,y-1) == 3:
                        self.create_cell([x+1,y-1], 1)
                case 5:
                    if y != 0 and self.neighbor_check(x,y-1) == 3:
                        self.create_cell([x,y-1], 1)
                case 6:
                    if x != 0 and y != 0 and self.neighbor_check(x-1,y-1) == 3:
                        self.create_cell([x-1,y-1], 1)
                case 7:
                    if x != 0 and self.neighbor_check(x-1,y) == 3:
                        self.create_cell([x-1,y], 1)
                case 8:
                    z = self.neighbor_check(x,y)
                    if z == 2 or z == 3:
                        self.create_cell([x,y], 1)

    def update_state(self):
        for rows in self.cells:
            for cells in rows:
                if cells is not None: self.update_cells(cells)
        self.cells = np.copy(self.cells_future)
        self.cells_future = np.empty((self.WIDTH,self.HEIGHT), dtype=Cell)
        return self.cells_future


                    
    def is_cell(self, cell_pos):
        if self.cells[cell_pos[0]//TILE_SIZE, cell_pos[1]//TILE_SIZE] == None:
            return False
        return True

    def create_cell(self, cell_pos, flag):
        if flag == 0:
            self.cells[cell_pos[0]//TILE_SIZE, cell_pos[1]//TILE_SIZE] = Cell(self.cell_image, ((cell_pos[0]//TILE_SIZE)*TILE_SIZE,(cell_pos[1]//TILE_SIZE)*TILE_SIZE), 0)
        else:
            self.cells_future[(cell_pos[0]), (cell_pos[1])] = Cell(self.cell_image, ((cell_pos[0])*TILE_SIZE,(cell_pos[1])*TILE_SIZE), 0)
    
    def delete_cell(self, cell_pos):
        self.cells[cell_pos[0]//TILE_SIZE, cell_pos[1]//TILE_SIZE] = None

    # def update_test(self, mouse_pos):
    #     #self.max_i=len(self.cells)
    #     #self.max_j=len(self.cells[0])
    #     #for c in self.cells[:]:
    #     self.cells = self.update_state().copy()
    #     for _, cell in np.ndenumerate(self.cells):
    #         if cell != None:
    #             cell.draw(prepare.SCREEN)
    #         #print(c)
    #         self.highlighted_cell.update(0, (round(mouse_pos[0]/TILE_SIZE)*TILE_SIZE,round(mouse_pos[1]/TILE_SIZE)*TILE_SIZE))
    #         self.highlighted_cell.draw(prepare.SCREEN)

    def update(self, mouse_pos):
        #self.max_i=len(self.cells)
        #self.max_j=len(self.cells[0])
        #for c in self.cells[:]:
        for _, cell in np.ndenumerate(self.cells):
            if cell != None:
                cell.draw(prepare.SCREEN)
            #print(c)
            self.highlighted_cell.update(((mouse_pos[0]//TILE_SIZE)*TILE_SIZE,(mouse_pos[1]//TILE_SIZE)*TILE_SIZE))
            self.highlighted_cell.draw(prepare.SCREEN)
            
    

    
class Cell:
    def __init__(self, image, pos, neighbor_cnt) -> None:
        self.image = image
        self.cell_pos = pos
        self.rect = self.image.get_rect(
            center=(self.cell_pos[0]+(TILE_SIZE//2), self.cell_pos[1]+(TILE_SIZE//2))
        )
        self.location = (self.cell_pos[0]/TILE_SIZE, self.cell_pos[1]/TILE_SIZE)
        self.neighbors = neighbor_cnt
        self.dead = False

    def update(self, pos):
        self.cell_pos = pos
        self.rect = self.image.get_rect(
            center=(self.cell_pos[0]+(TILE_SIZE//2), self.cell_pos[1]+(TILE_SIZE//2))
        )

    def draw(self, surf):
        surf.blit(self.image, self.rect)
