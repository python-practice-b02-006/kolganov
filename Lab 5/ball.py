import pygame as pg
from random import randint, uniform


FPS = 30

clock = pg.time.Clock()
screen = pg.display.set_mode((640, 480))
done = False

pg.font.init()
font_1 = pg.font.SysFont("Times New Roman", 30)

# ball_coords = list([[random.rand() 

class Balls():
    def __init__(self, n_balls):
        self.n_balls = n_balls
        self.balls = list([[randint(0, 639), randint(0, 479)] for i in range(n_balls)])
        self.velocities = list([[randint(-10, 10), randint(-10, 10)] for i in range(n_balls)])
        self.radius = list([randint(10, 50) for i in range(n_balls)])
        self.colors = list([(randint(0, 255), randint(0, 255), randint(0, 255)) for i in range(n_balls)])
        self.score = 0

    def iterate(self, tick):
        for i, ball in enumerate(self.balls):
            for k in range(2):
                self.balls[i][k] += self.velocities[i][k] * tick
            if ball[0] > 639:
                self.balls[i][0] = 639
                self.velocities[i][0] *= -1
            elif ball[0] < 0:
                self.balls[i][0] = 0
                self.velocities[i][0] *= -1
            elif ball[1] > 479:
                self.balls[i][1] = 479
                self.velocities[i][1] *= -1
            elif ball[1] < 0:
                self.balls[i][1] = 0
                self.velocities[i][1] *= -1

    def draw(self, screen):
        for i in range(self.n_balls):
            pg.draw.circle(screen, self.colors[i], self.balls[i], self.radius[i])

    def probe(self, x, y):
        for i, ball in enumerate(self.balls):
            if (x - ball[0])**2 + (y - ball[1])**2 < self.radius[i]**2:
                self.score += 1
                self.balls[i] = [randint(0, 639), randint(0, 479)]
                self.radius[i] = randint(20, 50)
                speed = 10 + self.score
                self.velocities[0] = [randint(-speed, speed), randint(-speed, speed)]
                return True

x, y = (0, 0)

balls = Balls(10)

while not done:
    clock.tick(20)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True
        elif event.type == pg.MOUSEBUTTONDOWN:
            x, y = event.pos
    balls.probe(x, y)
    screen.fill((0, 0, 0))
    balls.iterate(1)
    balls.draw(screen)
    score_surf = font_1.render("Score: {}".format(balls.score), False, (255, 0, 0))
    screen.blit(score_surf, (10, 30))
    pg.display.update()

pg.quit()
