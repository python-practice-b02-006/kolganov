import numpy as np
import pygame as pg
from random import randint

pg.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

SCREEN_SIZE = (800, 600)


class Ball():
    def __init__(self, coord, vel, rad=20, color=None):
        self.coord = coord
        self.vel = vel
        if color == None:
            color = (randint(0, 255), randint(0, 255), randint(0, 255))
        self.color = color
        self.rad = rad
        self.is_alive = True

    def check_corners(self, refl_ort=0.8, refl_par=0.9):
        for i in range(2):
            if self.coord[i] < self.rad:
                self.coord[i] = self.rad
                self.vel[i] = -int(self.vel[i] * refl_ort)
                self.vel[1-i] = int(self.vel[1-i] * refl_par)
            elif self.coord[i] > SCREEN_SIZE[i] - self.rad:
                self.coord[i] = SCREEN_SIZE[i] - self.rad
                self.vel[i] = -int(self.vel[i] * refl_ort)
                self.vel[1-i] = int(self.vel[1-i] * refl_par)

    def move(self, time=1, grav=0):
        self.vel[1] += grav
        for i in range(2):
            self.coord[i] += time * self.vel[i]
        self.check_corners()
        if self.vel[0]**2 + self.vel[1]**2 < 2**2:
            self.is_alive = False

    def draw(self, screen):
        pg.draw.circle(screen, self.color, self.coord, self.rad)
        
class Target():
    def __init__(self):
        pass

    def check(self):
        pass


class Gun():
    def __init__(self, coord=[30, SCREEN_SIZE[1]//2], angle=0, max_pow=50, min_pow=10, color=BLACK):
        self.coord = coord
        self.angle = angle
        self.max_pow = max_pow
        self.min_pow = min_pow
        self.color = color
        self.active = False
        self.pow = min_pow
    
    def activate(self):
        self.active = True

    def gain(self, inc=2):
        if self.active and self.pow < self.max_pow:
            self.pow += inc

    def strike(self):
        vel = self.pow
        angle = self.angle
        ball = Ball(list(self.coord), [int(vel*np.cos(angle)), int(vel*np.sin(angle))])
        self.pow = self.min_pow
        self.active = False
        return ball
        
    def set_angle(self, target_pos):
        self.angle = np.arctan2(target_pos[1] - self.coord[1], target_pos[0] - self.coord[0])

    def move(self, inc):
        self.coord[1] += inc

    def draw(self, screen):
        gun_shape = []
        vec_1 = np.array([int(5*np.cos(self.angle - np.pi/2)), int(5*np.sin(self.angle - np.pi/2))])
        vec_2 = np.array([int(self.pow*np.cos(self.angle)), int(self.pow*np.sin(self.angle))])
        gun_pos = np.array(self.coord)
        gun_shape.append((gun_pos + vec_1).tolist())
        gun_shape.append((gun_pos + vec_1 + vec_2).tolist())
        gun_shape.append((gun_pos + vec_2 - vec_1).tolist())
        gun_shape.append((gun_pos-vec_1).tolist())
        pg.draw.polygon(screen, self.color, gun_shape)


class Manager():
    def __init__(self):
        self.balls = []
        self.gun = Gun()

    def process(self, events, screen):
        done = False
        for event in events:
            if event.type == pg.QUIT:
                done = True
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_UP:
                    self.gun.move(-2)
                elif event.key == pg.K_DOWN:
                    self.gun.move(2)
            elif event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.gun.activate()
            elif event.type == pg.MOUSEBUTTONUP:
                if event.button == 1:
                    self.balls.append(self.gun.strike())

        if pg.mouse.get_focused():
            mouse_pos = pg.mouse.get_pos()
            self.gun.set_angle(mouse_pos)

        self.move()
        self.draw(screen)

        return done


    def draw(self, screen):
        for ball in self.balls:
            ball.draw(screen)
        self.gun.draw(screen)

    def move(self):
        dead_balls = []
        for i, ball in enumerate(self.balls):
            ball.move(grav=2)
            if not ball.is_alive:
                dead_balls.append(i)
        for i in reversed(dead_balls):
            self.balls.pop(i)
        self.gun.gain()



screen = pg.display.set_mode(SCREEN_SIZE)
pg.display.set_caption("Gun of Khiryanov")

done = False
clock = pg.time.Clock()

mgr = Manager()

while not done:
    clock.tick(10)
    screen.fill(WHITE)

    done = mgr.process(pg.event.get(), screen)

    pg.display.flip()


pg.quit()
