class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[KEY_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
            if keys[K_DOWN] and self.rect.y < win_weight - 80:
                self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
            if keys[K_s] and self.rect.y < win_weight - 80:
                self.rect.y += self.speed
back = (200, 255 , 255)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(back)
game = True
finish = False
clock = time.Clock()
FPS = 60


racket1 = Player("raketka.png", 30, 200, 4, 50, 150)
racket2 = Player("raketka.png", 520, 200, 4, 50, 150)
ball = GameSprite("ball.png", 200, 200, 4, 50, 50)

speed_x = 3
speed_y = 3

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.fill(back)
        racket1.update_l()
        racket2.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        racket1.reset()
        racket2.reset()
        ball.reset()

    display.update()
    clock.tick(FPS)  
