import pygame as pg
import time
import random
from sprite import *
pg.init()

size = (1500,750)
screen = pg.display.set_mode(size)
pg.display.set_caption("Fifa 25")

fps = 30
clock = pg.time.Clock()
fon = pg.image.load('Field.jpg')
f = pg.transform.scale(fon, size)
ball = pg.Rect(size[0] // 2-18,size[1] // 2-5, 30, 30)
rect_1 = pg.Rect(1350, 340, 25, 75)
rect_2 = pg.Rect(1200, 200, 25, 75)
rect_3 = pg.Rect(1200, 478, 25, 75)
rect_4 = pg.Rect(1050, 340, 25, 75)
rect_5 = pg.Rect(900, 340, 25, 75)
rect_6 = pg.Rect(125, 340, 25, 75)
rect_7 = pg.Rect(280, 200, 25, 75)
rect_8 = pg.Rect(280, 478, 25, 75)
rect_9 = pg.Rect(420, 340, 25, 75)
rect_10 = pg.Rect(570, 340, 25, 75)
door_p=pg.Rect(-26, 278, 100, 195)
door_y=pg.Rect(size[0]-75, 278, 100, 195)


# def Enemy(rect_6, rect_7, rect_8, rect_9, rect_10):

    # if rect_6.y == 175:  # Изменили условие на <=
    #     direction = 'down'
    # if rect_6.y >= 400:  # Изменили условие на >=
    #     a = 'up'
    # if a == 'down':
    #     rect_6.y += 10
    #     rect_7.y -= 10
    #     rect_7.x -= 10
    #     rect_8.y += 10
    #     rect_8.x -= 10
    # if a == "up":
    #     rect_6.y -= 10
    #     rect_7.y += 10
    #     rect_7.x += 10
    #     rect_8.y -= 10
    #     rect_8.x += 10

m = random.randint(1, 2)
blue=0
red=0
f_count=pg.font.Font('font.otf', 100)  
def Count_screen():
    text1 = f_count.render(f'{blue} - {red}', True, pg.Color('black'))
    text_rect1 = text1.get_rect(center=(size[0] // 2,75))
    screen.blit(text1, text_rect1)

f_number=pg.font.Font('font.otf', 55)
def number(number,rectx,recty):
    text1 = f_number.render(number, True, pg.Color('black'))
    text_rect1 = text1.get_rect(center=(rectx,recty))
    screen.blit(text1, text_rect1)


# def Count_final():
#     if blue > red:
#         text2 = f_count.render(f'Синий игрок победил, {blue} - {red}', True ,pg.Color('blue'))
#     else:
#         text2 = f_count.render(f'Красный игрок победил, {blue} - {red}', True, pg.Color('red'))
#     text_rect2 = text2.get_rect(center=(size[0] // 2, size[1] // 2))
#     screen.blit(text2, text_rect2)

if m == 1:
    speedx = 'right'
else:
    speedx = 'left'

if m == 1:
    speedy = 'down'
else:
    speedy = 'up'

def Count():
    if blue<red:
        print(f'Ты выиграл!!!,{blue}-{red}')
    elif red<blue:
        print(f'ИИ выиграл!,{blue}-{red}')
    elif blue==red:
        print(f'Ничья,{blue}-{red}')
    

fifa=Football
        
direction='down'

t=True
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            Count()
            pg.quit()
            quit()
    if t==True:
        start_timer=time.time()
        t=False
    screen.blit(f, (0, 0))
    pg.draw.rect(screen, pg.Color(225,105,225), rect_1)
    pg.draw.rect(screen, pg.Color(225,105,225), rect_2)
    pg.draw.rect(screen, pg.Color(225,105,225), rect_3)
    pg.draw.rect(screen, pg.Color(225,105,225), rect_4)
    pg.draw.rect(screen, pg.Color(225,105,225), rect_5)
    pg.draw.rect(screen, pg.Color(225,225,0), rect_6)
    pg.draw.rect(screen, pg.Color(225,225,0), rect_7)
    pg.draw.rect(screen, pg.Color(225,225,0), rect_8)
    pg.draw.rect(screen, pg.Color(225,225,0), rect_9)
    pg.draw.rect(screen, pg.Color(225,225,0), rect_10)
    pg.draw.ellipse(screen, pg.Color('black'), ball)
    wall_1=pg.draw.line(screen, pg.Color('black'), (70, 25), (1429, 25), 6)
    wall_2=pg.draw.line(screen, pg.Color('black'), (70, 725), (1429,725), 6)
    wall_3=pg.draw.line(screen, pg.Color('black'), (70, 24), (70, 726), 6)
    wall_4=pg.draw.line(screen, pg.Color('black'), (1427, 25), (1427, 725), 6)
    pg.draw.rect(screen, pg.Color(225,225,0), door_y)
    pg.draw.rect(screen, pg.Color(225,105,225), door_p)

    number('1',rect_1.x+10,rect_1.y+35)
    number('2',rect_2.x+10,rect_2.y+35)
    number('3',rect_3.x+10,rect_3.y+35)
    number('4',rect_4.x+10,rect_4.y+35)
    number('5',rect_5.x+10,rect_5.y+35)


    keys = pg.key.get_pressed()

    rect_sp_e=[rect_1,rect_2,rect_3,rect_4,rect_5]

    if keys[pg.K_1]:
        fifa(rect_1, ball,rect_6,rect_7,rect_8,rect_9,rect_10)
    if keys[pg.K_2]:
        fifa(rect_2, ball,rect_6,rect_7,rect_8,rect_9,rect_10)
    if keys[pg.K_3]:
        fifa(rect_3, ball,rect_6,rect_7,rect_8,rect_9,rect_10)
    if keys[pg.K_4]:
        fifa(rect_4, ball,rect_6,rect_7,rect_8,rect_9,rect_10)
    if keys[pg.K_5]:
        fifa(rect_5, ball,rect_6,rect_7,rect_8,rect_9,rect_10)

    rect_we=[rect_1,rect_2,rect_3,rect_4,rect_5]
    a=rect_10.x-ball.x
    b=rect_9.x-ball.x
    if abs(b)>abs(a):
        fifa.attack(rect_10,ball, door_p,speedx,speedy,rect_we)
    if abs(b)<abs(a):
        fifa.attack(rect_9,ball, door_p,speedx,speedy,rect_we)
        

    if ball.colliderect(door_y):
            speedx = 'left' if speedx == 'right' else 'right'
            # speedy = 'up' if speedy == 'down' else 'down'
            ball.center=(size[0] // 2, size[1] // 2)
            blue+=1
            speedx='left'
            rect_1.topleft=(1350, 340)
            rect_2.topleft=(1200, 200)
            rect_3.topleft=(1200, 478)
            rect_4.topleft=(1050, 340)
            rect_5.topleft=(900, 340)
            rect_6.topleft=(125, 340)
            rect_7.topleft=(280,200)
            rect_8.topleft=(280, 478)
            rect_9.topleft=(420, 340)
            rect_10.topleft=(570, 340)
            

    if ball.colliderect(door_p):
        speedx = 'left' if speedx == 'right' else 'right'
        # speedy = 'up' if speedy == 'down' else 'down'
        ball.center=(size[0] // 2, size[1] // 2)
        rect_1.topleft=(1350, 340)
        rect_2.topleft=(1200, 200)
        rect_3.topleft=(1200, 478)
        rect_4.topleft=(1050, 340)
        rect_5.topleft=(900, 340)
        rect_6.topleft=(125, 340)
        rect_7.topleft=(280,200)
        rect_8.topleft=(280, 478)
        rect_9.topleft=(420, 340)
        rect_10.topleft=(570, 340)
        red+=1
        speedx='right'

    # Enemy(rect_6,rect_7,rect_8,rect_9,rect_10)

    if rect_7.y <= 150:  # Изменили условие на <=
        direction = 'up'
    if rect_7.y >= 250:  # Изменили условие на >=
        direction = 'down'
    if direction == 'up':
        # rect_6.y += 5
        rect_7.y += 4
        # rect_7.x -= 4
        rect_8.y -= 4
        # rect_8.x -= 4
    if direction == "down":
        # rect_6.y -= 5
        rect_7.y -= 4
        # rect_7.x += 4
        rect_8.y += 4
        # rect_8.x += 4
    if ball.x<60:
        ball.center=(size[0] // 2, size[1] // 2)

    if ball.centery<=rect_6.centery:
            rect_6.y -=5
    if ball.centery>=rect_6.centery:
            rect_6.y +=5


    # fifa.enemy_touch(ball,rect_6,direction)
    # fifa.enemy_touch(ball,rect_7,direction)
    # fifa.enemy_touch(ball,rect_8,direction)
    # fifa.enemy_touch(ball,rect_9,direction)

    # if ball.colliderect(rect_6):
    #     speedx = 'left' if speedx == 'right' else 'right'
    #     speedy = 'up' if speedy == 'down' else 'down'

    wall=[wall_1,wall_2,wall_3,wall_4]
    fifa.area(rect_1,wall,speedx,speedy)
    fifa.area(rect_2,wall,speedx,speedy)
    fifa.area(rect_3,wall,speedx,speedy)
    fifa.area(rect_4,wall,speedx,speedy)
    fifa.area(rect_5,wall,speedx,speedy)
    fifa.area(rect_6,wall,speedx,speedy)
    fifa.area(rect_7,wall,speedx,speedy)
    fifa.area(rect_8,wall,speedx,speedy)
    fifa.area(rect_9,wall,speedx,speedy)
    fifa.area(rect_10,wall,speedx,speedy)
    fifa.area(ball,wall,speedx,speedy)

    
    f_timer=pg.font.Font('font.otf', 60)
    for i in range(300):
        current_time=int(time.time() - start_timer)
        if current_time==i:
            if i<60:
                vremya = f_timer.render(f'time:{0}. {i}', True, pg.Color('black'))
            elif i<120:
                vremya = f_timer.render(f'time:{1}. {i-60}', True, pg.Color('black'))
            elif i<180:
                vremya = f_timer.render(f'time:{2}. {i-120}', True, pg.Color('black'))
            elif i<240:
                vremya = f_timer.render(f'time:{3}. {i-180}', True, pg.Color('black'))
            elif i<300:
                vremya = f_timer.render(f'time:{4}. {i-240}', True, pg.Color('red'))
            vremya_rect = vremya.get_rect(center=(size[0] // 2+500,75))
            screen.blit(vremya, vremya_rect)
            


    
    if time.time()-start_timer > 300:
        Count()
        break
        

    if fps==100000000000:
        print('чо? почему это сработало? у меня фпс 100000000000 что ли? ашалеть')
    Count_screen()
    pg.display.flip()
    clock.tick(fps)