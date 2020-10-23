import pygame as pg

SCREEN_SIZE = (800, 600)
BLACK = (0, 0, 0)

pg.init()

class Ball():
    pass

class Table():
    pass

class Gun():
    pass

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
    
    def handle_events(self, events):
        done = False
        for event in events:
            if event.type == pg.QUIT:
                done = True

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

