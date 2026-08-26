from DF_Base import Spaceship, ProjectileManager
from Player import Player
from ResourceManager import ResourceManager
from Player import Player
import pyray as RL
from abc import abstractmethod
from random import randint

class Enemy(Spaceship):
    SPEED = 100
    FOLLOWDISTANCE_MIN = 200
    ROTATION = -90
    SOURCE_RECT = (64, 64, 16, 16)
    SPEED=100
    FOLLOWDISTANCE_MIN=150
    TAG = "enemy"
    FIRE_COOLDOWN = 1

    def __init__(self, resource_manager: ResourceManager, projectile_manager: ProjectileManager, spawn_position: RL.Vector2, player: Player):
        super().__init__(resource_manager, projectile_manager)
        self.position = spawn_position
        self._player = player
        self._fire_timer = 0

    @abstractmethod
    def update(self, dt: float):
        # follow player
        direction = RL.Vector2()
        if RL.vector2_length(RL.vector2_subtract(self._player.position, self.position)) > self.FOLLOWDISTANCE_MIN:
            direction = RL.vector2_subtract(self._player.position, self.position)

        self.move(direction, dt)

        # track player
        self.rotate_to(self._player.position)

        # shoot player periodically
        self._fire_timer += dt
        if self._fire_timer >= self.FIRE_COOLDOWN:
            self._fire_timer -= self.FIRE_COOLDOWN
            self.shoot(RL.vector2_subtract(self._player.position, self.position))


class EnemySpawner:
    def __init__(self, resource_manager: ResourceManager, projectile_manager: ProjectileManager, enemy_count: int, player: Player):
        self.enemies: list[Enemy] = []

        for i in range(enemy_count):
            self.enemies.append(
                Drone(
                    resource_manager,
                    projectile_manager,
                    RL.Vector2(
                        randint(100, RL.get_screen_width()-100),
                        randint(100, RL.get_screen_height()-100)
                    ),
                    player
                )
            )

    def update(self, dt: float):
        for i in self.enemies:
            i.update(dt)

    def draw(self):
        for i in self.enemies:
            i.draw()

class Drone(Enemy):
    def update(self, dt: float):
        super().update(dt)