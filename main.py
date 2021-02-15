# Tower Defence Game

import pygame
import Values
import Paint
import Functions

pygame.init()

# Main game loop
running = True
while running:

    while Values.paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Values.paused = False
                running = False
            if not Values.can_pause:
                Values.can_pause = True
        Paint.paint()
        Functions.mouse_pause_check()

    while Values.starting:
        Paint.start_paint()
        Functions.mouse_check_start()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Values.starting = False
                running = False
            if event.type == pygame.MOUSEBUTTONUP and not Values.can_enemy:
                Values.can_enemy = True
            if event.type == pygame.MOUSEBUTTONUP and not Values.can_money:
                Values.can_money = True

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            if Values.is_pressed_auto:
                Values.is_pressed_auto = False
            if not Values.can_pause:
                Values.can_pause = True

    Paint.paint()
    Functions.key_check()
    Functions.mouse_check()
    Functions.enemies_main()
    Functions.attack_tower()

pygame.quit()
