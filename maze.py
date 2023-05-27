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
        is_catch = pygame.sprite.spritecollide(self, enemys, False)
        if is_catch:
            self.gameOver = 1
            pygame.mixer.music.stop()
            shoot_music1.play()
        is_catch = pygame.sprite.collide_rect(self, door)
        if is_catch:
            self.gameOver = 2  
            pygame.mixer.music.stop()
            shoot_music.play()      

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h, img, speed, x_end):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img)
        self.image = pygame.transform.scale(self.image, (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
        self.direction = 'right'
        self.x_end = x_end
        self.x_start = x
    
    def draw(self, win):
        win.blit(self.image, self.rect)
    
    def update(self):
        if self.direction == 'left' and self.rect.x < self.x_start:
            self.rect.x += self.speed
        elif self.direction == 'left' and self.rect.x >= self.x_start:
            self.direction = 'right'
        elif self.direction == 'right' and self.rect.x > self.x_end:
            self.rect.x -= self.speed
        elif self.direction == 'right' and self.rect.x <= self.x_end:
            self.direction = 'left'

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
    enemys.update()

###

W, H = 1208, 502

###

win = pygame.display.set_mode((W, H))
fon = pygame.image.load('wyVWDWLFQqo.jpg')
fon = pygame.transform.scale(fon, (W, H))
pygame.display.set_caption('Гусу. Облачные глубины.')

###

run = True
clock = pygame.time.Clock()

###

walls=pygame.sprite.Group()
hero = Hero(0, 390, 104, 84, "v.png", 5)
door = Door(1034, 357, 120, 120, 'l.png')
walls.add(Walls(54, 25, 1100, 5, (38, 144, 144)))
walls.add(Walls(54, 25, 5, 365, (38, 144, 144)))
walls.add(Walls(1154, 25, 5, 457, (38, 144, 144)))
walls.add(Walls(54, 477, 1100, 5, (38, 144, 144)))
walls.add(Walls(165, 120, 880, 5, (38, 144, 144)))
walls.add(Walls(165, 380, 600, 5, (38, 144, 144)))
walls.add(Walls(765, 215, 5, 170, (38, 144, 144)))
walls.add(Walls(875, 215, 5, 265, (38, 144, 144)))
walls.add(Walls(990, 215, 5, 105, (38, 144, 144)))
walls.add(Walls(990, 425, 5, 55, (38, 144, 144)))
walls.add(Walls(990, 280, 165, 5, (38, 144, 144)))
walls.add(Walls(165, 215, 600, 5, (38, 144, 144)))

enemys = pygame.sprite.Group()
enemys.add(Enemy(1080, 130, 67, 84, 'images.png', 7, 50))
enemys.add(Enemy(750, 375, 201, 142, 'z.png', 5, 110))

fps = 60

#font = pygame.font.Font('ofont.ru_Saytag.ttf', 70)
#font1 = pygame.font.Font('ofont.ru_Saytag.ttf', 71)

font = pygame.font.SysFont('arial', 70)
font1 = pygame.font.SysFont('arial', 71)

pygame.mixer.music.load('b.mp3')
pygame.mixer.music.play(-1)
shoot_music = pygame.mixer.Sound('vl1.ogg')
shoot_music1 = pygame.mixer.Sound('k.ogg')
###

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    win.blit(fon, (0, 0))
    if (hero.gameOver == 0):
        game()
    elif (hero.gameOver == 1):
        text_go1 = font1.render('Тебя поймали!', 1, (255, 255, 255))
        text_rect1 = text_go1.get_rect()
        text_rect1.center = (W//2, H//2)
        win.blit(text_go1, text_rect1)
        text_go = font.render('Тебя поймали!', 1, (160, 202, 223))
        text_rect = text_go.get_rect()
        text_rect.center = (W//2, H//2)
        win.blit(text_go, text_rect)
    elif (hero.gameOver == 2):
        text_go1 = font1.render('Ты добрался до Лань Чжаня!', 1, (255, 255, 255))
        text_rect1 = text_go1.get_rect()
        text_rect1.center = (W//2, H//2)
        win.blit(text_go1, text_rect1)
        text_go = font.render('Ты добрался до Лань Чжаня!', 1, (160, 202, 223))
        text_rect = text_go.get_rect()
        text_rect.center = (W//2, H//2)
        win.blit(text_go, text_rect)
    pygame.display.update()
    clock.tick(fps)

    ###