import random
import Values
import Paint

class Enemy:

    alive = True
    colour = (0, 0, 0)
    enemy_type = 0
    max_delay = 100
    min_delay = 50
    delay = 0
    attacking = False
    fake = False
    is_sec_attack = False
    lower = False
    sec_attack = 0
    sec_delay = 0
    slower = 0
    temp_speed = 0
    attack_count = 0
    has_attacked_count = 0
    max_attack_count = 10
    max_health = [100, 300, 50, 500, 130, 75]
    min_health = [50, 150, 10, 200, 80, 50]
    health = 0
    damage = 0
    max_speed = [2, 1, 4, 1.5, 1.8, 3]
    min_speed = [1, 0.5, 2, 0.5, 0.8, 1.5]
    x_speed = 0
    y_speed = 0
    speed = 0
    name = ''
    r = 75/2
    x = -r
    y = 200

    def __init__(self, num, fake):
        self.fake = fake
        if not fake:
            self.damage = Values.enemy_damage[self.enemy_type]
            self.delay = random.randint(self.min_delay, self.max_delay)
            self.x = self. x - num * self.delay
            self.enemy_type = random.randint(0, Values.num_enemy - 1)
            self.health = random.randint(self.min_health[self.enemy_type] + 20 * Values.wave, self.max_health[self.enemy_type] + 20 * Values.wave)
            fraction = 1 - (self.health - (self.min_health[self.enemy_type] + 20 * Values.wave)) / (self.max_health[self.enemy_type] + 20 * Values.wave)
            self.speed = fraction * (self.max_speed[self.enemy_type] - self.min_speed[self.enemy_type]) + self.min_speed[self.enemy_type]
            self.x_speed = self.speed
            self.colour = Paint.enemy_col[self.enemy_type]
            self.name = Values.enemy_name[self.enemy_type]

    def die(self):
        if self.health <= 0:
            self.alive = False

    def sec_attacking(self):
        if self.has_attacked_count > self.max_attack_count:
            self.is_sec_attack = False
        else:
            if self.attack_count < self.sec_delay:
                self.attack_count += 1
            else:
                if not Values.invincible_enemy:
                    self.health -= self.sec_attack
                self.attack_count = 0
                self.has_attacked_count += 1

    def fix_speed(self):
        if self.x < 750 and self.y < 600:
            self.x_speed = self.speed
        elif self.y < 600:
            self.y_speed = self.speed
        else:
            self.x_speed = -self.speed

    def move(self):
        self.die()
        if self.is_sec_attack:
            self.sec_attacking()
            if not self.lower:
                self.temp_speed = self.speed
                self.speed *= self.slower
                if self.speed < 0.3:
                    self.speed = 0.3
                self.fix_speed()
                self.lower = True
        elif self.lower:
            self.lower = False
            self.attack_count = 0
            self.sec_delay = 0
            self.sec_attack = 0
            self.has_attacked_count = 0
            self.speed = self.temp_speed
            self.fix_speed()

        if self.x > 750:
            self.x = 750
            self.y_speed = self.speed
            self.x_speed = 0
        if self.y > 600:
            self.y = 600
            self.x_speed = -self.speed
            self.y_speed = 0
        if self.x > 0:
            self.attacking = True
        if self.x < 0 and self.attacking:
            Values.health -= self.damage
            self.alive = False

        self.x = self.x + self.x_speed
        self.y = self.y + self.y_speed
