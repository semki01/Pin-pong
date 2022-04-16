from pygame import*

img_back = 'blue_fon.png'
img_hero = 'racket.png'

win_width = 700
win_height = 500
display.set_caption('Pin pong')
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(img_back), (win_width, win_height))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_width - 80:
            self.rect.y += self.speed

class Player2(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_width - 80:
            self.rect.y += self.speed

speed_x = 10
speed_y = 10

class Ball(GameSprite):
    def update(self):

        #if ball.rect.colliderect(racket.rect):
            #self.speed *= -1 
        #elif ball.rect.colliderect(racket2.rect):
            #self.speed *= -1
 


        if ball.rect.x > 700:
            text = font2.render('Player 1 победил!', 1, (195, 0, 0))
            window.blit(text, (95, 220))
        elif ball.rect.x < 0:
            text = font2.render('Player 2 победил!', 1, (195, 0, 0))
            window.blit(text, (95, 220))
        


font.init()
font2 = font.SysFont(None, 90)

racket = Player2('racket.png', 650, 200, 30, 120, 10)
racket2 = Player('racket.png', 50, 205, 30, 120, 10)
ball = Ball('tenis_ball.png', 250, 250, 60, 60, 10)
#wall_1 = GameSprite('black.png', 0, 0, 700, 20, 0)
#wall_2 = GameSprite('black.png', 0, 480, 700, 20, 0)

finish = False
clock = time.Clock()
run = True
FPS = 60

while run:
    if not finish:

        window.blit(background,(0,0))

        for e in event.get():
            if e.type == QUIT:
                run = False

        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if ball.rect.y > win_height-50 or ball.rect.y < 0:
            speed_y *= -1

        if sprite.collide_rect(racket, ball) or sprite.collide_rect(racket2, ball):
            speed_x *= -1


        racket.update()
        racket.reset()
        racket2.update()
        racket2.reset()
        ball.update()
        ball.reset()
        #wall_1.update()
        #wall_1.reset()
        #wall_2.update()
        #wall_2.reset()
        
        display.update()

        time.delay(50)
        clock.tick(FPS)