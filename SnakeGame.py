import pygame
import random as rd
import time
x=pygame.init()
screen_width=1200
screen_height=600
white=(255,255,255)
red=(255,0,0)
black=(0,0,0)
gamewindow=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('My First Game')
exit_game=False
game_over=False
snake_x=55
snake_y=55
velocity_x=5
velocity_y=5
snake_size=50
fx1=0
fx2=screen_width-snake_size-10
fy1=70
fy2=screen_height-snake_size-10
food_x=rd.randint(fx1,fx2)
food_y=rd.randint(fy1,fy2)
clock=pygame.time.Clock()
fps=40
flag=6
score=0
eat_flag=0
vxflag=0
vyflag=0
font=pygame.font.SysFont(None,55)
def text_screen(text,color,x,y):
    screen_text=font.render(text,True,color)
    gamewindow.blit(screen_text,(x,y))
head=[[45,45]]
snake_length=1
def snake(gamewindow,color,head1,snake_size):
    for x,y in head1:
        pygame.draw.rect(gamewindow,color,[x,y, snake_size, snake_size])
        pygame.draw.rect(gamewindow,red,[snake_x,snake_y, 10, 10])
        
    
while not exit_game:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit_game==True
            pygame.display.quit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                #snake_x+=abs(snake_size-velocity_x)
                flag=6
            elif event.key==pygame.K_LEFT:
                #snake_x-=abs(snake_size-velocity_x)
                flag=4
            elif event.key==pygame.K_UP:
                #snake_y-=abs(snake_size-velocity_y)
                flag=8
            elif event.key==pygame.K_DOWN:
                #snake_y+=abs(snake_size-velocity_y)
                flag=2  
    if flag==6 :
        snake_x+=velocity_x
    if flag==4 :
        snake_x-=velocity_x
    if flag==8 :
        snake_y-=velocity_y
    if flag==2 :
        snake_y+=velocity_y
    if snake_x==0:
        flag=6
        #print('1')
    if snake_x==screen_width:
        flag=4
        #print('2')
    if snake_y==0:
        flag=2
        #print('3')
    if snake_y==screen_height:
        flag=8
        #print('4')
    if snake_y>=screen_height and vyflag!=2:
        snake_y=0
        vyflag=1
        flag=2
        #print('5')
    if snake_x>=screen_width and vxflag!=2:
        snake_x=0
        vxflag=1
        flag=6
        #print('6')
    if (snake_y<=0) and vyflag!=1:
        snake_y=screen_height
        flag=8
        vyflag=2
        #print('7')
    if (snake_x<=0) and vxflag!=1:
        snake_x=screen_width
        flag=4
        vxflag=2
        #print('8')
    if abs(snake_y-0)>=velocity_y and abs(snake_y-screen_height)>=velocity_y:
        vyflag=0
        #print('9')
    if abs(snake_x-0)>=velocity_x and abs(snake_x-screen_width)>=velocity_x:
        vxflag=0
        #print('10')
    head.append([snake_x,snake_y])
    #print(snake_x,snake_y,vxflag,vyflag,flag)
    if abs(snake_x-food_x)< (snake_size//2)+1 and abs(snake_y-food_y)< (snake_size//2)+1:
        score+=10
        eat_flag=1
        snake_length+=snake_size//10
        #print(head)
        '''print('food_x',food_x)
        print('food_y',food_y)'''
        food_x=rd.randint(fx1,fx2)
        food_y=rd.randint(fy1,fy2)
        #print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        while [food_x,food_y] in head[1:]:
            food_x=rd.randint(fx1,fx2)
            food_y=rd.randint(fy1,fy2)
    if len(head)>snake_length:
        a=len(head)-snake_length
        for i in range(a):
            del head[i]
    if score%20==0 and eat_flag==1:
        eat_flag=0
        velocity_x+=1
        velocity_y+=1
    gamewindow.fill(white)
    text_screen('SCORE : '+str(score),red,5,5)
    snake(gamewindow,black,head, snake_size)
    pygame.draw.rect(gamewindow,red,[food_x,food_y, snake_size, snake_size])
    pygame.draw.rect(gamewindow,black,[food_x,food_y, 10, 10])
    clock.tick(fps)
    pygame.display.update()

  
pygame.quit()
quit()
