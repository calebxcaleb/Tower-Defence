import pygame
import Values
import random
from Enemy import Enemy
from Tower import Tower

pygame.init()

max_enemies = 2 * (Values.wave)
min_enemies = Values.wave
num_enemies = 0
enemies = []
towers = []
tower_money = [200, 300, 500, 300, 400, 100]
tower_1_6 = [False, False, False, False, False, False]
upgrade_money = [100, 150, 200]

def enemies_main():
    if len(enemies) == 0:
        if Values.auto:
            Values.wave += 1
            add_enemies()
        else:
            Values.is_wave = False
    if Values.is_wave:
        remove_enemy()
        move_enemy()

def add_enemies():
    global max_enemies
    global min_enemies
    global num_enemies

    max_enemies = 2 * (Values.wave)
    min_enemies = Values.wave
    num_enemies = random.randint(min_enemies, max_enemies)
    if Values.invincible_enemy:
        num_enemies = 1
    for i in range(num_enemies):
        enemy = Enemy(i, False)
        enemies.append(enemy)

def move_enemy():
    for item in enemies:
        item.move()

def remove_enemy():
    for i in range(len(enemies)):
        if not enemies[i].alive:
            if enemies[i].health <= 0:
                Values.money += Values.money_enemy
            if enemies[i] is Values.menu_enemy:
                set_menu(0)
            enemies.pop(i)
            break

def add_tower(num):
    tower = Tower(num + 1, pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
    towers.append(tower)
    tower_rect = (tower.x - tower.r, tower.y - tower.r, tower.x + tower.r, tower.y + tower.r)
    Values.rects.append(tower_rect)

def attack_tower():
    for i in range(len(towers)):
        towers[i].find_attack(enemies)

def valid_click():
    result = True

    if not pygame.mouse.get_pos()[0] < Values.screen_width - 200:
        result = False

    for i in range(len(Values.rects)):
        if Values.rects[i][0] - 40 < pygame.mouse.get_pos()[0] < Values.rects[i][2] + 40 and \
           Values.rects[i][1] - 40 < pygame.mouse.get_pos()[1] < Values.rects[i][3] + 40:
            result = False
            break

    return result

def key_check():
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_ESCAPE]:
        set_menu(0)
        for i in range(len(tower_1_6)):
            tower_1_6[i] = False

def set_menu(num):
    for i in range(len(Values.menu_items)):
        Values.menu_items[i] = False
    Values.menu_items[num] = True
    Values.menu_shop_num = 0
    Values.menu_enemy = None
    Values.menu_tower = None

def mouse_check_start():
    if pygame.mouse.get_pressed() == (1, 0, 0):
        if Values.start_button_rect[0] < pygame.mouse.get_pos()[0] < Values.start_button_rect[0] + Values.start_button_rect[2] and \
           Values.start_button_rect[1] < pygame.mouse.get_pos()[1] < Values.start_button_rect[1] + Values.start_button_rect[3]:
            Values.starting = False

        if Values.infinite_money_rect[0] < pygame.mouse.get_pos()[0] < Values.infinite_money_rect[0] + Values.infinite_money_rect[2] and \
           Values.infinite_money_rect[1] < pygame.mouse.get_pos()[1] < Values.infinite_money_rect[1] + Values.infinite_money_rect[3]:
            if Values.can_money:
                Values.infinite_money = not Values.infinite_money
                Values.can_money = False

        if Values.enemy_health_rect[0] < pygame.mouse.get_pos()[0] < Values.enemy_health_rect[0] + Values.enemy_health_rect[2] and \
           Values.enemy_health_rect[1] < pygame.mouse.get_pos()[1] < Values.enemy_health_rect[1] + Values.enemy_health_rect[3]:
            if Values.can_enemy:
                Values.invincible_enemy = not Values.invincible_enemy
                Values.can_enemy = False

def mouse_pause_check():
    if pygame.mouse.get_pressed() == (1, 0, 0):

        if Values.pause_rect[0] < pygame.mouse.get_pos()[0] < Values.pause_rect[0] + Values.pause_rect[2] and \
           Values.pause_rect[1] < pygame.mouse.get_pos()[1] < Values.pause_rect[1] + Values.pause_rect[3]:
            if Values.can_pause:
                Values.paused = not Values.paused
                Values.can_pause = False

def mouse_check():
    if pygame.mouse.get_pressed() == (1, 0, 0):

        if Values.pause_rect[0] < pygame.mouse.get_pos()[0] < Values.pause_rect[0] + Values.pause_rect[2] and \
           Values.pause_rect[1] < pygame.mouse.get_pos()[1] < Values.pause_rect[1] + Values.pause_rect[3]:
            if Values.can_pause:
                Values.paused = not Values.paused
                Values.can_pause = False

        if Values.sell_rect[0] < pygame.mouse.get_pos()[0] < Values.sell_rect[0] + Values.sell_rect[2] and \
           Values.sell_rect[1] < pygame.mouse.get_pos()[1] < Values.sell_rect[1] + Values.sell_rect[3]:
            if Values.menu_items[3]:
                for i in range(len(towers)):
                    if Values.menu_tower is towers[i]:
                        Values.money += towers[i].money * 0.8
                        set_menu(0)
                        Values.rects.pop(5 + i)
                        towers.pop(i)
                        break

        for i in range(len(Values.upgrade_rects)):
            if Values.upgrade_rects[i][0] < pygame.mouse.get_pos()[0] < Values.upgrade_rects[i][0] + Values.upgrade_rects[i][2] and \
               Values.upgrade_rects[i][1] < pygame.mouse.get_pos()[1] < Values.upgrade_rects[i][1] + Values.upgrade_rects[i][3]:
                for a in range(len(towers)):
                    if Values.menu_tower is towers[a] and towers[a].upgrade_colours[i] == towers[a].upgrade_light:
                        if Values.money >= upgrade_money[i] or Values.infinite_money:
                            towers[a].upgrade_colours[i] = towers[a].upgrade_dark
                            if not Values.infinite_money:
                                Values.money -= upgrade_money[i]
                            towers[a].money += upgrade_money[i]
                            towers[a].upgrade(i)
                            break

        if Values.start_rect[0] < pygame.mouse.get_pos()[0] < Values.start_rect[0] + Values.start_rect[2] and \
           Values.start_rect[1] < pygame.mouse.get_pos()[1] < Values.start_rect[1] + Values.start_rect[3]:
            if not Values.is_wave:
                Values.is_wave = True
                Values.wave += 1
                add_enemies()

        if Values.auto_rect[0] < pygame.mouse.get_pos()[0] < Values.auto_rect[0] + Values.auto_rect[2] and \
           Values.auto_rect[1] < pygame.mouse.get_pos()[1] < Values.auto_rect[1] + Values.auto_rect[3]:
            if not Values.auto and not Values.is_pressed_auto:
                Values.auto = True
                Values.is_wave = True
                Values.is_pressed_auto = True
            elif not Values.is_pressed_auto:
                Values.auto = False
                Values.is_pressed_auto = True

        for i in range(len(enemies)):
            if enemies[i].x - enemies[i].r < pygame.mouse.get_pos()[0] < enemies[i].x + enemies[i].r and \
               enemies[i].y - enemies[i].r < pygame.mouse.get_pos()[1] < enemies[i].y + enemies[i].r:
                set_menu(2)
                Values.menu_enemy = enemies[i]

        for i in range(len(towers)):
            if towers[i].x - towers[i].r < pygame.mouse.get_pos()[0] < towers[i].x + towers[i].r and \
               towers[i].y - towers[i].r < pygame.mouse.get_pos()[1] < towers[i].y + towers[i].r:
                set_menu(3)
                Values.menu_tower = towers[i]

        for i in range(len(Values.shop_img_rects)):
            if Values.shop_img_rects[i][0] < pygame.mouse.get_pos()[0] < Values.shop_img_rects[i][2] and \
               Values.shop_img_rects[i][1] < pygame.mouse.get_pos()[1] < Values.shop_img_rects[i][3]:
                if (Values.money >= tower_money[i] or Values.infinite_money) and not tower_1_6[i] :
                    for a in range(len(tower_1_6)):
                        tower_1_6[a] = False
                    tower_1_6[i] = True
                    set_menu(1)
                    Values.menu_shop_num = i

        for i in range(len(tower_1_6)):
            if tower_1_6[i]:
                if valid_click():
                    set_menu(0)
                    if not Values.infinite_money:
                        Values.money -= tower_money[i]
                    add_tower(i)
                    towers[len(towers) - 1].money += tower_money[i]
                    tower_1_6[i] = False
