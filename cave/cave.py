import sys
from random import randint
import pygame
from pygame.locals import QUIT, Rect, KEYDOWN, K_SPACE
import keyboard

pygame.init()
pygame.key.set_repeat(5, 5) # 누르고 있어도 동작
SURFACE = pygame.display.set_mode((800, 600))
FPSCLOCK = pygame.time.Clock() # FPS - frame per sec /게임속도

def main():
    """ 메인 루틴 """
    walls = 80
    ship_y = 250
    velocity = 0
    score = 0
    slope = randint(1, 6)
    sysfont = pygame.font.SysFont(None, 36)
    ship_image = pygame.image.load("ship.png")
    aShip_image = pygame.image.load("aShip.png")
    bang_image = pygame.image.load("bang.png")
    coin_image = pygame.image.load("coin.png")
    holes = []
    for xpos in range(walls):
        holes.append(Rect(xpos * 10, 100, 10, 400))
    game_over = False

    while True:
        is_space_down = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_SPACE:
                    is_space_down = True
            elif keyboard.is_pressed('a'):
                FPSCLOCK.tick(3)
                SURFACE.fill((255,0,255))
                SURFACE.blit(aShip_image, (0, ship_y))
                pygame.display.update()

        # 내 캐릭터를 이동
        if not game_over:
            score += 10
            velocity += -3 if is_space_down else 3
            ship_y += velocity

            # 동굴을 스크롤
            edge = holes[-1].copy()
            test = edge.move(0, slope)
            if test.top <= 0 or test.bottom >= 600:
                slope = randint(1, 6) * (-1 if slope > 0 else 1)
                edge.inflate_ip(0, -20)
            edge.move_ip(10, slope)
            holes.append(edge)
            del holes[0]
            holes = [x.move(-10, 0) for x in holes]

            # 코인얻으면 score +500
           # if test.top <= 0 or test.bottom >= 600:
                

            # 충돌?
            if holes[0].top > ship_y or \
                holes[0].bottom < ship_y + 80:
                game_over = True

        # 그리기
        SURFACE.fill((0, 255, 0))
        for hole in holes:
            pygame.draw.rect(SURFACE, (0, 0, 0), hole)
        SURFACE.blit(ship_image, (0, ship_y))
        score_image = sysfont.render("score is {}".format(score),
                                     True, (0, 0, 225))
        SURFACE.blit(score_image, (600, 20))
        skill_string = sysfont.render("press skill 'a'",
                                      True, (255, 255, 0))
        SURFACE.blit(skill_string, (600, 50))

        if game_over:
            SURFACE.blit(bang_image, (0, ship_y-40))

        pygame.display.update()
        FPSCLOCK.tick(15)
        
   #     if keyboard.is_pressed('a'):
   #         FPSCLOCK.tick(3)
   #         SURFACE.fill((255,0,255))
   #         SURFACE.blit(aShip_image, (0, ship_y))
   #         pygame.display.update() 
        

if __name__ == '__main__':
    main()
