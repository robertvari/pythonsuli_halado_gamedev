import pyray as RL
from abc import abstractmethod
from DF_Base import Spaceship
from random import randint

class Enemy(Spaceship):
    SOURCE_RECT = (64, 64, 16, 16)

    def __init__(self, resource_manager, spawn_position: RL.Vector2):
        super().__init__(resource_manager)
        self.position = spawn_position

    @abstractmethod
    def update(self, dt: float):
        pass

class EnemySpawner:
    def __init__(self, resource_manager):
        self.enemies: list[Enemy] = []

        # Spawn some enemy
        for i in range(4):
            self.enemies.append(
                Drone(resource_manager, RL.Vector2(randint(100, RL.get_screen_width() - 100), randint(100, RL.get_screen_height()-100)))
            )

    def update(self, dt: float):
        for i in self.enemies:
            i.update(dt)

    def draw(self):
        for i in self.enemies:
            i.draw()

class Drone(Enemy):
    def update(self, dt: float):
        pass