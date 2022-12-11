import sys
import numpy
import pygame
from game.src.facade import *
from game.src.config import *
from typing import List, Tuple, Callable

def exit() -> None:
    """Exit the game"""

    quit()
    sys.exit()
    
def projectile_collided(projectile_origin: Vector2, projectile_size: Vector2, rects: List[Rect]) -> bool:
    """Returns boolean that represents if bulltes to collide
    
    :param projectile_origin: 
    :type projectile_origin: Vector2
    :param projectile_direction: 
    :type projectile_direction: Vector2
    :param rects:
    :type rects: List[Rect]

    :returns: a boolean representing whether it was a collision
    :rtype: boolean
    """
    collision = False

    if projectile_origin.x >= tela.size.x or projectile_origin.x <= 0:
        collision = True
    
    if projectile_origin.y + projectile_size.y >= tela.size.y or projectile_origin.y - projectile_size.y <= 0:
        collision = True

    for rect in rects:
        if rect.colliderect(Rect(projectile_origin.x, projectile_origin.y, projectile_size.x, projectile_size.y)):
            collision = True
            break


    return collision

def update_menu(play_enable: bool) -> bool:
    tela.close()
   
    menu = True
    if play_enable:
        menu = False
    
    return menu

def creat_button(text: str, size: Vector2, position: Vector2, function: Callable):
    button: List[Vector2, Vector2] = []
    mouse_pos = mouse_position()
    if button_jogar_position.x <= mouse_pos.x <= button_jogar_position.x + button_size.x and button_jogar_position.y <= mouse_pos.y <= button_jogar_position.y + button_size.y:
        #Aqui será o botão cinza
        button = draw.rect(tela.surface, color_light,(button_jogar_position, button_size))  
          
    else: 
        #Aqui será o botão preto
        button = draw.rect(tela.surface, color_dark,(button_jogar_position, button_size))    
    return button


class Game(object):
    def __init__(self) -> None:
        self.fire_rate = 50
        self.waiting_time = self.fire_rate
        self.inMenu = True
        self.inGame = False
        self.inPause = False
        self.phase_1 = phase_1
        self.phase_2 = phase_2
        self.walls: List[Rect] = []
        self.bullets: List[Tuple[bool, Vector2, Vector2, Vector2]] = []
        self.bullet_speed = 1
        self.player: Rect =  player.update()



    def run(self):
        all_items = get_random_items(items)
        positions = [Vector2(50, 50), Vector2(144, 50 + items_size.y + 5), Vector2(711, 54 + 2 * items_size.y), Vector2(400, 65 + 3 * items_size.y)]
        while self.inMenu:
            tela.surface.blit(tela_background_image, (0, 0))
            write("v.1.0")
            write("Ghostware", position=Vector2(tela_center.x - 140, tela_center.y-200), bg_color=(0, 0, 0), font=get_font("Agency FB", 90))
            self.inMenu = update_menu(self.inGame)
            left_click, scroll_click, right_click = mouse.get_pressed()
            mouse_pos = mouse_position()

            
            for i in range(0, len(all_items)):
                tela.surface.blit(all_items[i], positions[i]) 

            if left_click:
                #Criando cada um dos botões...
                if button_jogar_position.x <= mouse_pos.x <= button_jogar_position.x + button_size.x and button_jogar_position.y <= mouse_pos.y <= button_jogar_position.y + button_size.y:
                    mixer.music.play()
                    self.inGame = True
                    return self.play()
                
                if button_quit_position.x <= mouse_pos.x <= button_quit_position.x + button_size.x and button_quit_position.y <= mouse_pos.y <= button_quit_position.y + button_size.y:
                    mixer.music.play()
                    quit() 
                
                if button_help_position.x <= mouse_pos.x <= button_help_position.x + button_size.x and button_help_position.y  <= mouse_pos.y <= button_help_position.y + button_size.y:
                    mixer.music.play()
                    draw.rect(tela.surface, [128]*3, (Vector2(tela_center.x - 100, tela_center.y - 80), Vector2(tela_center.x - 180, tela_center.y - 140)))
                    write("Press WASD to walk", position=Vector2(tela_center.x - 70, tela_center.y + 50))      
                    write("Click to attack", position=Vector2(tela_center.x - 70, tela_center.y - 10))      
                    write("Press Esc to skip", position=Vector2(tela_center.x - 70, tela_center.y - 65))


            for pos in positions:
                index = positions.index(pos)
                if index % 2 == 0:
                    if pos.x < 0 - all_items[index].get_rect().w:
                        pos.x = tela.size.x
                    else:
                        pos.x -= 0.5
                else:
                    if pos.x > tela.size.x:
                        pos.x = 0 - all_items[index].get_rect().w
                    else:
                        pos.x += 0.5     
            
            
            #pegando a posição do mouse
            # creat_button("Jogar", button_size, button_jogar_position)
            # #botão iniciar
            if button_jogar_position.x <= mouse_pos.x <= button_jogar_position.x + button_size.x and button_jogar_position.y <= mouse_pos.y <= button_jogar_position.y + button_size.y:
                #Aqui será o botão cinza
                draw.rect(tela.surface,color_light,(button_jogar_position, button_size))  
                
            else: 
                #Aqui será o botão preto
                draw.rect(tela.surface,color_dark,(button_jogar_position, button_size))    

            #Botão quit

            if button_quit_position.x <= mouse_pos.x <= button_quit_position.x + button_size.x and button_quit_position.y <= mouse_pos.y <= button_quit_position.y + button_size.y:
                #Aqui será o botão cinza
                draw.rect(tela.surface,color_light,(button_quit_position, button_size))
            else: 
                #Aqui será o botão preto
                draw.rect(tela.surface,color_dark,(button_quit_position, button_size)) 

            # #Aqui será os texto que representarão Jogar e Quit
                
            if button_help_position.x <= mouse_pos.x <= button_help_position.x + button_size.x and button_help_position.y  <= mouse_pos.y <= button_help_position.y + button_size.y:
                #Aqui será o botão cinza
                draw.rect(tela.surface,color_light,(button_help_position, button_size))
            else: 
                #Aqui será o botão preto
                draw.rect(tela.surface,color_dark,(button_help_position, button_size))
            

            #Aqui será os texto que representarão Jogar e Quit
            
            
            tela.surface.blit(text_1, (button_jogar_position.x + 30,button_jogar_position.y))#texto 
            tela.surface.blit(text_2, (button_quit_position.x + 40, button_quit_position.y ))
            tela.surface.blit(text_3, (button_help_position.x + 40, button_help_position.y ))
            display.update()

    def play(self):
        next_phase = False
        while self.inGame:
            """main loop responsible for drawing things on the tela"""
            while not self.inPause:

                if next_phase:
                    self.phase = self.phase_2
                else:
                    self.phase = self.phase_1

                self.inGame = self.phase.update()
                delta_time = time.get_ticks()
                left_click, scroll_click, right_click = mouse.get_pressed()

                self.player = draw.circle(tela.surface, [255]*3, self.player_position, self.player_size)
                self.enemy = [
                    draw.rect(tela.surface, (240,42,42), Rect(self.enemy_position[0].x, self.enemy_position[0].y, 20, 20),2), 
                    draw.rect(tela.surface, (240,42,42), Rect(self.enemy_position[1].x, self.enemy_position[1].y, 20, 20),2)
    
                ]

                raycast = Raycaster(player.position, mouse_position(), tela.size)
                self.ray = raycast.raycast_with_collision(tela.size, self.walls)
                self.raycast_line = draw.aaline(tela.surface, [0, 255, 0], self.player_position, self.ray)
                

                for i in self.walls:
                    draw.rect(tela.surface, [160]*3, i)


                for i in self.all_items:
                    if not i in self.items_taken:
                        item, pos = i
                        rect = item.get_rect()

                        if pos == 0:
                            tela.surface.blit(item, Vector2(0, 0))
                            rect.update(0, 0, items_size.x, items_size.y)

                        elif pos == 1:
                            tela.surface.blit(item, Vector2(tela.size.x - items_size.x, 0))
                            rect.update(tela.size.x - items_size.x, 0, items_size.x, items_size.y)
                    
                        elif pos == 2:
                            tela.surface.blit(item, Vector2(0, tela.size.y - items_size.y))
                            rect.update(0, tela.size.y - items_size.y, items_size.x, items_size.y)

                        else:
                            tela.surface.blit(item, Vector2(tela.size.x - items_size.x, tela.size.y - items_size.y))
                            rect.update(tela.size.x - items_size.x, tela.size.y - items_size.y, items_size.x, items_size.y)
                    
                        
                        if rect.colliderect(self.player):
                            if item not in self.items_taken:
                                self.items_taken.append(i)

                self.score = len(self.items_taken) * 10

                key = key.get_pressed()
                if self.score >= 40 or key[local.K_ESCAPE]:
                    self.restart()
                    self.inMenu = False
                    self.inGame = True
                    next_phase = True

                if left_click:
                    if self.waiting_time >= self.fire_rate:
                        start_position = Vector2(self.player_position.x - 2.5, self.player_position.y - 2.5)
                        self.bullets.append((False, start_position, self.ray, Vector2(5, 5)))
                        self.waiting_time = 0
                    else:
                        self.waiting_time += abs(time.get_ticks() - delta_time)

                for bullet in self.bullets:
                    bullet_collide, bullet_origin, bullet_direction, bullet_size = bullet
                    if bullet_collide:
                        del self.bullets[self.bullets.index(bullet)]
                    else:
                        
                        b_width = bullet_origin.x - bullet_direction.x
                        b_heigth = bullet_direction.y - bullet_origin.y
                        
                        b_angle = numpy.degrees(numpy.arctan(b_heigth / b_width))

                        b_cos = numpy.cos(b_angle)
                        b_sin = numpy.sin(b_angle) 
                        if b_width<0:
                            b_sin = -b_sin
                            b_cos = -b_cos
                            
                        bullet_origin.y += b_cos * 0.1
                        bullet_origin.x += b_sin * 0.1
                        
                        bullet_collide = projectile_collided(bullet_origin, bullet_size, self.walls) | bullet_collide
                        self.bullets[self.bullets.index(bullet)] = (bullet_collide, bullet_origin, bullet_direction, bullet_size)
                        bullet_rect = draw.rect(tela.surface, [255, 127, 0], (bullet_origin, bullet_size))
                    self.i= -1
                for enemy in self.enemy:
                    self.i = self.i+1
                    if bullet_rect.colliderect(enemy):
                        del self.bullets[self.bullets.index(bullet)]
                        self.enemy_die(self.i)

                    if enemy.colliderect(self.player):
                        self.inPause = True

                default_bold = get_font(bold = True)
                text_center = center(Vector2(30,0))
                write(f"score: {self.score}", Color(255, 255, 255), Vector2(tela_center.x - text_center.x, 0), Color(0, 0, 0), default_bold)

            events = event.get()
            tela.close()
            for event in events:
                write("Game Over", Color(255, 0, 0), Vector2(tela_center.x - 120, tela_center.y - 60), font=get_font("Impact", 60))
                write("press any key to exit", position=Vector2(tela_center.x - 90, tela_center.y + 30), font=get_font(size=30))
                self.update()
                if event.type == local.KEYDOWN or event.type == local.MOUSEBUTTONDOWN:
                    self.inGame = False
                    self.inPause = False
                    self.inMenu = True
                    self.restart()
                    return self.run()

if __name__ == '__main__':
    game = Game()
    game.run()
