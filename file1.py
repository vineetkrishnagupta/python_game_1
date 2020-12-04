import pygame
import random
pygame.init()
gamewindow=pygame.display.set_mode()
pygame.display.set_caption("supper snake")
game_over=False
game_puss=False
fps=100
clock=pygame.time.Clock()
x_max,y_max=pygame.display.get_window_size()
print("x ",x_max,"y ",y_max)
food_x=random.randint(30,x_max-30)
food_y=random.randint(30,y_max-30)
font_1=pygame.font.SysFont("time romen",55)
food_size=20
snake_x=55;snake_y=55
snake_size=45
score=0
snake_speed=5
snake_len=1
snake_list=[]
user_input=None
def polt_snake(window,color,snk_list,snk_size):
    for x,y in snk_list:
        pygame.draw.rect(window,color,[x,y,snk_size,snk_size])
def set_lines():
    pygame.draw.line(gamewindow, 'white', [x_max - 20, 10], [x_max - 20, 50], 10)
    pygame.draw.line(gamewindow, 'white', [x_max - 40, 10], [x_max - 40, 50], 10)
while not game_over:
    gamewindow.fill('black')
    clock.tick(fps)
    set_lines()
    pygame.draw.circle(gamewindow,"green",[food_x,food_y],food_size)
    score_font=font_1.render(f"score - {str(score)}",True,"white")
    gamewindow.blit(score_font,[10,10])
    polt_snake(gamewindow,"white",snake_list,snake_size)
    head=[]
    head.append(snake_x)
    head.append(snake_y)
    snake_list.append(head)
    if len(snake_list)>snake_len:
        del snake_list[0]
    pygame.draw.rect(gamewindow, 'red', [snake_x, snake_y, snake_size, snake_size])
    pygame.display.update()
    if snake_x>=x_max:
        snake_x=0
    elif snake_x<=0:
        snake_x=x_max
    elif snake_y>=y_max:
        snake_y=0
    elif snake_y<=0:
        snake_y=y_max
    if(abs((snake_x+(snake_size/2))-food_x)<=40 and abs((snake_y+(snake_size/2))-food_y)<=40):
        food_x=random.randint(30,x_max-30)
        food_y=random.randint(30,y_max-30)
        score+=10
        snake_len+=5
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            quit()
        if event.type==pygame.MOUSEBUTTONUP:
            x,y=pygame.mouse.get_pos()
            print(x,y)
            if x>=x_max-40 and x<=x_max-20 and y>=10 and y<=50:
                print('jjjj')
                x,y=0,0
                print(x,y)
                pygame.draw.line(gamewindow, 'red', [x_max - 20, 10], [x_max - 20, 50], 10)
                pygame.draw.line(gamewindow, 'red', [x_max - 40, 10], [x_max - 40, 50], 10)
                pygame.display.update()
                game_puss=False
                while not game_puss:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            quit()
                        if event.type == pygame.MOUSEBUTTONUP:
                            x, y = pygame.mouse.get_pos()
                            if x >= x_max - 40 and x <= x_max - 20 and y >= 10 and y <= 50:
                                game_puss=True

        if event.type==pygame.KEYDOWN:
            if event.key== pygame.K_UP:
                if user_input != 'y--':
                    user_input='y++'
            if event.key== pygame.K_DOWN:
                if user_input != 'y++':
                    user_input='y--'
            if event.key== pygame.K_LEFT:
                if user_input != 'x++':
                    user_input='x--'
            if event.key== pygame.K_RIGHT:
                if user_input != 'x--':
                    user_input='x++'
            if event.key== pygame.K_q or event.key==pygame.K_ESCAPE:
                pygame.quit()
                quit()
    if user_input=='x++':
        snake_x=snake_x+snake_speed
    if user_input=='x--':
        snake_x=snake_x-snake_speed
    if user_input=='y++':
        snake_y=snake_y-snake_speed
    if user_input=='y--':
        snake_y=snake_y+snake_speed
