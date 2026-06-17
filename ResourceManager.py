import os
import pyray as RL

class ResourceManager:
    RESOURCES_DIR = os.path.join(os.path.dirname(__file__), "resources")
    TEXTURE_EXTENSIONS = {".png"}

    def __init__(self):
        self._textures: dict[str, RL.Texture2D] = {}
        self._load_textures()

    def _load_textures(self):
        for filename in os.listdir(self.RESOURCES_DIR):
            name, ext = os.path.splitext(filename)
            if ext.lower() in self.TEXTURE_EXTENSIONS:
                path = os.path.join(self.RESOURCES_DIR, filename)
                self._textures[name] = RL.load_texture(path)

    def get_texture(self, name: str) -> RL.Texture2D:
        if name not in self._textures:
            raise KeyError(f"Texture '{name}' not found. Available: {list(self._textures)}")
        return self._textures[name]

    def unload(self):
        for texture in self._textures.values():
            RL.unload_texture(texture)
        self._textures.clear()