class Button():
    def __init__(self, coord, rect, caption, action):
        self.coord = coord
        self.rect = rect
        self.caption = caption
        self.action = action

    def handle(self, event):
        """Вызывает action если нажетие было в поле кнопки.
        """
        pass

class Bar():
    pass
