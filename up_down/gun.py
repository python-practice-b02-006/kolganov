import pygame as pg
import numpy as np

SCREEN_SIZE = (800, 600)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

pg.init()

class Ball():
    pass

class Table():
    pass

class Gun():
    def __init__(self, coord=[30, SCREEN_SIZE[1]//2]):
        self.coord = coord
        self.angle = 0

    def draw(self, screen):
        end_pos = [self.coord[0] + 20*np.cos(self.angle), self.coord[1] + 20*np.sin(self.angle)]
        pg.draw.line(screen, RED, self.coord, end_pos, 5)

    def strike(self):
        pass

    def set_angle(self, mouse_pos):
        self.angle = np.arctan2(mouse_pos[1] - self.coord[1], 
                                mouse_pos[0] - self.coord[0])


class Target():
    pass

class Manager():
    def __init__(self):
        self.gun = Gun()
        self.table = Table()
    
    def process(self, events, screen):
        done = self.handle_events(events)
        self.draw(screen)
        return done

    def draw(self, screen):
        screen.fill(BLACK)
        self.gun.draw(screen)
    
    def handle_events(self, events):
        done = False
        for event in events:
            if event.type == pg.QUIT:
                done = True
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_UP:
                    self.gun.coord[1] -= 5
                elif event.key == pg.K_DOWN:
                    self.gun.coord[1] += 5
        
        if pg.mouse.get_focused():
            mouse_pos = pg.mouse.get_pos()
            self.gun.set_angle(mouse_pos)

        return done


screen = pg.display.set_mode(SCREEN_SIZE)
pg.display.set_caption("The gun of Khiryanov")
clock = pg.time.Clock()

mgr = Manager()

done = False

while not done:
    clock.tick(15)

    done = mgr.process(pg.event.get(), screen)

    pg.display.flip()

