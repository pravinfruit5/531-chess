from piece import Piece
'''Импорт фигуры'''

class Knight(Piece):
    '''Создание класса Конь'''
    def __init__(self, color):
        self.color = color
        self.position = None
    def attack_squares(self):
        """"Это ходы коня и также его атаки"""
        x,y=self.position
        return [(x+2, y+1), (x+2, y-1),(x-2, y+1), (x-2, y-1),(x+1, y+2), (x+1, y-2),(x-1, y+2), (x-1, y-2)]