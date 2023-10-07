import pygame as pg
import random



class Football(pg.sprite.Sprite):
    def __init__(self, rect,ball,rect_6,rect_7,rect_8,rect_9,rect_10):
        pg.sprite.Sprite.__init__(self)
        rect_sp=[rect_6,rect_7,rect_8,rect_9,rect_10]
        m=random.randint(1,2)
        if m == 1:
            self.speedx = 'right'
        else:
            self.speedx = 'left'

        if m == 1:
            self.speedy = 'down'
        else:
            self.speedy = 'up'
        keys = pg.key.get_pressed()


        if keys[pg.K_RIGHT]:
            rect.x += 10
            if ball.colliderect(rect):
                self.speedx = 'left' if self.speedx == 'right' else 'right'
                self.speedy = 'up' if self.speedy == 'down' else 'down'
                ball.x+=10
        
        if keys[pg.K_UP]:
            rect.y -= 10
            if ball.colliderect(rect):
                self.speedx = 'left' if self.speedx == 'right' else 'right'
                self.speedy = 'up' if self.speedy == 'down' else 'down'
                ball.y-=10
        if keys[pg.K_DOWN]:
            rect.y += 10
            if ball.colliderect(rect):
                self.speedx = 'left' if self.speedx == 'right' else 'right'
                self.speedy = 'up' if self.speedy == 'down' else 'down'
                ball.y+=10
        if keys[pg.K_LEFT]:
            rect.x -= 10
            if ball.colliderect(rect):
                self.speedx = 'left' if self.speedx == 'right' else 'right'
                self.speedy = 'up' if self.speedy == 'down' else 'down'
                ball.x-=10
                if keys[pg.K_f]:
                    ball.x+=5
                for i in rect_sp:
                    if ball.colliderect(i):
                        self.speedx = 'left' if self.speedx == 'right' else 'right'
                        self.speedy = 'up' if self.speedy == 'down' else 'down'
                        rect.x += 10
                        ball.x+=10
        if keys[pg.K_SPACE]:
            rect.x -= 1
            if ball.colliderect(rect):
                self.speedx = 'left' if self.speedx == 'right' else 'right'
                self.speedy = 'up' if self.speedy == 'down' else 'down'
                ball.x-=150


    
    def area(rect,wall,speedx,speedy):
        for i in wall:
            if i.colliderect(rect):
                    speedx = 'left' if speedx == 'right' else 'right'
                    speedy = 'up' if speedy == 'down' else 'down'
                    if i == wall[0]:
                        rect.y+=10
                    if i == wall[1]:
                        rect.y-=10
                    if i == wall[2]:
                        rect.x+=10
                    if i == wall[3]:
                        rect.x-=10
                    

    def attack(forward, ball, door, speedx, speedy, rect_we):
        if ball.x >= forward.x:
            forward.x += 7
            for i in rect_we:
                if ball.colliderect(i):
                    speedx = 'left' if speedx == 'right' else 'right'
                    speedy = 'up' if speedy == 'down' else 'down'
                    if i.centery > forward.y:
                        forward.y -= 14
                        ball.y -= 14
                    elif i.centery < forward.y:
                        forward.y += 14
                        ball.y += 14
                    forward.x -= 7
                    ball.x -= 7
        elif ball.x <= forward.x:
            forward.x -= 7
        if ball.y+14 > forward.centery:
            forward.y += 7
        elif ball.y+14 < forward.centery:
            forward.y -= 7
        if forward.x > door.x:
            if ball.colliderect(forward):
                speedx = 'left' if speedx == 'right' else 'right'
                speedy = 'up' if speedy == 'down' else 'down'
                ball.x += 7
                # forward.x += 7
        if forward.y >= door.y:
            if ball.colliderect(forward):
                speedx = 'left' if speedx == 'right' else 'right'
                speedy = 'up' if speedy == 'down' else 'down'
                ball.y -= 7
                forward.y -= 7
        elif forward.y <= door.y:
            if ball.colliderect(forward):
                speedx = 'left' if speedx == 'right' else 'right'
                speedy = 'up' if speedy == 'down' else 'down'
                ball.y += 7
                forward.y += 7
        

        


    # def enemy_touch(ball,rect,direction):
    #     m=random.randint(1,2)
    #     if m == 1:
    #         speedx = 'right'
    #     else:
    #         speedx = 'left'

    #     if m == 1:
    #         speedy = 'down'
    #     else:
    #         speedy = 'up'
    #     if direction=='down':
    #         if ball.colliderect(rect):
    #             speedx = 'left' if speedx == 'right' else 'right'
    #             speedy = 'up' if speedy == 'down' else 'down'
    #             ball.y+=3

    #     if direction=='up':
    #         if ball.colliderect(rect):
    #             speedx = 'left' if speedx == 'right' else 'right'
    #             speedy = 'up' if speedy == 'down' else 'down'
    #             ball.y-=3