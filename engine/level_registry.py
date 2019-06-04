class RegistryItem():
    def __init__(self, instance, position):
        self.instance = instance
        self.position = position


class LevelRegistry():
    def __init__(self):
        self.storage = {}

    def add_object(self, instance, position):
        self.storage.update({
            instance.uuid: RegistryItem(instance, position)
        })

    def get_object(self, uuid):
        return self.storage.get(uuid).instance

    def get_position(self, uuid):
        return self.storage.get(uuid).position

    def move_object(self, uuid, position):
        self.storage.get(uuid).position = position

    def remove_object(self, uuid):
        return self.storage.pop(uuid)
