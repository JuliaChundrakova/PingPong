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
