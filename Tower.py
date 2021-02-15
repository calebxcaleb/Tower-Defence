import Paint
import Values
from Enemy import Enemy

class Tower:
    colour = (0, 0, 0)
    upgrade_light = (255, 255, 255)
    upgrade_dark = (150, 150, 150)
    upgrade_colours = [upgrade_light, upgrade_light, upgrade_light]
    r = 40
    beam_r = 20
    delay = 0
    attack = 0
    attacking = False
    damage = 0
    attack_count = 0
    area = 0
    slower = 0
    sec_attack = 0
    sec_delay = 0
    money = 0
    x = 0
    y = 0
    rect = (0, 0, 0, 0)
    enemy = Enemy(0, True)

    def __init__(self, tower_type, x, y):
        self.tower_type = tower_type
        self.x = x
        self.y = y
        self.attack = Values.tower_attack[tower_type - 1]
        self.delay = Values.tower_delay[tower_type - 1]
        self.upgrade_colours = [self.upgrade_light, self.upgrade_light, self.upgrade_light]
        if self.tower_type <= 3:
            self.assign123()
        elif self.tower_type == 4:
            self.assign4()
        elif self.tower_type == 5:
            self.assign5()
        elif self.tower_type == 6:
            self.assign6()

    def assign123(self):
        self.area = 150
        self.rect = (self.x - self.area, self.y - self.area, 2 * self.area, 2 * self.area)
        if self.tower_type == 1:
            self.colour = Paint.green
        elif self.tower_type == 2:
            self.colour = Paint.blue
        elif self.tower_type == 3:
            self.colour = Paint.gray

    def assign4(self):
        self.r = 60
        self.rect = (0, 0, Values.screen_width, Values.screen_height)
        self.area = Values.screen_width/2
        self.colour = Paint.orange

    def assign5(self):
        self.r = 60
        self.area = 150
        self.rect = (self.x - self.area, self.y - self.area, 2 * self.area, 2 * self.area)
        self.colour = Paint.lime_yellow
        self.sec_attack = 4
        self.sec_delay = 100
        self.slower = 0.5

    def assign6(self):
        self.r = 40
        self.area = 150
        self.rect = (self.x - self.area, self.y - self.area, 2 * self.area, 2 * self.area)
        self.colour = Paint.brown
        self.enemy = [Enemy(0, True)]

    def upgrade(self, num):
        if num == 0:
            self.attack += Values.tower_upgrade_attack[self.tower_type - 1]
        elif num == 1:
            self.delay -= Values.tower_upgrade_delay[self.tower_type - 1]
        elif num == 2:
            self.attack += Values.tower_upgrade_attack[self.tower_type - 1]
            self.delay -= Values.tower_upgrade_delay[self.tower_type - 1]

    def attack_enemy(self):
        if self.attack_count < self.delay:
            self.attack_count += 1
        else:
            if not Values.invincible_enemy:
                self.enemy.health -= self.attack
            self.damage += self.attack
            self.attack_count = 0

    def farther(self, now_enemy, new_enemy):
        if now_enemy.x_speed > 0:
            if new_enemy.x_speed > 0:
                return new_enemy.x > now_enemy.x
            else:
                return True
        elif now_enemy.x_speed == 0:
            if new_enemy.x_speed == 0:
                return new_enemy.y > now_enemy.y
            else:
                return new_enemy.x_speed < 0
        elif now_enemy.x_speed < 0:
            if new_enemy.x_speed < 0:
                return new_enemy.x < now_enemy.x
            else:
                return False

        return False

    def attack6(self):
        if self.attack_count < self.delay:
            self.attack_count += 1
        else:
            if not Values.invincible_enemy:
                for enem in self.enemy:
                    enem.health -= self.attack
            self.damage += self.attack
            self.attack_count = 0

    def find_attack(self, enemies):
        self.enemy = Enemy(3, True)
        self.attacking = False

        if self.tower_type == 6:
            self.enemy = [Enemy(0, True)]

        for i in range(len(enemies)):
            if enemies[i].x - enemies[i].r < self.rect[0] + self.rect[2] and enemies[i].x + enemies[i].r > self.rect[0] and \
               enemies[i].y - enemies[i].r < self.rect[1] + self.rect[3] and enemies[i].y + enemies[i].r > self.rect[1]:
                if self.tower_type == 6:
                    self.enemy.append(enemies[i])
                if self.tower_type == 5:
                    self.enemy = enemies[i]
                    self.attacking = True
                    break
                if self.tower_type != 6 and (self.enemy.fake or self.farther(self.enemy, enemies[i])):
                    self.enemy = enemies[i]
                self.attacking = True

        if self.attacking:
            if self.tower_type == 6:
                self.enemy.pop(0)
                self.attack6()
            else:
                self.attack_enemy()
                if self.tower_type == 5:
                    self.enemy.has_attacked_count = 0
                    self.enemy.sec_attack = self.sec_attack
                    self.enemy.sec_delay = self.sec_delay
                    self.enemy.slower = self.slower
                    self.enemy.is_sec_attack = True

        # self.attack_enemy()

        if self.tower_type == 6:
            for enem in self.enemy:
                if enem.fake:
                    self.attack_count = 0
                    self.attacking = False
        elif self.enemy.fake:
            self.attack_count = 0
            self.attacking = False
