from src.prop import Prop

class LaserGun(Prop):

    def __init__(self):
        super().__init__("Laser Gun")

    def make_sound(self):
        return "pew pew pew"