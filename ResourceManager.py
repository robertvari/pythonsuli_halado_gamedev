import pyray as RL
import os

class ResourceManager:
    RESOURCE_DIR = os.path.join(os.path.dirname(__file__), "resources")
    TEXTURE_EXTENSIONS = {".png"}

    def __init__(self):
        # type annotation
        self._textures: dict[str, RL.Texture2D] = {}
        self._load_texture()

    # private/protected methods
    def _load_texture(self):
        for filename in os.listdir(self.RESOURCE_DIR):
            name, ext = os.path.splitext(filename)
            if ext.lower() in self.TEXTURE_EXTENSIONS:
                path = os.path.join(self.RESOURCE_DIR, filename)
                self._textures[name] = RL.load_texture(path)
    
    # Public methods
    def get_texture(self, name: str):
        if name not in self._textures:
            raise KeyError(f"Texture {name} not found")
        return self._textures[name]

    def unload(self):
        for texture in self._textures.values():
            RL.unload_texture(texture)
        self._textures.clear()