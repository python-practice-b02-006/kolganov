import pygame as pg
from manager import Manager

SCREEN_SIZE = (800, 600)

pg.init()

screen = pg.display.set_mode(SCREEN_SIZE)
pg.display.set_caption("Solar system")
clock = pg.time.Clock()

mgr = Manager()

done = False

while not done:
    clock.tick(15)
    
    done = mgr.process(pg.event.get(), screen)

    pg.display.flip()
