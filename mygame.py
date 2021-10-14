import pygame, sys

pygame.init()
SURFACE = pygame.display.set_mode((800,500))
SURFACE.fill((102,255,255))

pygame.draw.rect(SURFACE, (0,0,255), (100,50,150,100), 5)
points = ((100,100),(200,50),(250,150),(180,210),(110,170)) #좌표리스트
pygame.draw.polygon(SURFACE,(255,255,255),points)
pygame.draw.line(SURFACE,(0,0,0),(50,50),(100,150),3)
triangle = ((200,250),(100,400),(300,400))
pygame.draw.lines(SURFACE,(0,255,0),True,triangle,2)
#pygame.draw.polygon(SURFACE,(255,0,0),triangle)
pygame.draw.circle(SURFACE,(255,0,255),(250,250),50)
pygame.draw.ellipse(SURFACE,(255,255,0),(400,100,100,150),5)
pygame.display.update()

ball = pygame.image.load("이미지/beach_ball.png")
SURFACE.blit(ball, (50,50))

w = ball.get_width
h = ball.get_height
#SURFACE,blit(ball,(100+w,50), (0,0,w,h/2))

for i in range(5): #공 이동 구현
    SURFACE.fill((102,255,255))
    SURFACE.blit(ball, (i*100+50,300))
    pygame.display.update()
    pygame.time.delay(200)

logoImg = pygame.image.load("이미지/pythonlogo.jpg")
#img1 = pygame.transform.scale(logoImg,(200,300))
#img2 = pygame.transform.scale(logoImg,(100,100))
img3 = pygame.transform.rotozoom(logoImg, 45, 0.5)
img4 = pygame.transform.rotozoom(logoImg, 45, 1.5)

img1 = pygame.transform.rotate(logoImg,0)             
img2 = pygame.transform.rotate(logoImg,90)
#img3 = pygame.transform.rotate(logoImg,180)
#img4 = pygame.transform.rotate(logoImg,45)
SURFACE.blit(img1, (0,0))
SURFACE.blit(img2, (200,0))
SURFACE.blit(img3, (400,0))
SURFACE.blit(img4, (600,00))

pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

