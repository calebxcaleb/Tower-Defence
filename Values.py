# Game values
health = 100
wave = 0
money_enemy = 20
starting = True
invincible_enemy = False
infinite_money = False
can_enemy = True
can_money = True
paused = False
can_pause = True
max_money = 10000
min_money = 500
num_enemy = 6
money = 500
is_wave = False
auto = False
is_pressed_auto = False
price1 = 200
price2 = 300
price3 = 500
screen_width = 1200
menu_width = 230
screen_height = 800
blob_r = 25
enemy_damage = [10, 20, 5, 30, 10, 6]
enemy_name = ['Slime', 'Ork', 'Robot', 'Alien', 'Skeleton', 'UFO']
tower_r = [40, 40, 40, 60, 60, 40]
tower_attack = [29, 49, 69, 15, 10, 5]
tower_delay = [30, 45, 60, 120, 200, 10]
tower_upgrade_attack = [2, 4, 6, 5, 3, 2]
tower_upgrade_delay = [1, 2, 3, 5, 20, 2]
tower_name = ['Archer Tower', 'Mage Tower', 'Cannon Tower', 'Sniper Tower', 'Toxic Tower', 'Plasma Tower']
tower_speed_life = ['Speed: ', 'Speed: ', 'Speed: ', 'Speed: ', 'Speed: ', 'Speed: ']

# Menu item
menu_shop_num = 0
menu_enemy = None
menu_tower = None
menu_empty = True
menu_shop = False
menu_enemy = False
menu_enemy_num = 0
menu_items = [menu_empty, menu_shop, menu_enemy, menu_tower]

# Rectangle Areas
start_button_rect = ((screen_width + menu_width) / 2 - 300, screen_height - 450, 600, 200)
infinite_money_rect = (50, 50, 300, 100)
enemy_health_rect = (screen_width + menu_width - 350, 50, 300, 100)
top_rect = (0, 0, screen_width, 50)
right_rect = (screen_width - 200, 0, screen_width, screen_height)
sell_rect = (screen_width + menu_width/2 - 105, screen_height - 75, 210, 50)
upgrade1_rect = (screen_width + menu_width/2 - 80, screen_height - 300, 160, 50)
upgrade2_rect = (screen_width + menu_width/2 - 80, screen_height - 225, 160, 50)
upgrade3_rect = (screen_width + menu_width/2 - 80, screen_height - 150, 160, 50)
upgrade_rects = [upgrade1_rect, upgrade2_rect, upgrade3_rect]
shop_img1_rect = (screen_width - 200, 70, screen_width, 170)
shop_img2_rect = (screen_width - 200, 170, screen_width, 270)
shop_img3_rect = (screen_width - 200, 270, screen_width, 370)
shop_img4_rect = (screen_width - 200, 370, screen_width, 470)
shop_img5_rect = (screen_width - 200, 470, screen_width, 570)
shop_img6_rect = (screen_width - 200, 570, screen_width, 670)
shop_img_rects = [shop_img1_rect, shop_img2_rect, shop_img3_rect, shop_img4_rect, shop_img5_rect, shop_img6_rect]
wave_rect = (screen_width - 157, 10, 120, 50)
start_rect = (screen_width - 170, screen_height - 60, 150, 50)
auto_rect = (screen_width - 170, screen_height - 120, 150, 50)
shop_rect = (screen_width - 200, 70, 200, 600)
menu_rect = (screen_width, 0, menu_width, screen_height)
pause_rect = (screen_width - 400, 0, 120, 50)
# tower1_rect = (screen_width - 100 - 20, 250 - 20, screen_width - 100 + 20, 250 + 20)
# tower2_rect = (screen_width - 100 - 20, 400 - 20, screen_width - 100 + 20, 400 + 20)
# tower3_rect = (screen_width - 100 - 20, 550 - 20, screen_width - 100 + 20, 550 + 20)
# tower123_rect = [tower1_rect, tower2_rect, tower3_rect]
path1_rect = (0, 150, 700, 250)
path2_rect = (700, 150, 800, 650)
path3_rect = (0, 550, 700, 650)
paths = [path1_rect, path2_rect, path3_rect]
rects = [top_rect, right_rect, path1_rect, path2_rect, path3_rect]