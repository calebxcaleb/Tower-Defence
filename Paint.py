import pygame
import Values
import Functions

pygame.init()

# Colours
brown = (205, 133, 63)          # path
orange = (255, 165, 0)          # tower 4
gray = (128, 128, 128)          # tower 3
green = (50, 205, 50)           # background
dark_green = (0, 128, 0)        # menu
black = (0, 0, 0)               # text
white = (255, 255, 255)         # general
blue = (0, 191, 255)            # tower 1
dark_blue = (0, 0, 128)         # tower 1 dark
yellow = (255, 255, 0)          # tower 2 / start wave
lime_yellow = (173, 255, 47)    # tower 5
purple = (255, 0, 255)          # tower 3
dark_purple = (75, 0, 130)      # tower 3 dark
dark_yellow = (128, 128, 0)     # start wave / tower 2 dark
red = (220, 20, 60)             # enemy light
dark_red = (128, 0, 0)          # enemy heave
now_yellow = yellow             # start wave current colour
auto_yellow = yellow            # auto wave current colour
enemy_col = [red, dark_red, purple, lime_yellow, black, green]
tower_col = [green, blue, gray, orange, lime_yellow, brown]  # colour of towers
now_white_money = white
now_white_enemy = white
now_white_pause = white

# Images
blob_img = pygame.image.load('blob.png')
enemy1_img = pygame.image.load('enemy2.png')
enemy2_img = pygame.image.load('enemy1.png')
enemy3_img = pygame.image.load('enemy3.png')
enemy4_img = pygame.image.load('enemy4.png')
enemy5_img = pygame.image.load('enemy5.png')
enemy6_img = pygame.image.load('enemy6.png')
enemy_imgs = [enemy1_img, enemy2_img, enemy3_img, enemy4_img, enemy5_img, enemy6_img]
tower1_img = pygame.image.load('tower1.png')
tower2_img = pygame.image.load('tower2.png')
tower3_img = pygame.image.load('tower3.png')
tower4_img = pygame.image.load('tower4.png')
tower5_img = pygame.image.load('tower5.png')
tower4_s_img = pygame.image.load('tower4_small.png')
tower5_s_img = pygame.image.load('tower5_small.png')
# tower6_img = pygame.image.load('tower6.png')
tower6_img = pygame.image.load('tower7.png')
tower_s_imgs = [tower1_img, tower2_img, tower3_img, tower4_s_img, tower5_s_img, tower6_img]
tower_imgs = [tower1_img, tower2_img, tower3_img, tower4_img, tower5_img, tower6_img]
beam1_img = pygame.image.load('beam1.png')
beam2_img = pygame.image.load('beam2.png')
beam3_img = pygame.image.load('beam3.png')
beam4_img = pygame.image.load('beam4.png')
beam5_img = pygame.image.load('beam5.png')
beam6_img = pygame.image.load('beam6.png')
beam_imgs = [beam1_img, beam2_img, beam3_img, beam4_img, beam5_img, beam6_img]

# Fonts
font1 = pygame.font.Font('freesansbold.ttf', 20)
font2 = pygame.font.Font('freesansbold.ttf', 40)
font3 = pygame.font.Font('freesansbold.ttf', 15)
font4 = pygame.font.Font('freesansbold.ttf', 30)
font_start_big = pygame.font.Font('freesansbold.ttf', 80)
font_pause = pygame.font.Font('freesansbold.ttf', 160)

# Set up the drawing window
screen = pygame.display.set_mode([Values.screen_width + Values.menu_width, Values.screen_height])
pygame.display.set_caption('Show Text')

# Text - Starting
title1_text = font_start_big.render('Caleb\'s', True, black, blue)
title1_textRect = title1_text.get_rect()
title1_textRect.center = ((Values.screen_width + Values.menu_width) / 2, 80)
title2_text = font_start_big.render('Tower Defence', True, black, blue)
title2_textRect = title2_text.get_rect()
title2_textRect.center = ((Values.screen_width + Values.menu_width) / 2, 200)
start_button_text = font_start_big.render('Start', True, black, white)
start_button_textRect = start_button_text.get_rect()
start_button_textRect.center = ((Values.screen_width + Values.menu_width) / 2, Values.screen_height - 350)
start_money_text = font4.render('Infinite Money', True, black, now_white_money)
start_money_textRect = start_money_text.get_rect()
start_money_textRect.center = (200, 100)
start_enemy_text = font4.render('Invincible Enemies', True, black, now_white_enemy)
start_enemy_textRect = start_enemy_text.get_rect()
start_enemy_textRect.center = (Values.screen_width + Values.menu_width - 200, 100)

# Text - empty
menu_empty1_text = font2.render('Tower', True, black, white)
menu_empty1_textRect = menu_empty1_text.get_rect()
menu_empty1_textRect.center = (Values.screen_width + Values.menu_width/2, Values.screen_height/2 - 20)
menu_empty2_text = font2.render('Defence', True, black, white)
menu_empty2_textRect = menu_empty2_text.get_rect()
menu_empty2_textRect.center = (Values.screen_width + Values.menu_width/2, Values.screen_height/2 + 20)

# Text - pause
pause_button_text = font1.render('Pause', True, black, None)
pause_button_textRect = pause_button_text.get_rect()
pause_button_textRect.center = (Values.pause_rect[0] + Values.pause_rect[2] / 2, Values.pause_rect[1] + Values.pause_rect[3] / 2)
pause_text = font_pause.render('Paused...', True, black, None)
pause_textRect = pause_text.get_rect()
pause_textRect.center = (Values.screen_width / 2, Values.screen_height / 2)

# Text - health
health_text = font1.render(' = ' + str(Values.health), True, black, dark_green)
health_textRect = health_text.get_rect()
health_textRect.center = (75, 25)

# Text - money
money_text = font1.render(' = ' + str(0), True, black, dark_green)
money_textRect = money_text.get_rect()
money_textRect.center = (220, 25)

# Text - store
store1_text = font3.render(Values.tower_name[0], True, black, white)
store1_textRect = store1_text.get_rect()
store1_textRect.center = (Values.screen_width - 60, 100)
store2_text = font3.render(Values.tower_name[1], True, black, white)
store2_textRect = store2_text.get_rect()
store2_textRect.center = (Values.screen_width - 60, 200)
store3_text = font3.render(Values.tower_name[2], True, black, white)
store3_textRect = store3_text.get_rect()
store3_textRect.center = (Values.screen_width - 60, 300)
store4_text = font3.render(Values.tower_name[3], True, black, white)
store4_textRect = store4_text.get_rect()
store4_textRect.center = (Values.screen_width - 60, 400)
store5_text = font3.render(Values.tower_name[4], True, black, white)
store5_textRect = store5_text.get_rect()
store5_textRect.center = (Values.screen_width - 60, 500)
store6_text = font3.render(Values.tower_name[5], True, black, white)
store6_textRect = store6_text.get_rect()
store6_textRect.center = (Values.screen_width - 60, 600)

store1m_text = font3.render('$ ' + str(Functions.tower_money[0]), True, black, white)
store1m_textRect = store1m_text.get_rect()
store1m_textRect.center = (Values.screen_width - 60, 140)
store2m_text = font3.render('$ ' + str(Functions.tower_money[1]), True, black, white)
store2m_textRect = store2m_text.get_rect()
store2m_textRect.center = (Values.screen_width - 60, 240)
store3m_text = font3.render('$ ' + str(Functions.tower_money[2]), True, black, white)
store3m_textRect = store3m_text.get_rect()
store3m_textRect.center = (Values.screen_width - 60, 340)
store4m_text = font3.render('$ ' + str(Functions.tower_money[3]), True, black, white)
store4m_textRect = store4m_text.get_rect()
store4m_textRect.center = (Values.screen_width - 60, 440)
store5m_text = font3.render('$ ' + str(Functions.tower_money[4]), True, black, white)
store5m_textRect = store5m_text.get_rect()
store5m_textRect.center = (Values.screen_width - 60, 540)
store6m_text = font3.render('$ ' + str(Functions.tower_money[5]), True, black, white)
store6m_textRect = store6m_text.get_rect()
store6m_textRect.center = (Values.screen_width - 60, 640)

# Text - enemy number
enemy_text = font1.render(str(len(Functions.enemies)) + ' / ' + str(Functions.num_enemies), True, black, dark_green)
enemy_textRect = enemy_text.get_rect()
enemy_textRect.center = (600, 25)

# Text - wave
wave_text = font1.render('Wave ' + str(Values.wave), True, black, white)
wave_textRect = wave_text.get_rect()
wave_textRect.center = (Values.screen_width - 100, 35)
start_wave_text = font1.render('Start Wave', True, black, now_yellow)
start_wave_textRect = start_wave_text.get_rect()
start_wave_textRect.center = (Values.screen_width - 100, Values.screen_height - 35)
auto_wave_text = font1.render('Auto Wave', True, black, auto_yellow)
auto_wave_textRect = auto_wave_text.get_rect()
auto_wave_textRect.center = (Values.screen_width - 100, Values.screen_height - 95)

# Text - store menu
menu_store_title_text = font1.render(Values.tower_name[0], True, black, white)
menu_store_title_textRect = menu_store_title_text.get_rect()
menu_store_title_textRect.center = (Values.screen_width + Values.menu_width/2, 20)
menu_store_money_text = font1.render('Price: ' + str(Functions.tower_money[0]), True, black, white)
menu_store_money_textRect = menu_store_money_text.get_rect()
menu_store_money_textRect.center = (Values.screen_width + 100, 200)
menu_store_attack_text = font1.render('Attack: ' + str(0), True, black, white)
menu_store_attack_textRect = menu_store_attack_text.get_rect()
menu_store_attack_textRect.center = (Values.screen_width + 100, 300)
menu_store_speed_text = font1.render('Speed: ' + str(0), True, black, white)
menu_store_speed_textRect = menu_store_speed_text.get_rect()
menu_store_speed_textRect.center = (Values.screen_width + 100, 400)

# Text - tower menu
menu_tower_title_text = font1.render(Values.tower_name[0], True, black, white)
menu_tower_title_textRect = menu_tower_title_text.get_rect()
menu_tower_title_textRect.center = (Values.screen_width + Values.menu_width/2, 20)
menu_tower_attack_text = font1.render('Attack: ' + str(0), True, black, white)
menu_tower_attack_textRect = menu_tower_attack_text.get_rect()
menu_tower_attack_textRect.center = (Values.screen_width + 100, 200)
menu_tower_speed_text = font1.render('Speed: ' + str(0), True, black, white)
menu_tower_speed_textRect = menu_tower_speed_text.get_rect()
menu_tower_speed_textRect.center = (Values.screen_width + 100, 300)
menu_tower_damage_text = font1.render('Damage: ' + str(0), True, black, white)
menu_tower_damage_textRect = menu_tower_damage_text.get_rect()
menu_tower_damage_textRect.center = (Values.screen_width + 100, 400)
menu_tower_sell_text = font1.render('Sell : ' + str(0), True, black, red)
menu_tower_sell_textRect = menu_tower_sell_text.get_rect()
menu_tower_sell_textRect.center = (Values.screen_width + Values.menu_width/2, Values.screen_height - 50)
menu_tower_upgrade1_text = font1.render('Upgrade 1: ' + str(Functions.upgrade_money[0]), True, black, white)
menu_tower_upgrade1_textRect = menu_tower_upgrade1_text.get_rect()
menu_tower_upgrade1_textRect.center = (Values.screen_width + Values.menu_width/2, Values.screen_height - 275)
menu_tower_upgrade2_text = font1.render('Upgrade 2: ' + str(Functions.upgrade_money[1]), True, black, white)
menu_tower_upgrade2_textRect = menu_tower_upgrade2_text.get_rect()
menu_tower_upgrade2_textRect.center = (Values.screen_width + Values.menu_width/2, Values.screen_height - 200)
menu_tower_upgrade3_text = font1.render('Upgrade 3: ' + str(Functions.upgrade_money[2]), True, black, white)
menu_tower_upgrade3_textRect = menu_tower_upgrade3_text.get_rect()
menu_tower_upgrade3_textRect.center = (Values.screen_width + Values.menu_width/2, Values.screen_height - 125)

# Text - enemy menu
menu_enemy_title_text = font1.render('', True, black, white)
menu_enemy_title_textRect = menu_enemy_title_text.get_rect()
menu_enemy_title_textRect.center = (Values.screen_width + Values.menu_width/2, 20)
menu_enemy_attack_text = font1.render('Attack: ' + str(0), True, black, white)
menu_enemy_attack_textRect = menu_enemy_attack_text.get_rect()
menu_enemy_attack_textRect.center = (Values.screen_width + 100, 200)
menu_enemy_health_text = font1.render('Health: ' + str(0), True, black, white)
menu_enemy_health_textRect = menu_enemy_health_text.get_rect()
menu_enemy_health_textRect.center = (Values.screen_width + 100, 300)
menu_enemy_speed_text = font1.render('Speed: ' + str(0), True, black, white)
menu_enemy_speed_textRect = menu_enemy_speed_text.get_rect()
menu_enemy_speed_textRect.center = (Values.screen_width + 100, 400)

def wave_colour():
    global now_yellow
    global start_wave_text

    if Values.is_wave and now_yellow == yellow:
        now_yellow = dark_yellow
        start_wave_text = font1.render('Start Wave', True, black, now_yellow)
    elif not Values.is_wave and now_yellow == dark_yellow:
        now_yellow = yellow
        start_wave_text = font1.render('Start Wave', True, black, now_yellow)

def auto_colour():
    global auto_yellow
    global auto_wave_text

    if Values.auto and auto_yellow == yellow:
        auto_yellow = dark_yellow
        auto_wave_text = font1.render('Auto Wave', True, black, auto_yellow)
    elif not Values.auto and auto_yellow == dark_yellow:
        auto_yellow = yellow
        auto_wave_text = font1.render('Auto Wave', True, black, auto_yellow)

def update_text():
    global health_text
    global money_text
    global wave_text
    global enemy_text

    health_text = font1.render(' = ' + str(Values.health), True, black, dark_green)
    money_text = font1.render(' = ' + str(Values.money), True, black, dark_green)
    wave_text = font1.render('Wave ' + str(Values.wave), True, black, white)
    enemy_text = font1.render(str(len(Functions.enemies)) + ' / ' + str(Functions.num_enemies), True, black, dark_green)

def display_menu_empty():
    global menu_empty1_textRect
    global menu_empty1_text
    global menu_empty2_textRect
    global menu_empty2_text

    screen.blit(menu_empty1_text,menu_empty1_textRect)
    screen.blit(menu_empty2_text,menu_empty2_textRect)

def display_menu_shop(num):
    global menu_store_title_textRect
    global menu_store_title_text
    global menu_store_speed_textRect
    global menu_store_speed_text
    global menu_store_money_textRect
    global menu_store_money_text
    global menu_store_attack_textRect
    global menu_store_attack_text

    menu_store_title_text = font1.render(Values.tower_name[num], True, black, white)
    menu_store_title_textRect = menu_store_title_text.get_rect()
    menu_store_title_textRect.center = (Values.screen_width + Values.menu_width / 2, 20)
    screen.blit(menu_store_title_text, menu_store_title_textRect)
    pygame.draw.rect(screen, tower_col[num], (Values.screen_width + Values.menu_width/2 - (Values.tower_r[num] + 10), 100 - (Values.tower_r[num] + 10), (Values.tower_r[num] + 10) * 2, (Values.tower_r[num] + 10) * 2))
    pygame.draw.rect(screen, black, (Values.screen_width + Values.menu_width/2 - (Values.tower_r[num] + 10), 100 - (Values.tower_r[num] + 10), (Values.tower_r[num] + 10) * 2, (Values.tower_r[num] + 10) * 2), 3)
    screen.blit(tower_imgs[num], (Values.screen_width + Values.menu_width/2 - Values.tower_r[num], 100 - Values.tower_r[num]))
    # pygame.draw.circle(screen, tower_col[num], (Values.screen_width + Values.menu_width/2, 200), 40)
    menu_store_attack_text = font1.render('Attack: ' + str(Values.tower_attack[num]), True, black, white)
    screen.blit(menu_store_attack_text, menu_store_attack_textRect)
    menu_store_speed_text = font1.render(Values.tower_speed_life[num] + str(Values.tower_delay[num]), True, black, white)
    screen.blit(menu_store_speed_text, menu_store_speed_textRect)
    menu_store_money_text = font1.render('Price: ' + str(Functions.tower_money[num]), True, black, white)
    screen.blit(menu_store_money_text, menu_store_money_textRect)

def display_menu_enemy(enemy):
    global menu_enemy_title_textRect
    global menu_enemy_title_text
    global menu_enemy_attack_textRect
    global menu_enemy_attack_text
    global menu_enemy_health_textRect
    global menu_enemy_health_text
    global menu_enemy_speed_textRect
    global menu_enemy_speed_text

    pygame.draw.rect(screen, enemy.colour, (Values.screen_width + Values.menu_width / 2 - 50, 100 - 50, 100, 100))
    pygame.draw.rect(screen, black, (Values.screen_width + Values.menu_width / 2 - 50, 100 - 50, 100, 100), 3)
    screen.blit(enemy_imgs[enemy.enemy_type], (Values.screen_width + Values.menu_width/2 - enemy.r, 100 - enemy.r))
    pygame.draw.circle(screen, black, (enemy.x, enemy.y), enemy.r, 5)
    menu_enemy_title_text = font1.render(enemy.name, True, black, white)
    menu_enemy_title_textRect = menu_enemy_title_text.get_rect()
    menu_enemy_title_textRect.center = (Values.screen_width + Values.menu_width / 2, 20)
    screen.blit(menu_enemy_title_text, menu_enemy_title_textRect)
    menu_enemy_attack_text = font1.render('Attack: ' + str(enemy.damage), True, black, white)
    screen.blit(menu_enemy_attack_text, menu_enemy_attack_textRect)
    menu_enemy_health_text = font1.render('Health: ' + str(enemy.health), True, black, white)
    screen.blit(menu_enemy_health_text, menu_enemy_health_textRect)
    menu_enemy_speed_text = font1.render('Speed: ' + str(round(enemy.speed,2)), True, black, white)
    screen.blit(menu_enemy_speed_text, menu_enemy_speed_textRect)

def display_menu_tower(tower):
    global menu_tower_title_textRect
    global menu_tower_title_text
    global menu_tower_attack_textRect
    global menu_tower_attack_text
    global menu_tower_speed_textRect
    global menu_tower_speed_text
    global menu_tower_damage_textRect
    global menu_tower_damage_text
    global menu_tower_upgrade1_textRect
    global menu_tower_upgrade1_text
    global menu_tower_upgrade2_textRect
    global menu_tower_upgrade2_text
    global menu_tower_upgrade3_textRect
    global menu_tower_upgrade3_text
    global menu_tower_sell_textRect
    global menu_tower_sell_text

    menu_tower_title_text = font1.render(Values.tower_name[tower.tower_type-1], True, black, white)
    menu_tower_title_textRect = menu_tower_title_text.get_rect()
    menu_tower_title_textRect.center = (Values.screen_width + Values.menu_width / 2, 20)
    screen.blit(menu_tower_title_text, menu_tower_title_textRect)
    pygame.draw.rect(screen, tower.colour, (Values.screen_width + Values.menu_width / 2 - (tower.r + 10), 100 - (tower.r + 10), (tower.r + 10) * 2, (tower.r + 10) * 2))
    pygame.draw.rect(screen, black, (Values.screen_width + Values.menu_width / 2 - (tower.r + 10), 100 - (tower.r + 10), (tower.r + 10) * 2, (tower.r + 10) * 2), 3)
    screen.blit(tower_imgs[tower.tower_type-1], (Values.screen_width + Values.menu_width/2 - tower.r, 100 - tower.r))
    pygame.draw.circle(screen, black, (tower.x, tower.y), tower.r, 5)
    pygame.draw.rect(screen, black, (tower.x - 150, tower.y - 150, 300, 300), 5)
    menu_tower_attack_text = font1.render('Attack: ' + str(tower.attack), True, black, white)
    screen.blit(menu_tower_attack_text, menu_tower_attack_textRect)
    menu_tower_speed_text = font1.render(Values.tower_speed_life[tower.tower_type-1] + str(tower.delay), True, black, white)
    screen.blit(menu_tower_speed_text, menu_tower_speed_textRect)
    menu_tower_damage_text = font1.render('Damage: ' + str(tower.damage), True, black, white)
    screen.blit(menu_tower_damage_text, menu_tower_damage_textRect)
    pygame.draw.rect(screen, red, Values.sell_rect)
    pygame.draw.rect(screen, black, Values.sell_rect, 5)
    pygame.draw.rect(screen, tower.upgrade_colours[0], Values.upgrade1_rect)
    pygame.draw.rect(screen, black, Values.upgrade1_rect, 5)
    menu_tower_upgrade1_text = font1.render('Upgrade 1: ' + str(Functions.upgrade_money[0]), True, black, tower.upgrade_colours[0])
    screen.blit(menu_tower_upgrade1_text, menu_tower_upgrade1_textRect)
    pygame.draw.rect(screen, tower.upgrade_colours[1], Values.upgrade2_rect)
    pygame.draw.rect(screen, black, Values.upgrade2_rect, 5)
    menu_tower_upgrade2_text = font1.render('Upgrade 2: ' + str(Functions.upgrade_money[1]), True, black, tower.upgrade_colours[1])
    screen.blit(menu_tower_upgrade2_text, menu_tower_upgrade2_textRect)
    pygame.draw.rect(screen, tower.upgrade_colours[2], Values.upgrade3_rect)
    pygame.draw.rect(screen, black, Values.upgrade3_rect, 5)
    menu_tower_upgrade3_text = font1.render('Upgrade 3: ' + str(Functions.upgrade_money[2]), True, black, tower.upgrade_colours[2])
    screen.blit(menu_tower_upgrade3_text, menu_tower_upgrade3_textRect)
    menu_tower_sell_text = font1.render('Sell : ' + str(round(tower.money * 0.8)) + '', True, black, red)
    menu_tower_sell_textRect = menu_tower_sell_text.get_rect()
    menu_tower_sell_textRect.center = (Values.screen_width + Values.menu_width / 2, Values.screen_height - 50)
    screen.blit(menu_tower_sell_text, menu_tower_sell_textRect)

def button_colour():
    global now_white_pause

    if Values.paused:
        now_white_pause = gray
    else:
        now_white_pause = white

def draw_blob(x, y):
    screen.blit(blob_img, (x - Values.blob_r, y - Values.blob_r))

def paint():
    # set colour
    wave_colour()
    auto_colour()
    button_colour()

    # update text values
    update_text()

    # background
    screen.fill(green)
    pygame.draw.rect(screen, dark_green, Values.top_rect)
    pygame.draw.rect(screen, dark_green, Values.right_rect)
    pygame.draw.rect(screen, white, Values.menu_rect)

    # path for enemies
    pygame.draw.rect(screen, brown, (0, 150, 700, 100))
    pygame.draw.rect(screen, brown, (700, 150, 100, 500))
    pygame.draw.rect(screen, brown, (0, 550, 700, 100))

    # lines
    pygame.draw.line(screen, black, (0, 50), (Values.screen_width - 200, 50), 3)
    pygame.draw.line(screen, black, (Values.screen_width - 200, 50), (Values.screen_width - 200, Values.screen_height), 3)
    pygame.draw.line(screen, black, (Values.screen_width, 0), (Values.screen_width, Values.screen_height), 3)
    pygame.draw.line(screen, black, (0, 0), (Values.screen_width + Values.menu_width, 0), 6)
    pygame.draw.line(screen, black, (0, 0), (0, Values.screen_height), 6)
    pygame.draw.line(screen, black, (Values.screen_width + Values.menu_width, 0), (Values.screen_width + Values.menu_width, Values.screen_height), 9)
    pygame.draw.line(screen, black, (0, Values.screen_height), (Values.screen_width + Values.menu_width, Values.screen_height), 9)

    # store
    pygame.draw.rect(screen, white, Values.shop_rect)
    pygame.draw.rect(screen, black, Values.shop_rect, 3)
    screen.blit(tower1_img, (Values.screen_width - 190, 80))
    screen.blit(tower2_img, (Values.screen_width - 190, 180))
    screen.blit(tower3_img, (Values.screen_width - 190, 280))
    screen.blit(tower4_s_img, (Values.screen_width - 190, 380))
    screen.blit(tower5_s_img, (Values.screen_width - 190, 480))
    # pygame.draw.circle(screen, blue, (Values.screen_width - 100, 250), 40)
    screen.blit(tower6_img, (Values.screen_width - 190, 580))
    screen.blit(store1_text, store1_textRect)
    screen.blit(store2_text, store2_textRect)
    screen.blit(store3_text, store3_textRect)
    screen.blit(store4_text, store4_textRect)
    screen.blit(store5_text, store5_textRect)
    screen.blit(store6_text, store6_textRect)
    screen.blit(store1m_text, store1m_textRect)
    screen.blit(store2m_text, store2m_textRect)
    screen.blit(store3m_text, store3m_textRect)
    screen.blit(store4m_text, store4m_textRect)
    screen.blit(store5m_text, store5m_textRect)
    screen.blit(store6m_text, store6m_textRect)
    # pygame.draw.circle(screen, yellow, (Values.screen_width - 100, 400), 40)
    # pygame.draw.circle(screen, purple, (Values.screen_width - 100, 550), 40)
    pygame.draw.line(screen, black, (Values.screen_width - 200, 170), (Values.screen_width, 170), 5)
    pygame.draw.line(screen, black, (Values.screen_width - 200, 270), (Values.screen_width, 270), 5)
    pygame.draw.line(screen, black, (Values.screen_width - 200, 370), (Values.screen_width, 370), 5)
    pygame.draw.line(screen, black, (Values.screen_width - 200, 470), (Values.screen_width, 470), 5)
    pygame.draw.line(screen, black, (Values.screen_width - 200, 570), (Values.screen_width, 570), 5)

    # health
    screen.blit(health_text, health_textRect)
    pygame.draw.circle(screen, red, (20, 20), 10)
    pygame.draw.circle(screen, red, (35, 20), 10)
    pygame.draw.circle(screen, red, (27.5, 33), 8)

    # money
    global money_text
    money_text = font1.render(' = ' + str(round(Values.money)), True, black, dark_green)
    screen.blit(money_text, money_textRect)
    pygame.draw.circle(screen, yellow, (170, 25), 15)

    # enemy num
    screen.blit(enemy_text, enemy_textRect)

    # wave
    pygame.draw.rect(screen, white, Values.wave_rect)
    pygame.draw.rect(screen, black, Values.wave_rect, 3)
    screen.blit(wave_text, wave_textRect)
    pygame.draw.rect(screen, now_yellow, Values.start_rect)
    pygame.draw.rect(screen, black, Values.start_rect, 3)
    screen.blit(start_wave_text, start_wave_textRect)
    pygame.draw.rect(screen, auto_yellow, Values.auto_rect)
    pygame.draw.rect(screen, black, Values.auto_rect, 3)
    screen.blit(auto_wave_text, auto_wave_textRect)

    # pause button
    pygame.draw.rect(screen, now_white_pause, Values.pause_rect)
    pygame.draw.rect(screen, black, Values.pause_rect, 5)
    screen.blit(pause_button_text, pause_button_textRect)

    # menu methods
    if Values.menu_items[0]:
        display_menu_empty()
    elif Values.menu_items[1]:
        display_menu_shop(Values.menu_shop_num)
    elif Values.menu_items[2]:
        display_menu_enemy(Values.menu_enemy)
    elif Values.menu_items[3]:
        display_menu_tower(Values.menu_tower)

    # list - enemy
    for enemy in Functions.enemies:
        screen.blit(enemy_imgs[enemy.enemy_type], (enemy.x - enemy.r, enemy.y - enemy.r))
        if enemy.is_sec_attack:
            draw_blob(enemy.x, enemy.y)
        # pygame.draw.circle(screen, enemy.colour, (enemy.x, enemy.y), enemy.r)

    # list - tower
    for tower in Functions.towers:
        screen.blit(tower_imgs[tower.tower_type-1], (tower.x - tower.r, tower.y - tower.r))
        # pygame.draw.circle(screen, tower.colour, (tower.x, tower.y), tower.r)
        if tower.attacking:
            if tower.tower_type == 6:
                for enem in tower.enemy:
                    dist = tower.attack_count / tower.delay
                    new_x = enem.x - tower.x
                    new_y = enem.y - tower.y
                    screen.blit(beam_imgs[tower.tower_type - 1], (tower.x + new_x * dist - tower.beam_r, tower.y + new_y * dist - tower.beam_r))
                    pygame.draw.line(screen, lime_yellow, (tower.x, tower.y), (enem.x, enem.y), 3)
            else:
                dist = tower.attack_count / tower.delay
                new_x = tower.enemy.x - tower.x
                new_y = tower.enemy.y - tower.y
                screen.blit(beam_imgs[tower.tower_type - 1], (tower.x + new_x * dist - tower.beam_r, tower.y + new_y * dist - tower.beam_r))
                # pygame.draw.circle(screen, tower.dark_colour, (tower.x + new_x * dist, tower.y + new_y * dist), 20)

    # buying tower
    for i in range(len(Values.shop_img_rects)):
        if Functions.tower_1_6[i]:
            pygame.draw.circle(screen, black, (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]), Values.tower_r[i], 5)
            pygame.draw.rect(screen, black, (pygame.mouse.get_pos()[0] - 150, pygame.mouse.get_pos()[1] - 150, 300, 300), 5)
            # pygame.draw.circle(screen, black, (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]), 150, 5)
            screen.blit(tower_imgs[i], (pygame.mouse.get_pos()[0] - Values.tower_r[i], pygame.mouse.get_pos()[1] - Values.tower_r[i]))
            # pygame.draw.circle(screen, tower_col[i], (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]), Values.tower_r[i])

    # pause menu display
    if Values.paused:
        screen.blit(pause_text, pause_textRect)

    pygame.display.flip()

def change_white():
    global now_white_money
    global now_white_enemy

    if Values.infinite_money:
        now_white_money = gray
    else:
        now_white_money = white

    if Values.invincible_enemy:
        now_white_enemy = gray
    else:
        now_white_enemy = white

def start_paint():
    global start_money_text
    global start_enemy_text

    screen.fill(blue)

    change_white()

    pygame.draw.rect(screen, white, Values.start_button_rect)
    pygame.draw.rect(screen, black, Values.start_button_rect, 20)
    pygame.draw.rect(screen, now_white_money, Values.infinite_money_rect)
    pygame.draw.rect(screen, black, Values.infinite_money_rect, 10)
    pygame.draw.rect(screen, now_white_enemy, Values.enemy_health_rect)
    pygame.draw.rect(screen, black, Values.enemy_health_rect, 10)

    start_money_text = font4.render('Infinite Money', True, black, now_white_money)
    start_enemy_text = font4.render('Invincible Enemies', True, black, now_white_enemy)

    screen.blit(title1_text, title1_textRect)
    screen.blit(title2_text, title2_textRect)
    screen.blit(start_button_text, start_button_textRect)
    screen.blit(start_money_text, start_money_textRect)
    screen.blit(start_enemy_text, start_enemy_textRect)

    for i in range(len(tower_s_imgs)):
        screen.blit(tower_s_imgs[i], ((Values.screen_width + Values.menu_width) / 7 * (i+1) - 40, Values.screen_height - 140))

    screen.blit(enemy_imgs[0], ((Values.screen_width + Values.menu_width) / 7 - 40, Values.screen_height - 540))
    screen.blit(enemy_imgs[1], ((Values.screen_width + Values.menu_width) / 7 - 40, Values.screen_height - 340))
    screen.blit(enemy_imgs[2], ((Values.screen_width + Values.menu_width) / 7 * 6 - 40, Values.screen_height - 540))
    screen.blit(enemy_imgs[3], ((Values.screen_width + Values.menu_width) / 7 * 6 - 40, Values.screen_height - 340))
    screen.blit(enemy_imgs[4], ((Values.screen_width + Values.menu_width) / 7 - 140, Values.screen_height - 440))
    screen.blit(enemy_imgs[5], ((Values.screen_width + Values.menu_width) / 7 * 6 + 60, Values.screen_height - 440))

    pygame.display.flip()
