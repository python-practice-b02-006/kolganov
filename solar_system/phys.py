import numpy as np

class Body():
    def __init__(self, coords, vel, mass, color=(255, 255, 255), name=""):
        self.coords = coords
        self.vel = vel
        self.mass = mass
        self.color = color
        self.name = name
        self.force = np.array([0., 0.])

    def move(self, step=1.):
        """Изменят скорость и координаты тела, согласно приложенной общей силе, обнуляет общую силу.
        """
        pass
    
    def interact(self, body):
        """В качестве аргумента принимает класс тела, вычисляет силу между
        телами и добавляет её к общей силе.
        """
        pass

class PhysEngine():
    def __init__(self, bodies=[]):
        self.bodies = bodies
        pass

    def interact_all(self):
        """Производит попарные взаимодействия между телами.
        """
        pass

    def move(self):
        """Вызывает метод move всех подконтрольных тел.
        """
        pass





