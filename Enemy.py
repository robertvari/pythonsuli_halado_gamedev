from DF_Base import Spaceship
from ResourceManager import ResourceManager
from Player import Player
import pyray as RL
from abc import abstractmethod
from random import randint

class Enemy(Spaceship):
    ROTATION = -90
    SOURCE_RECT = (64, 64, 16, 16)

    def __init__(self, resource_manager: ResourceManager, spawn_position: RL.Vector2, player: Player):
        super().__init__(resource_manager)
        self.position = spawn_position
        self._player = player

    @abstractmethod
    def update(self, dt: float):
        pass

class EnemySpawner:
    def __init__(self, resource_manager: ResourceManager, enemy_count: int, player: Player):
        self.enemies: list[Enemy] = []

        for i in range(enemy_count):
            self.enemies.append(
                Drone(
                    resource_manager,
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
        self.rotate_to(self._player.position)