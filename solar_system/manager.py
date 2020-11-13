import pygame as pg

class Manager():
    def __init__(self):
        """ Создаёт экземпляр физ. движка, элементов управления (gui), класса для считывания файлов.
        """
        pass

    def process(self, events, screen):
        """ Функция вызываемая каждый тик по времени. Вызывает функции итерации по времени для физ. движка, обрабатывает события, 
        передаёт их элементам управления.
        """
        done = self.handle_events(events)
        return done

    def handle_events(self, events):
        done = False
        for event in events:
            if event.type == pg.QUIT:
                done = True
        
        return done
