#---------------------[Imports]
import time 
import pygame 
import numpy as np 

#------------------------------------[Settings] 
FPS= .01
size_of_cell= 15
col_of_cells= 80
row_of_cells= 60

#-----------------------------------[Colors]
COLOR_BG = (10, 10 ,10)
COLOR_GRID = (40, 40 ,40)
COLOR_DIE_NEXT= (170, 170, 170)
COLOR_ALIVE_NEXT= (255, 255, 255)


#----------------------------------------------------------------------------[Update Function]
def update(screen, cells, size, pause=False):
    update_cells= np.zeros((cells.shape[0], cells.shape[1]))

    for row, col in np.ndindex(cells.shape):
        alive = np.sum(cells[row-1:row+2, col-1:col+2]) - cells[row, col]
        color = COLOR_BG if cells[row,col]==0 else COLOR_ALIVE_NEXT

        if cells[row, col] == 1:
            if alive < 2 or alive > 3: 
                if pause == True:
                    color = COLOR_DIE_NEXT
            elif 2 <= alive <=3:
                update_cells[row,col] = 1
                if pause:
                    color = COLOR_ALIVE_NEXT
        else:
            if alive == 3:
                update_cells[row,col]= 1
                if pause:
                    color= COLOR_ALIVE_NEXT
        
        pygame.draw.rect(screen, color, (col*size, row*size, size-1, size-1))
    return update_cells

#------------------------------------------------------------------------------------------------[Main Function]
def main():
    pygame.init()
    screen = pygame.display.set_mode((col_of_cells*size_of_cell, row_of_cells*size_of_cell))

    cells= np.zeros((row_of_cells, col_of_cells))
    screen.fill(COLOR_GRID)
    update(screen, cells, size_of_cell)

    pygame.display.update()

    running = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return 
            elif event.type == pygame.KEYDOWN:
                if  event.key == pygame.K_SPACE:
                    running = not running
                    update(screen, cells, size_of_cell)
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                cells[pos[1]//size_of_cell, pos[0]//size_of_cell] = 1
                update(screen, cells, size_of_cell)
                pygame.display.update()

        screen.fill(COLOR_GRID)
        
        if running:
            cells= update(screen, cells, size_of_cell, pause=True)
            pygame.display.update()
            time.sleep(FPS)

if __name__== '__main__':
    main()

