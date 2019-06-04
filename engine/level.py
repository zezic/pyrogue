from .level_registry import LevelRegistry

class Level():
    def __init__(self, size):
        self.width, self.height = size
        self.object_map = Level.make_blank_map(size)
        self.object_registry = LevelRegistry()

    @staticmethod
    def make_blank_map(size):
        width, height = size
        return [
            [None for x in range(width)]
            for y in range(height)
        ]

    def add_object(self, instance, position):
        x, y = position
        self.object_map[y][x] = instance
        self.object_registry.add_object(instance, position)

    def get_object_at(self, position):
        x, y = position
        return self.object_map[y][x]

    def move_object(self, uuid, position):
        new_x, new_y = position
        old_x, old_y = self.object_registry.get_position(uuid)
        instance = self.object_registry.get_object(uuid)
        self.object_map[new_y][new_x] = instance
        self.object_map[old_y][old_x] = None
        self.object_registry.move_object(uuid, position)

    def remove_object(self, uuid):
        old_x, old_y = self.object_registry.get_position(uuid)
        self.object_map[old_x][old_y] = None
        return self.object_registry.remove_object(uuid)
