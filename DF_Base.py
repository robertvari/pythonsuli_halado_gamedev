import pyray as RL
from abc import ABC, abstractmethod
from math import degrees, atan2
from ResourceManager import ResourceManager

class GameObject(ABC):
    @abstractmethod
    def update(self, dt: float):
        print("GameObject: update")

    @abstractmethod
    def draw(self):
        print("GameObject: draw")

class Spaceship(GameObject):
    SPEED = 200
    ACCELERATION = 400
    DECELERATION = 100
    SCALE = 3
    ROTATION = 0
    SOURCE_RECT = (32, 64, 16, 16)
    TEXTURE_NAME = "Ships"
    TAG = ""

    def __init__(self, resource_manager: ResourceManager, projectile_manager: ProjectileManager):
        self._texture = resource_manager.get_texture(self.TEXTURE_NAME)
        self._source_rect = RL.Rectangle(*self.SOURCE_RECT)
        self._size = self._source_rect.width * self.SCALE
        self._origin = RL.Vector2(self._size/2, self._size/2)
        self.position =RL.Vector2(RL.get_screen_width()/2, RL.get_screen_height()/2)
        self.velocity = RL.Vector2(0, 0)
        self.rotation = self.ROTATION
        self._projectile_manager = projectile_manager
    
    def rotate_to(self, target: RL.Vector2):
        direction = RL.vector2_subtract(target, self.position)
        if direction.x == 0 and direction.y == 0:
            return
        
        self.rotation = degrees(atan2(direction.y, direction.x)) + self.ROTATION

    def move(self, direction: RL.Vector2, dt: float):
        if direction.x != 0 or direction.y != 0:
            direction = RL.vector2_normalize(direction)
            target_velocity = RL.vector2_scale(direction, self.SPEED)
            rate = self.ACCELERATION
        else:
            target_velocity = RL.Vector2(0, 0)
            rate = self.DECELERATION

        self.velocity = RL.vector2_move_towards(self.velocity, target_velocity, rate * dt)
        self.position.x += self.velocity.x * dt
        self.position.y += self.velocity.y * dt

    def shoot(self, direction: RL.Vector2):
        spawn_position = RL.Vector2(self.position.x, self.position.y)
        self._projectile_manager.spawn(spawn_position, direction, self.TAG)

    def draw(self):
        dest_rect = RL.Rectangle(self.position.x, self.position.y, self._size, self._size)
        RL.draw_texture_pro(self._texture, self._source_rect, dest_rect, self._origin, self.rotation, RL.WHITE)

class Projectile(GameObject):
    SPEED = 500
    SCALE = 4
    ROTATION = 90
    SOURCE_RECT = (11, 4, 1, 2)
    TEXTURE_NAME = "Projectiles"
    DAMAGE = 10

    def __init__(self, resource_manager: ResourceManager, position: RL.Vector2, direction: RL.Vector2, owner: str):
        self._texture = resource_manager.get_texture(self.TEXTURE_NAME)
        self._source_rect = RL.Rectangle(*self.SOURCE_RECT)
        self._origin = RL.Vector2(self._source_rect.width/2, self._source_rect.height/2)

        self.position = position
        self.direction = RL.vector2_normalize(direction)
        self.owner = owner
        self.rotation = degrees(atan2(self.direction.y, self.direction.x)) + self.ROTATION

    def update(self, dt: float):
        self.position.x += self.direction.x * self.SPEED * dt
        self.position.y += self.direction.y * self.SPEED * dt

    def draw(self):
        dest_rect = RL.Rectangle(self.position.x, self.position.y, self._source_rect.width*self.SCALE, self._source_rect.height*self.SCALE)
        RL.draw_texture_pro(self._texture, self._source_rect, dest_rect, self._origin, self.rotation, RL.WHITE)

class ProjectileManager(GameObject):
    def __init__(self, resource_manager: ResourceManager):
        self._resource_manager = resource_manager
        self.projectiles: list[Projectile] = []

    def spawn(self, position: RL.Vector2, direction: RL.Vector2, owner: str):
        self.projectiles.append(Projectile(self._resource_manager, position, direction, owner))

    def update(self, dt: float):
        for projectile in self.projectiles:
            projectile.update(dt)

        self.projectiles = [p for p in self.projectiles if self._is_on_screen(p)]

    def draw(self):
        for projectile in self.projectiles:
            projectile.draw()

    def _is_on_screen(self, projectile: Projectile) -> bool:
        return (0 <= projectile.position.x <= RL.get_screen_width()
                and 0 <= projectile.position.y <= RL.get_screen_height())