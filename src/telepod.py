from src.prop import Prop

class Telepod(Prop):

    def __init__(self):
        super().__init__("Telepod")

    def make_sound(self):
        return "schwoooof"
