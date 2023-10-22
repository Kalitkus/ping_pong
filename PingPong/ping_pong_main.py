from pygame import *

font.init()

# Игровая сцена:
bg_color = (200, 255, 255) # цвет фона (background)
window = display.set_mode((600, 500))
window.fill(bg_color)
display.set_caption("Ping Pong")

clock = time.Clock()
FPS = 60
game = True
winner = ''

class GameSprite(sprite.Sprite):
    def __init__(self, image_file, x, y, w, h, spd_x, spd_y):
        super().__init__()
        self.image = transform.scale(image.load(image_file), (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.spd_x = spd_x
        self.spd_y = spd_y
    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class PlayerRed(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.spd_y
        if keys[K_s] and self.rect.y < 350:
            self.rect.y += self.spd_y

class PlayerBlue(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.spd_y
        if keys[K_DOWN] and self.rect.y < 350:
            self.rect.y += self.spd_y

class Ball(GameSprite):
    def colliderect(self, rect):
        return self.rect.colliderect(rect)
    def update(self):
        global winner
        self.rect.x += self.spd_x
        self.rect.y += self.spd_y
        if self.rect.x > 575:
            self.x_win = 20
            winner = 'КРАСНЫЙ ИГРОК!'
        if self.rect.x < 0:
            winner = 'СИНИЙ ИГРОК!'
        if self.rect.y < 0 or self.rect.y > 470:
            self.spd_y *= -1
        if self.colliderect(red_board) or self.colliderect(blue_board):
            self.spd_x *= -1


bY = 180

red_board = PlayerRed("red_line.png", 0, bY, 35, 160, 0, 6)
blue_board = PlayerBlue("blue_line.png", 570, bY, 35, 160, 0, 6)
ball = Ball("ball.png", 280, 250, 25, 25, 3, 3)

Font = font.SysFont('Arial', 35)
txt_winner = Font.render('ПОБЕДИЛ ' + winner, True, (25, 80, 255))
txt_reset = Font.render('ЕЩЁ РАЗ', True, (85, 255, 55))

while game:

    window.fill(bg_color)

    if winner == '':
        red_board.update()
        blue_board.update()
        ball.update()
    else:
        # Подбор оптимальной координаты X
        if winner == 'КРАСНЫЙ ИГРОК!':
            bX = 60
            txt_color = (255, 43, 40)
        else:  # 'СИНИЙ ИГРОК!'
            bX = 80
            txt_color = (25, 80, 255)
        txt_winner = Font.render('ПОБЕДИЛ ' + winner, True, txt_color)
        bg_txt = Surface((txt_reset.get_width(), txt_reset.get_height())) # создание заднего фона
        bg_txt.fill((255, 247, 173)) # заливка заднего фона
        window.blit(bg_txt, (220, 300))  # отображение заднего фона на экране
        window.blit(txt_winner, (bX, bY))
        window.blit(txt_reset, (220, 300))

    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == MOUSEBUTTONDOWN:
            # получение координат клика мыши
            x, y = e.pos
            # получение прямоугольника, охватывающего текст
            text_size = txt_reset.get_size() # возвращает ширину и высоту текста в виде кортежа
            text_rect = Rect(220, 300, text_size[0], text_size[1])
            # проверка, было ли нажатие мыши внутри прямоугольника
            if text_rect.collidepoint(x, y):
                ball.rect.x, ball.rect.y = 280, 250
                red_board.rect.y, blue_board.rect.y = bY, bY
                winner = ''

    # Отрисовка спрайтов
    red_board.draw()
    blue_board.draw()
    ball.draw()

    display.update()
    clock.tick(FPS)
