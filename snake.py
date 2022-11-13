from tkinter import *
import random
from time import sleep

# ширина окна
WIDTH = 800
# высота окна
HEIGHT = 600
# Размер сегмента змейки
SEG_SIZE = 20
# Переменная для состояния игры
IN_GAME = True


class Segment:

    def __init__(self, x, y):
        self.instance = c.create_rectangle(x, y, x+SEG_SIZE, y+SEG_SIZE, fill='white')


class Snake:

    def __init__(self, segments):
        self.segments = segments

        # словарь направлений движения
        self.mapping = {
            'Down': (0, 1),
            'Up': (0, -1),
            'Left': (-1, 0),
            'Right': (1, 0),
        }
        # начальное направление движения
        self.vector = self.mapping['Right']

    def move(self):
        """Двигает змейку в текущем направлении"""

        # перебираем все сегменты кроме первого
        for index in range(len(self.segments)-1):
            segment = self.segments[index].instance
            x1, y1, x2, y2 = c.coords(self.segments[index + 1].instance)
            # задаем координаты сегменту
            c.coords(segment, x1, y1, x2, y2)

        # получаем координаты сегмента перед головой
        x1, y1, x2, y2 = c.coords(self.segments[-2].instance)
        # помещаем голову в направлении движения
        c.coords(self.segments[-1].instance,
                    x1 + self.vector[0]*SEG_SIZE,
                    y1 + self.vector[1]*SEG_SIZE,
                    x2 + self.vector[0]*SEG_SIZE,
                    y2 + self.vector[1]*SEG_SIZE,
        )

    def change_direction(self, event):
        """Изменяет направление движения змейки """

        # event передаст нам символ нажатой клавиши
        if event.keysym in self.mapping:
            self.vector = self.mapping[event.keysym]

    def add_segment(self):
        """ Добавляет сегмент змейке """

        # Определяем последний сегмент
        last_seg = c.coords(self.segments[0].instance)

        # Определяем координаты следующего сегмента
        x = last_seg[2] - SEG_SIZE
        y = last_seg[3] - SEG_SIZE

        # Добавляем змейке новый сегмент
        self.segments.insert(0, Segment(x, y))

def create_block():
    """ Создает блок в случайной позиции на карте """
    global BLOCK
    posx = SEG_SIZE * (random.randint(1, (WIDTH-SEG_SIZE)/SEG_SIZE))
    posy = SEG_SIZE * (random.randint(1, (HEIGHT-SEG_SIZE)/SEG_SIZE))

    # Создаем блок как красный круг
    BLOCK = c.create_oval(posx, posy, posx+SEG_SIZE, posy+SEG_SIZE, fill='red')

def main():
    global IN_GAME

    if IN_GAME:
        # Двигаем змейку
        s.move()

        # Определяем координаты головы
        head_coords = c.coords(s.segments[-1].instance)
        x1, y1, x2, y2 = head_coords

        # Проверяем столкновение с границами экрана
        if x1 < 0 or x2 > WIDTH or y1 < 0 or y2 > HEIGHT:
            IN_GAME = False
        
        # Поедание яблок
        elif head_coords == c.coords(BLOCK):
            s.add_segment()
            c.delete(BLOCK)
            create_block()

        # Змейка съела саму себя
        else:
            # Проходим по всем сегментам
            for index in range(len(s.segments)-1):
                if c.coords(s.segments[index].instance) == head_coords:
                    IN_GAME = False
                    break
    
    # Если не в игре, то выводим сообщение о проигрыше
    else:
        c.create_text(WIDTH/2, HEIGHT/2, text='ТЫ ПРОИГРАЛ!', font='Arial 20', fill='#ff0000' )

# Создаем окно
root = Tk()
# Устанавливаем название окна
root.title("Змейка")

# Создаем экземпляр класса Canvas
c = Canvas(root, width=WIDTH, height=HEIGHT, bg="#005500")
c.grid()

# Создаем набор сегментов
segments = [
    Segment(SEG_SIZE, SEG_SIZE),
    Segment(SEG_SIZE*2, SEG_SIZE),
    Segment(SEG_SIZE*3, SEG_SIZE),
]
# Сама змейка
s = Snake(segments)

# Переводим фокус на холст
c.focus_set()

# Реагируем на нажатия клавиш
c.bind("<KeyPress>", s.change_direction)

create_block()

while True:
    main()
    c.update_idletasks()
    c.update()
    sleep(0.1)
    
# Запускаем окно
root.mainloop()