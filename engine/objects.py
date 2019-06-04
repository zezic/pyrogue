from uuid import uuid4


class BaseObjectAttrChecker(type):
    def __call__(cls, *args, **kwargs):
        instance = type.__call__(cls, *args, **kwargs)
        instance.self_check()
        return instance


class BaseObject(metaclass=BaseObjectAttrChecker):
    char = None # a text symbol for visual representation
    is_consumable = None # can be eaten by player or monster

    def __init__(self, uuid=None):
        self.uuid = uuid or uuid4()

    def self_check(self):
        if self.char is None:
            raise NotImplementedError(
                'Subclass must define self.char'
            )
        if self.is_consumable is None:
            raise NotImplementedError(
                'Subclass must define self.consumable property'
            )

    def render(self):
        return self.char


class PlayerObject(BaseObject):
    char = '@'
    is_consumable = False


class GoldObject(BaseObject):
    char = '$'
    is_consumable = True
