
import pygame, sys, math, time

from pygame.locals import *

pygame.init()



#COLORS
bg = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)

c_street = (100, 100, 100)
c_fence  = (255, 5, 5)
c_finish = (255, 255, 5)

max_width = pygame.display.Info().current_w
max_height = pygame.display.Info().current_h
print(max_width,max_height)


screen = pygame.display.set_mode((max_width, max_height))#, pygame.FULLSCREEN)
screen.fill(bg)


trackList = []
a = 1
tracks = 1

while a == 1:    
    try:
        exec("trackList.append(pygame.image.load('Assets/track_" + str(tracks) + ".png'))")
    except:
        a = 0
    tracks += 1



track_counter = 0


player_1_y = 100
player_1 = pygame.Rect(100, player_1_y, 20, 20)
image_1 = pygame.image.load("Assets/car.png")

# player 2
player_2_y = 140
player_2 = pygame.Rect(100, player_2_y, 20, 20)
image_2 = pygame.image.load("Assets/car2.png")



explosion = pygame.image.load("Assets/explosion1.png")

# Variable: Player 1
pressed_1 = False
pressed_1_l = False
pressed_1_r = False
pressed_1_b = False 

position_index_1 = 0
angle_1 = 0
destroy_1 = False
count_destr_1 = 0

# Variable: Player 2
pressed_2 = False
pressed_2_l = False
pressed_2_r = False
pressed_2_b = False

position_index_2 = 0
angle_2 = 0
destroy_2 = False
count_destr_2 = 0

speed = 10
angle_ch = 5 / 8 # change angle

clock = pygame.time.Clock()
fps = 60


def resetcar(player,flag):
    if flag == True:
        screen.blit(explosion, globals()['player_' + player])
    pygame.display.update()
    globals()['destroy_' + player] = False  # Set the destroy flag for the specific player
    globals()['angle_' + player] = 0  # Reset the angle for the specific player
    globals()['count_destr_' + player] = 25


def movement(front,back,left,right,position_index, angle, player,image):
    if front == True and position_index < speed:
        position_index += 0.25
    if back == True:
        position_index -= 0.25
        
    if left == True and abs(position_index) > 2:
        angle -= angle_ch * position_index

    if right == True and abs(position_index) > 2:
        angle += angle_ch * position_index   


    if front == False and position_index > 0:
        position_index -= 0.25
    if back == False and position_index < 0:
        position_index += 0.25


    b_1 = math.cos(math.radians(angle)) * position_index 
    a_1 = math.sin(math.radians(angle)) * position_index
    player.left += round(b_1)
    player.top += round(a_1)

    image_neu = pygame.transform.rotate(image, angle*-1)    
    return image_neu, position_index, angle, player



def collison(player, position_index, destroy, image_neu,track_counter):
    try:
        if not screen.get_at((player.left + 10, player.top + 10)) == c_street:
            if position_index > 3:
                position_index = 0.5
            if position_index < -3:
                position_index = -0.5


        if screen.get_at((player.left + 10, player.top + 10)) == c_fence:
            destroy = True

        if screen.get_at((player.left + 10, player.top + 10)) == c_finish:
            track_counter += 1
            resetcar("1",False)
            resetcar("2",False)           
            if track_counter >= len(trackList):
                track_counter = 0    

    except:
        destroy = True
    if destroy == False:
        screen.blit(image_neu, player)
    
    return destroy, player, position_index,track_counter








##########
running = True
while running:
    if count_destr_1 == 1:
        player_1.left = 100 # respawn position
        player_1.top = player_1_y

    if count_destr_2 == 1:
        player_2.left = 100
        player_2.top = player_2_y



 
# Player 1
    if count_destr_1 == 0:
        image_1_neu, position_index_1, angle_1,player_1 = movement(pressed_1, pressed_1_b,pressed_1_l,pressed_1_r, position_index_1, angle_1, player_1, image_1)

    else:
        count_destr_1 -= 1

# Player 2
    if count_destr_2 == 0:
        image_2_neu, position_index_2, angle_2,player_2 = movement(pressed_2, pressed_2_b,pressed_2_l,pressed_2_r, position_index_2, angle_2, player_2, image_2)


    else:
        count_destr_2 -=1

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
            

        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
                
            if event.key == K_RETURN:
                track_counter += 1
                player_1.left = 100
                player_1.top = player_1_y
                angle_1 = 0

                player_2.left = 100
                player_2.top = player_2_y
                angle_2 = 0
                
                if track_counter >= len(trackList):
                    track_counter = 0                    

                
                
            if event.key == K_UP:
                pressed_1 = True
            if event.key == K_LEFT:
                pressed_1_l = True
            if event.key == K_RIGHT:
                pressed_1_r = True
            if event.key == K_DOWN:
                pressed_1_b = True

            if event.key == K_w:
                pressed_2 = True
            if event.key == K_a:
                pressed_2_l = True
            if event.key == K_d:
                pressed_2_r = True
            if event.key == K_s:
                pressed_2_b = True


        if event.type == KEYUP:
            if event.key == K_UP:
                pressed_1 = False
            if event.key == K_LEFT:
                pressed_1_l = False
            if event.key == K_RIGHT:
                pressed_1_r = False
            if event.key == K_DOWN:
                pressed_1_b = False

            if event.key == K_w:
                pressed_2 = False
            if event.key == K_a:
                pressed_2_l = False
            if event.key == K_d:
                pressed_2_r = False
            if event.key == K_s:
                pressed_2_b = False

    screen.fill((0, 0, 0))
    screen.blit(trackList[track_counter], (0, 0))

    if count_destr_1 == 0:
        destroy_1, player_1, position_index_1,track_counter = collison(player_1, position_index_1, destroy_1, image_1_neu,track_counter)


    else: 
        screen.blit(explosion, player_1)


# Player 2 collision detection
    if count_destr_2 == 0:
            destroy_2, player_2, position_index_2,track_counter = collison(player_2, position_index_2, destroy_2, image_2_neu,track_counter)

    else:
        screen.blit(explosion, player_2)


    if destroy_1 == True: # reset car if crashed - turn into function
        resetcar("1",True)
        
    if destroy_2 == True:
        resetcar("2",True)

    
    pygame.display.update()


    clock.tick(fps)

pygame.quit()

