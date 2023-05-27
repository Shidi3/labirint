import pygame
pygame.init()
###
class Hero(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h, img, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img)
        self.image = pygame.transform.scale(self.image, (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
        self.gameOver = 0
    def draw(self, win):
        win.blit(self.image, self.rect)
    def update(self):
        x_old, y_old  = self.rect.x, self.rect.y
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        elif keys[pygame.K_DOWN] and self.rect.bottom < H:
            self.rect.y += self.speed
        elif keys[pygame.K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed
        elif keys[pygame.K_RIGHT] and self.rect.right < W:
            self.rect.x += self.speed
        is_catch = pygame.sprite.spritecollide(self, walls, False)
        if is_catch:
            self.rect.x, self.rect.y = x_old, y_old

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h, img, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img)
        self.image = pygame.transform.scale(self.image, (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
    def draw(self, win):
        win.blit(self.image, self.rect)


class Door():
    def __init__(self, x, y, w, h, img):
        self.image = pygame.image.load(img)
        self.image = pygame.transform.scale(self.image, (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def draw(self, win):
        win.blit(self.image, self.rect)


class Walls(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h, color):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([w, h])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def draw(self, win):
        win.blit(self.image, self.rect)

def game():
    hero.draw(win)
    walls.draw(win)
    door.draw(win)
    enemys.draw(win)
    hero.update()

W, H = 1208, 502

win = pygame.display.set_mode((W, H))
fon = pygame.image.load('wyVWDWLFQqo.jpg')
fon = pygame.transform.scale(fon, (W, H))
pygame.display.set_caption('Гусу. Облачные глубины.')
hero = Hero(0, 390, 104, 84, "v.png", 5)
run = True
clock = pygame.time.Clock()
walls=pygame.sprite.Group()
door = Door(1034, 357, 120, 120, 'l.png')
walls.add(Walls(54, 25, 1100, 5, (38, 144, 144)))
walls.add(Walls(54, 25, 5, 365, (38, 144, 144)))
walls.add(Walls(1154, 25, 5, 457, (38, 144, 144)))
walls.add(Walls(54, 477, 1100, 5, (38, 144, 144)))
walls.add(Walls(165, 120, 880, 5, (38, 144, 144)))
walls.add(Walls(165, 380, 600, 5, (38, 144, 144)))
enemys = pygame.sprite.Group()
enemys.add(Enemy(100, 100, 201, 142, 'z.png', 5))
fps = 60

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    win.blit(fon, (0, 0))
    if (hero.gameOver == 0):
        game()
    elif (hero.gameOver == 1):
        text_go = font.render('Тебя поймал Лань Цижень!', 1, (64, 143, 136))
        text_rect = text_go.get_rect()
        text_rect.center = (W//2, H//2)
        win.blit(text_go, text_rect)
    elif (hero.gameOver == 2):
        text_go = font.render('Ты добрался до Лань Чжаня!', 1, (64, 143, 136))
        text_rect = text_go.get_rect()
        text_rect.center = (W//2, H//2)
        win.blit(text_go, text_rect)
    pygame.display.update()
    clock.tick(fps)