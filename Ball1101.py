import pygame, sys, random

pygame.init()
SURFACE = pygame.display.set_mode((500,500))
FPSCLOCK = pygame.time.Clock()

class Ball:
    def __init__(self, img_file, location, speed):
        self.image= pygame.image.load(img_file)
        self.rect= self.image.get_rect()
        self.rect.topleft= location
        self.speed= list(speed)

    def move(self):
        self.rect.move_ip(self.speed)
        if self.rect.left< 0 or self.rect.right> SURFACE.get_width():
            self.speed[0] = -self.speed[0]
        if self.rect.top< 0 or self.rect.bottom> SURFACE.get_height():
            self.speed[1] = -self.speed[1]

ball_group = []

for y in range(3):
    for x in range(3):
        location = (150*x+50, 150*y+50)
        speed = (random.choice([-2,2]), random.choice([-2,2]))
        myBall= Ball("./beach_ball.png", location, speed)
        ball_group.append(myBall)

#myBall= Ball("red_ball.png", (100,200), (-5,-5))
#ball_group.append(ball)
#myBall= Ball("bulb.png", (200,100), (-2,3))
#ball_group.append(ball)

while True:
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    SURFACE.fill((200,255,255))

    for myBall in ball_group:
        myBall.move()
        SURFACE.blit(myBall.image, myBall.rect)

    for myBall in ball_group:
        if len(myBall.rect.collidelistall(ball_group)) >= 2:
            myBall.speed[0] = -myBall.speed[0]
            myBall.speed[1] = -myBall.speed[1]
    
    pygame.display.update()
    FPSCLOCK.tick(50)
