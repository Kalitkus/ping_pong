from pygame import *

# Игровая сцена:
bg_color = (200, 255, 255) # цвет фона (background)
window = display.set_mode((600, 500))
window.fill(bg_color)
display.set_caption("Ping Pong")

clock = time.Clock()
FPS = 60
game = True

while game:

    for e in event.get():
        if e.type == QUIT:
            game = False

    display.update()
    clock.tick(FPS)