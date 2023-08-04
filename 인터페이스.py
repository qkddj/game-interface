import pygame

class interface: 

    def Hpbar(hpbar_coordinate, hp, color):

        pygame.draw.rect(screen, (128,128,128), hpbar_coordinate)
        pygame.draw.rect(screen, color, [hpbar_coordinate[0], hpbar_coordinate[1], hp, hpbar_coordinate[3]])
        pygame.draw.rect(screen, (0,0,0), [hpbar_coordinate[0]-4, hpbar_coordinate[1]-4, hpbar_coordinate[2]+8, hpbar_coordinate[3]+8], 4)
    
    def itembar(itembar_coordinate, Count):
        pygame.draw.rect(screen, (200,200,200), itembar_coordinate)
        pygame.draw.rect(screen, (50,50,50),[itembar_coordinate[0], itembar_coordinate[1], itembar_coordinate[2]/2, itembar_coordinate[3]])
        pygame.draw.rect(screen, (0,0,0),[itembar_coordinate[0]-4, itembar_coordinate[1]-4, itembar_coordinate[2]+8, itembar_coordinate[3]+8], 4)
        myfont = pygame.font.SysFont(None, itembar_coordinate[3])
        mytext = myfont.render(str(Count), True, (0,0,0))
        screen.blit(mytext, (itembar_coordinate[0]+itembar_coordinate[2]/1.45,itembar_coordinate[1]+itembar_coordinate[3]/5))
        pygame.display.update()




pygame.init()

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE  = (  0,   0, 255)
GREEN = (  0, 255,   0)
RED   = (255,   0,   0)
GRAY  = (128, 128, 128)
 
size   = [1000, 1000]
screen = pygame.display.set_mode(size)
  
pygame.display.set_caption("Game Title")
  
done = False
clock = pygame.time.Clock()

hpbar_coordinate1 = [75, 175, 400, 30]
hpbar_coordinate2 = [75, 275, 400, 30]
hacker_hp = hpbar_coordinate1[2]
enemy_hp = hpbar_coordinate1[2]
Count = 9
a=0

itembar_coordinate = [75, 375, 100, 50]

while not done:

    clock.tick(10)
     
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=True

    screen.fill(WHITE)
    
    interface.Hpbar(hpbar_coordinate1, hacker_hp, BLUE)
    interface.Hpbar(hpbar_coordinate2, enemy_hp, RED)
    interface.itembar(itembar_coordinate, Count)
    hacker_hp -= 1
    enemy_hp -= 10
    a+=1
    if a == 10:
        Count -= 1
        a=0
    
    pygame.display.flip()

pygame.quit()

