class Engine():
    def __init__(self):
        self.levels = {}

    def add_level(self, level, idx):
        self.levels.update({idx: level})

    def walk(self, level_idx, object_uuid, magnitude):
        delta_x, delta_y = magnitude
        level = self.levels.get(level_idx)
        old_x, old_y = level.object_registry.get_position(object_uuid)
        target_x = max(0, min(level.width - 1, old_x + delta_x))
        target_y = max(0, min(level.height - 1, old_y + delta_y))
        if target_x == old_x and target_y == old_y:
            return
        level.move_object(object_uuid, (target_x, target_y))
