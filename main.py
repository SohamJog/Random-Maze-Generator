import pygame
import random


pygame.init()

N = 20
offset = 10         #pixels
gap = 2

WIDTH, HEIGHT = 610, 610
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
BLACK = (0,0,0)
WHITE=(255, 255, 255)
BLUE = (0,255,255)
RED = (255, 0, 0)
GREEN = (0,255,0)

SCALE = (WIDTH-offset)/N


vis = {}
val = {}
for i in range(N):
    vis[i] = []
    val[i] = []
    for j in range(N):
        vis[i].append(False)
        val[i].append(15)




def draw():

    for i in range(N):
        for j in range(N):
            if(vis[i][j]==False):continue

            coords = [(SCALE*i), (SCALE*j), SCALE, SCALE]
            if(val[i][j]&8): coords[2]-=gap
            if(val[i][j]&4): coords[3]-=gap
            pygame.draw.rect(WIN, WHITE, ((offset/2)+coords[0], (offset/2)+coords[1], coords[2], coords[3]))



'''
1 up wall
2 left wall
4 down wall
8 right wall

'''

#down, right, up, left
dx = [0,1,0,-1]
dy = [1,0,-1,0]

def dfs(x,y):

    vis[x][y] = True

    draw()
    pygame.display.update()
    pygame.time.delay(40)

    temp = [0,2,3,1]
    random.shuffle(temp)
    for i in temp:
        X = dx[i]+x
        Y = dy[i]+y
        if(X<0 or Y<0 or X>=N or Y>=N):continue
        if vis[X][Y]: continue
        val[X][Y] -= 2**i
        val[x][y] -= 2**((i+2)%4)
        dfs(X,Y)



run = True
execute = False
done = False
isPressed = False
val[0][0]-=1 
val[N-1][N-1]-=8


WIN.fill((0,0,0))

while run:

    #time delay


    for event in pygame.event.get():
        if (event.type==pygame.QUIT): run = False
    
    
    
    
    keys = pygame.key.get_pressed()

  
    if keys[pygame.K_SPACE]:
        execute = True


    if(execute):
        if(vis[0][0]==False):
            dfs(0,0)
            #print(val)



 
pygame.quit()


